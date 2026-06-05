import pytest
from matplotlib.pyplot import title

from Ingredient import Ingredient
from recipe import Recipe
from shopping_list import ShoppingList

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



def test_create_recipe():
    ingredients = [Ingredient("яйца", 2, "шт"), Ingredient("соль", 1, "ст.л"),
                   Ingredient("помидоры", 0.5, "шт")]
    recipe = Recipe("яичница", ingredients)
    assert recipe.title == "яичница"
    assert recipe.ingredients == ingredients

def test_len():
    ingredients = [Ingredient("яйца", 2, "шт"), Ingredient("соль", 1, "ст.л"),
                   Ingredient("помидоры", 0.5, "шт")]
    recipe = Recipe("яичница", ingredients)
    assert len(recipe) == 3

def test_add_ingredient():
    ingredients = [Ingredient("яйца", 2, "шт"), Ingredient("соль", 1, "ст.л"),
                   Ingredient("помидоры", 0.5, "шт")]
    recipe = Recipe("яичница", ingredients)

    recipe.add_ingredient(Ingredient("лук", 12, "г"))
    assert len(recipe) == 4
    assert recipe.ingredients[3] == Ingredient("лук", 12, "г")

    recipe.add_ingredient(Ingredient("яйца", 2, "шт"))
    assert len(recipe) == 4
    assert recipe.ingredients[0].quantity == 4

def test_scale():
    ingredients = [Ingredient("яйца", 2, "шт"), Ingredient("соль", 1, "ст.л"),
                   Ingredient("помидоры", 0.5, "шт")]
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



def test_add_recipe():
    ingredients = [Ingredient("яйца", 2, "шт"), Ingredient("соль", 1, "ст.л"),
                   Ingredient("помидоры", 0.5, "шт")]
    recipe = Recipe("яичница", ingredients)

    shoppingList = ShoppingList()

    with pytest.raises(ValueError):
        shoppingList.add_recipe(recipe, 0)
    with pytest.raises(ValueError):
        shoppingList.add_recipe(recipe, -13)


    shoppingList.add_recipe(recipe, 2)
    shoppingList._items[0] = (Ingredient("яйца",4 , "шт"), "recipe")
    shoppingList._items[1] = (Ingredient("соль", 2, "ст.л"), "recipe")
    shoppingList._items[2] = (Ingredient("помидоры", 1, "шт"), "recipe")


def test_remove_recipe():
    recipe_1 = Recipe("яичница", [Ingredient("яйца", 2, "шт"),
                                   Ingredient("соль", 1, "ст.л"),
                                   Ingredient("помидоры", 0.5, "шт")])
    recipe_2 = Recipe("отбивная", [Ingredient("мясо", 500, "г"),
                                   Ingredient("соль", 501, "г")])


    shoppingList = ShoppingList()
    shoppingList.add_recipe(recipe_1, 1)
    shoppingList.add_recipe(recipe_2, 2)


    shoppingList.remove_recipe(recipe_2.title)

    titles = [t for int, t in shoppingList._items]
    assert titles.count("яичница") == 3
    assert titles.count("отбивная") == 0




    shoppingList.remove_recipe("борщ")

def test_get_list():
    recipe_1 = Recipe("яичница", [Ingredient("яйца", 2, "шт"),
                                   Ingredient("соль", 100, "г"),
                                   Ingredient("помидоры", 0.5, "шт")])
    recipe_2 = Recipe("отбивная", [Ingredient("мясо", 500, "г"),
                                   Ingredient("соль", 501, "г")])


    shoppingList = ShoppingList()
    shoppingList.add_recipe(recipe_1, 1)
    shoppingList.add_recipe(recipe_2, 1)

    lst = shoppingList.get_list()
    assert len(lst) == 4
    assert lst[0] == Ingredient("мясо", 500, "г")
    assert lst[1] == Ingredient("помидоры", 0.5, "шт")
    assert lst[2] == Ingredient("соль", 601, "г")  #сумируются
    assert lst[3] == Ingredient("яйца", 2, "шт")

def test_add():
    recipe_1 = Recipe("яичница", [Ingredient("яйца", 2, "шт"),
                                   Ingredient("соль", 100, "г"),
                                   Ingredient("помидоры", 0.5, "шт")])
    recipe_2 = Recipe("отбивная", [Ingredient("мясо", 500, "г"),
                                   Ingredient("соль", 501, "г")])

    shopping_list_1 = ShoppingList()
    shopping_list_1.add_recipe(recipe_1, 1)

    shopping_list_2 = ShoppingList()
    shopping_list_2.add_recipe(recipe_2, 1)


    sum_sl = shopping_list_1 + shopping_list_2
    assert len(shopping_list_1._items) + len(shopping_list_2._items) == len(sum_sl._items)
    assert len(shopping_list_1._items) == 3
    assert len(shopping_list_2._items) == 2

