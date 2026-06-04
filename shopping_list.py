from recipe import Recipe
from Ingredient import Ingredient

class ShoppingList:
    def __init__(self):
        self._items = []

    def add_recipe(self, recipe:Recipe, portions:float):
        if not portions > 0:
            raise ValueError("portions должно быть больше 0")

        new_recipe = recipe.scale(portions)

        for ingredient in new_recipe.ingredients:
            self._items.append((ingredient, recipe.title))

##
    def remove_recipe(self, title:str):
        items = []
        for ingredient, recipe_title in self._items:
            if recipe_title == title: continue
            else: items.append((ingredient, recipe_title))

        self._items = items

    def get_list(self):
        all_items = {}
        for ingredient, title in self._items:
            key = (ingredient.name, ingredient.unit)

            all_items[key] += ingredient.quantity

        res = []
        for (name, unit), quantity in all_items.items():
            res.append(Ingredient(name, quantity, unit))
        return sorted(res, key=lambda i: i.name)

    def __add__(self, other:ShoppingList):
        new_list = ShoppingList()
        new_list._items = self._items + other._items
        return new_list