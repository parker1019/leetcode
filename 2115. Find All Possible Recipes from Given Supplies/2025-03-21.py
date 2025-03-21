from typing import List

class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        recipe_dic = {}
        for i in range(len(recipes)):
            recipe_dic[recipes[i]] = ingredients[i]
        
        result = []
        for supply in supplies:
            for recipe in recipes:
                if supply in recipe_dic[recipe]:
                    recipe_dic[recipe].remove(supply)
                    if len(recipe_dic[recipe]) == 0:
                        supplies.append(recipe)
                        result.append(recipe)
        
        return result