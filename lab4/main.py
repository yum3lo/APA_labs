import time
import matplotlib.pyplot as plt
import random

class Graph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.inf = float('inf')
        self.graph = [[self.inf] * num_vertices for _ in range(num_vertices)]
        for i in range(num_vertices):
            self.graph[i][i] = 0

    def add_edge(self, u, v, weight):
        self.graph[u][v] = weight

    def dijkstra(self, source):
        distance = [float('inf')] * self.num_vertices
        distance[source] = 0
        visited = [False] * self.num_vertices
        start_time = time.perf_counter()

        for _ in range(self.num_vertices):
            # Find the vertex with the minimum distance
            min_dist = float('inf')
            min_vertex = -1
            for v in range(self.num_vertices):
                if not visited[v] and distance[v] < min_dist:
                    min_dist = distance[v]
                    min_vertex = v

            if min_vertex == -1:
                break

            visited[min_vertex] = True
            for v in range(self.num_vertices):
                if not visited[v] and self.graph[min_vertex][v] != float('inf') and \
                        distance[min_vertex] + self.graph[min_vertex][v] < distance[v]:
                    distance[v] = distance[min_vertex] + self.graph[min_vertex][v]

        end_time = time.perf_counter()
        return end_time - start_time

    def floyd_warshall(self):
        dist = [row[:] for row in self.graph]
        start_time = time.perf_counter()

        for k in range(self.num_vertices):
            for i in range(self.num_vertices):
                for j in range(self.num_vertices):
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

        end_time = time.perf_counter()
        return end_time - start_time

# Empirical Analysis
num_vertices = 180
num_edges_sparse = 400
num_edges_dense = num_vertices * (num_vertices - 1)

dijkstra_times_sparse = []
floyd_warshall_times_sparse = []
dijkstra_times_dense = []
floyd_warshall_times_dense = []

# Sparse Graphs
for i in range(20):  # Repeat the experiment 20 times
    g = Graph(num_vertices)
    for _ in range(num_edges_sparse):
        u = random.randint(0, num_vertices - 1)
        v = random.randint(0, num_vertices - 1)
        weight = random.randint(1, 100)
        g.add_edge(u, v, weight)

    dijkstra_time = g.dijkstra(0)
    floyd_warshall_time = g.floyd_warshall()
    dijkstra_times_sparse.append(dijkstra_time)
    floyd_warshall_times_sparse.append(floyd_warshall_time)

# Dense Graphs
for i in range(20):  # Repeat the experiment 20 times
    g = Graph(num_vertices)
    for u in range(num_vertices):
        for v in range(num_vertices):
            if u != v:
                weight = random.randint(1, 100)
                g.add_edge(u, v, weight)

    dijkstra_time = g.dijkstra(0)
    floyd_warshall_time = g.floyd_warshall()
    dijkstra_times_dense.append(dijkstra_time)
    floyd_warshall_times_dense.append(floyd_warshall_time)

# Plotting
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.plot(range(1, 21), dijkstra_times_sparse, label='Dijkstra (Sparse)')
plt.plot(range(1, 21), floyd_warshall_times_sparse, label='Floyd-Warshall (Sparse)')
plt.xlabel('Number of Tests')
plt.ylabel('Time (s)')
plt.title('Empirical Analysis for Sparse Graphs')
plt.legend()

plt.subplot(1, 2, 2)
plt.plot(range(1, 21), dijkstra_times_dense, label='Dijkstra (Dense)')
plt.plot(range(1, 21), floyd_warshall_times_dense, label='Floyd-Warshall (Dense)')
plt.xlabel('Number of Tests')
plt.ylabel('Time (s)')
plt.title('Empirical Analysis for Dense Graphs')
plt.legend()

plt.tight_layout()
plt.show()