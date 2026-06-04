from Ingredient import Ingredient

class Recipe:
    def __init__(self, title:str, ingredients:list):
        self.title = title
        self.ingredients = ingredients

    def add_ingredient(self, ingredient:Ingredient):
        for old_ingredient in self.ingredients:
            if old_ingredient == ingredient:
                old_ingredient.quantity += ingredient.quantity
                return

        self.ingredients.append(ingredient)

    @staticmethod
    def is_valid_ratio(ratio):
        if type(ratio) in (int, float) and ratio > 0: return True
        else: return False

    def scale(self, ratio:float):
        if not self.is_valid_ratio(ratio):
            raise ValueError("ratio должно быть > 0")

        new_ingredients = []
        for ingredient in self.ingredients:
            new_ingredient = Ingredient(ingredient.name, ingredient.quantity * ratio, ingredient.unit)
            new_ingredients.append(new_ingredient)

        return Recipe(self.title, new_ingredients)

    def __len__(self):
        return len(self.ingredients)

    def __str__(self):
        str_recipe = self.title

        for ingredient in self.ingredients:
            str_recipe += "\n" + ingredient

        return str_recipe