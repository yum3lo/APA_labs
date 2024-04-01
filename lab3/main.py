import time
import matplotlib.pyplot as plt
import random

class Graph:
    def __init__(self, num_vertices, num_edges):
        self.graph = {i: [] for i in range(num_vertices)}
        for _ in range(num_edges):
            u = random.randint(0, num_vertices - 1)
            v = random.randint(0, num_vertices - 1)
            self.add_edge(u, v)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def bfs(self, start):
        marked = [False] * len(self.graph)
        queue = [start]
        start_time = time.perf_counter()
        while queue:
            v = queue.pop(0)
            if not marked[v]:
                marked[v] = True
                for w in self.graph.get(v, []):
                    if not marked[w]:
                        queue.append(w)
        end_time = time.perf_counter()
        return end_time - start_time

    def dfs_recursive(self, v):
        marked = [False] * len(self.graph)
        start_time = time.perf_counter()
        self.dfs_util_recursive(v, marked)
        end_time = time.perf_counter()
        return end_time - start_time

    def dfs_util_recursive(self, v, marked):
        marked[v] = True
        for w in self.graph.get(v, []):
            if not marked[w]:
                self.dfs_util_recursive(w, marked)

    def dfs_iterative(self, start):
        marked = [False] * len(self.graph)
        stack = [start]
        start_time = time.perf_counter()
        while stack:
            v = stack.pop()
            if not marked[v]:
                marked[v] = True
                for w in self.graph.get(v, []):
                    if not marked[w]:
                        stack.append(w)
        end_time = time.perf_counter()
        return end_time - start_time

# Parameters for the experiment
num_vertices = 1000
num_edges = 3000

bfs_times = []
dfs_times = []
for i in range(20):  # Repeat the experiment 20 times
    g = Graph(num_vertices, num_edges)
    bfs_time = g.bfs(0)
    dfs_time = g.dfs_recursive(0)
    # dfs_time = g.dfs_iterative(0)
    bfs_times.append(bfs_time)
    dfs_times.append(dfs_time)

plt.plot(range(1, 21), bfs_times, label='BFS')
plt.plot(range(1, 21), dfs_times, label='DFS (Recursive)')
# plt.plot(range(1, 21), dfs_times, label='DFS (Iterative)')
plt.xlabel('Number of tests')
plt.ylabel('Time (s)')
plt.title('Comparison of BFS and Recursive DFS based on Time')
# plt.title('Comparison of BFS and Iterative DFS based on Time')
plt.legend()
plt.show()