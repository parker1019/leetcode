from typing import List

class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]
        for u, v, time in roads:
            graph[u].append((v, time))
            graph[v].append((u, time))

        mod = 10**9 + 7
        dist = [float('inf')] * n
        dist[0] = 0
        paths = [0] * n
        paths[0] = 1
        visited = [False] * n
        for _ in range(n):
            u = -1
            for i in range(n):
                if not visited[i] and (u == -1 or dist[i] < dist[u]):
                    u = i
            visited[u] = True
            for v, time in graph[u]:
                if dist[u] + time < dist[v]:
                    dist[v] = dist[u] + time
                    paths[v] = paths[u]
                elif dist[u] + time == dist[v]:
                    paths[v] = (paths[v] + paths[u]) % mod
        return paths[-1]
