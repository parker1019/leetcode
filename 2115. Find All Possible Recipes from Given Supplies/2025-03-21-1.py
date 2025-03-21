from typing import List
from collections import defaultdict, deque

class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        graph = defaultdict(list)
        in_degree = defaultdict(int)
        
        for i in range(len(recipes)):
            recipe = recipes[i]
            for ingredient in ingredients[i]:
                graph[ingredient].append(recipe)
                in_degree[recipe] += 1
        
        queue = deque(supplies)
        result = []
        
        while queue:
            current = queue.popleft()
            if current in recipes:
                result.append(current)
            for neighbor in graph[current]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        
        return result
