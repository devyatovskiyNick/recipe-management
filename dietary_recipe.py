class DietaryRecipe(Recipe):
    def __init__(self, title:str, diet_type:str, ingredients:list):
        self.title = title
        self.ingredients = ingredients
        self.diet_type = diet_type

    def scale(self, ratio:float):
        new_recipe = super().scale(ratio)
        return DietaryRecipe(new_recipe.title, self.diet_type, new_recipe.ingredients)

    def __str__(self):
        recipe_str = super().__str__()
        return f"[{self.diet_type}] {recipe_str}"