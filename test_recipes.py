from Ingredient import Ingredient

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

