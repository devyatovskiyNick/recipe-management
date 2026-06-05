# Recipe Manager
Проект, в котором реализована система управления рецептами и списком для покупок.

- `Ingredient` — хранит информацию об одном Ингредиенте: название, количество и единицу измерения.
- `Recipe` — хранит рецепт блюда: название и набор ингредиентов.
- `DietaryRecipe` — расширяет `Recipe`, добавляя диетическую категорию (веган, без сахара и т.д.)
- `ShoppingList` — список покупок из нескольких рецептов

## Использование
```bash
git clone https://github.com/devyatovskiyNick/recipe-management
cd recipe-management
pip install -r requirements.txt
pytest

# если bash не находит команду pytest
python -m pytest
```


Девятовский Николай Иванович, группа ББИ2510