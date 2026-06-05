import pytest

from Ingredient import Ingredient
from recipe import Recipe

def test_create_ingredient():
    ingredient = Ingredient("Соль", 822, "мг")

    assert ingredient.name == "Соль"
    assert ingredient.quantity == 822.0
    assert ingredient.unit == "мг"

def test_str():
    ingredient = Ingredient("Соль", 822, "мг")

    assert str(ingredient) == "Соль: 822.0 мг"

def test_eq():
    ingredient_1 = Ingredient("лук", 12, "г")

    ingredient_2 = Ingredient("лук", 120, "г")
    ingredient_3 = Ingredient("лук", 12, "кг")
    ingredient_4 = Ingredient("перец", 12, "г")

    assert ingredient_1 == ingredient_2
    assert ingredient_1 != ingredient_3
    assert ingredient_1 != ingredient_4





ingredients = [Ingredient("яйца", 2, "шт"), Ingredient("соль", 1, "ст.л"),
                   Ingredient("помидоры", 0.5, "шт")]
def test_create_recipe():
    recipe = Recipe("яичница", ingredients)
    assert recipe.title == "яичница"
    assert recipe.ingredients == ingredients

def test_len():
    recipe = Recipe("яичница", ingredients)
    assert len(recipe) == 3

def test_add_ingredient():
    recipe = Recipe("яичница", ingredients)

    recipe.add_ingredient(Ingredient("лук", 12, "г"))
    assert len(recipe) == 4
    assert recipe.ingredients[3] == Ingredient("лук", 12, "г")

    recipe.add_ingredient(Ingredient("яйца", 2, "шт"))
    assert len(recipe) == 4
    assert recipe.ingredients[0].quantity == 4

def test_scale():
    recipe = Recipe("яичница", ingredients)
    scaled_recipe = recipe.scale(4.2)
    assert recipe is not scaled_recipe
    assert recipe.ingredients[0].quantity == 2


    with pytest.raises(ValueError):
        recipe.scale(0)
    with pytest.raises(ValueError):
        recipe.scale(-69)


    scaled_recipe = recipe.scale(3)
    assert len(recipe) == 3
    assert scaled_recipe.ingredients[0].quantity == 6
    assert scaled_recipe.ingredients[1].quantity == 3
    assert scaled_recipe.ingredients[2].quantity == 1.5



