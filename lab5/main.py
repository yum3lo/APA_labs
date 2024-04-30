import time
import matplotlib.pyplot as plt
import random

class Graph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.graph = [[] for _ in range(num_vertices)]

    def add_edge(self, u, v, weight):
        self.graph[u].append((v, weight))
        self.graph[v].append((u, weight))  # For undirected graphs

    def prim(self):
        start_time = time.perf_counter()

        # Initialize MST set, key values, and parent array
        mst_set = set()
        key = [float('inf')] * self.num_vertices
        parent = [-1] * self.num_vertices

        # Randomly select the starting vertex
        start_vertex = random.randint(0, self.num_vertices - 1)
        key[start_vertex] = 0

        while len(mst_set) < self.num_vertices:
            # Find the vertex with the minimum key value
            min_key = float('inf')
            min_vertex = -1
            for v in range(self.num_vertices):
                if v not in mst_set and key[v] < min_key:
                    min_key = key[v]
                    min_vertex = v

            mst_set.add(min_vertex)

            # Update key values of adjacent vertices
            for neighbor, weight in self.graph[min_vertex]:
                if neighbor not in mst_set and weight < key[neighbor]:
                    key[neighbor] = weight
                    parent[neighbor] = min_vertex

        end_time = time.perf_counter()
        return end_time - start_time

    def kruskal(self):
        start_time = time.perf_counter()

        # Initialize MST edges list
        mst_edges = []

        # Sort edges by weight
        edges = []
        for u in range(self.num_vertices):
            for v, weight in self.graph[u]:
                edges.append((u, v, weight))
        edges.sort(key=lambda x: x[2])

        # Initialize parent array for union-find
        parent = [i for i in range(self.num_vertices)]

        # Helper function to find the parent of a vertex in a disjoint set
        def find(u):
            while parent[u] != u:
                parent[u] = parent[parent[u]]
                u = parent[u]
            return u

        # Helper function to perform union of two sets
        def union(u, v):
            parent_u = find(u)
            parent_v = find(v)
            parent[parent_u] = parent_v

        for u, v, weight in edges:
            if find(u) != find(v):
                mst_edges.append((u, v))
                union(u, v)

        end_time = time.perf_counter()
        return end_time - start_time

# Empirical Analysis
num_vertices_range = [50, 100, 150, 200, 250]
prim_times = []
kruskal_times = []

for num_vertices in num_vertices_range:
    prim_avg_time = 0
    kruskal_avg_time = 0
    num_tests = 20
    
    for _ in range(num_tests):
        g = Graph(num_vertices)
        for u in range(num_vertices):
            for v in range(u + 1, num_vertices):
                weight = random.randint(1, 100)
                g.add_edge(u, v, weight)

        prim_avg_time += g.prim()
        kruskal_avg_time += g.kruskal()

    prim_avg_time /= num_tests
    kruskal_avg_time /= num_tests

    prim_times.append(prim_avg_time)
    kruskal_times.append(kruskal_avg_time)

# Plotting
plt.plot(num_vertices_range, prim_times, label="Prim's Algorithm")
plt.plot(num_vertices_range, kruskal_times, label="Kruskal's Algorithm")
plt.xlabel('Number of Vertices')
plt.ylabel('Average Time (s)')
plt.title("Plot of Prim's and Kruskal's Algorithms")
plt.legend()
plt.grid(True)
plt.show()