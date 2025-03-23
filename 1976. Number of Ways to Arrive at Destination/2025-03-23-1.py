from typing import List
import heapq

class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]
        for u, v, time in roads:
            graph[u].append((v, time))
            graph[v].append((u, time))

        mod = 10**9 + 7
        # dist[i] is the shortest distance from node 0 to node i
        dist = [float('inf')] * n
        # dist[0] is 0 because the shortest distance from node 0 to node 0 is 0
        dist[0] = 0
        # count[i] is the number of ways to reach node i from node 0
        count = [0] * n
        # count[0] is 1 because there is only one way to reach node 0 from node 0
        count[0] = 1 
        
        # (dist, node)
        priority_queue = [(0, 0)]

        while priority_queue:
            current_dist, current_node = heapq.heappop(priority_queue)
            if current_dist > dist[current_node]:
                continue
            for neighbor, time in graph[current_node]:
                # If the current distance plus the time to reach the neighbor is less than the shortest distance to reach the neighbor
                if current_dist + time < dist[neighbor]:
                    dist[neighbor] = current_dist + time
                    # The number of ways to reach the neighbor is the same as the number of ways to reach the current node
                    count[neighbor] = count[current_node]
                    heapq.heappush(priority_queue, (dist[neighbor], neighbor))
                # If the current distance plus the time to reach the neighbor is equal to the shortest distance to reach the neighbor
                elif current_dist + time == dist[neighbor]:
                    # The number of ways to reach the neighbor is the sum of the number of ways to reach the neighbor and the number of ways to reach the current node
                    count[neighbor] = (count[neighbor] + count[current_node]) % mod
        return count[-1]

