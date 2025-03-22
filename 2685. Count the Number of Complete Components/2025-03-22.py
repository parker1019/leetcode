from collections import defaultdict
from typing import List

class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        visited = [False] * n
        def dfs(node):
            stack = [node]
            component_nodes = set()
            edge_count = 0 
            while stack:
                print(stack)
                cur = stack.pop()
                if cur not in component_nodes:
                    component_nodes.add(cur)
                    for neighbor in graph[cur]:
                        edge_count += 1
                        if not visited[neighbor]:
                            stack.append(neighbor)
                            visited[neighbor] = True
            return component_nodes, edge_count // 2
        complete_components = 0
        for i in range(n):
            if not visited[i]:
                visited[i] = True
                component_nodes, edge_count = dfs(i)
                node_count = len(component_nodes)
                if edge_count == node_count * (node_count - 1) // 2:
                    complete_components += 1
        
        return complete_components