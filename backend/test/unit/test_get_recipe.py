import pytest
import unittest.mock as mock
from src.controllers.recipecontroller import RecipeController
from src.static.diets import Diet


rec =    {
        "name": "Banana Bread",
        "diets": [
            "normal", "vegetarian"
        ],
        "ingredients": {
            "Butter": 100,
            "Banana": 4,
            "Sugar": 200,
            "Egg": 1,
            "Vanilla Sugar": 1,
            "Baking Powder": 0.5,
            "Salt": 5,
            "Cinnamon": 10,
            "Flour": 220,
            "Walnuts": 10
        }
    }

items = {
            "Butter": 100,
            "Banana": 4,
            "Sugar": 200,
            "Egg": 1,
            "Vanilla Sugar": 1,
            "Baking Powder": 0.5,
            "Salt": 5,
            "Cinnamon": 10,
            "Flour": 220,
            "Walnuts": 10
        
    }

diet_ = Diet.VEGETARIAN

recipe_1 = {
    "name": "Banana Bread",
    "diets": [
        "normal", "vegetarian"
    ],
    "ingredients": {
        "Butter": 100,
        "Banana": 4,
        "Sugar": 200,
        "Egg": 1,
        "Vanilla Sugar": 1,
        "Baking Powder": 0.5,
        "Salt": 5,
        "Cinnamon": 10,
        "Flour": 220,
        "Walnuts": 10
    }
}

@pytest.fixture
def sut(recipe, available_items, diet):
    mockeddao = mock.MagicMock()

    # calculate_readiness replace the function/class being mocked in the function currently under test
    # .return_value gives the returned valued from the mocked function
    mockeddao.get_recipe_readiness.return_value = (recipe, available_items, diet)
    mockedsut = RecipeController(dao=mockeddao)
    return mockedsut

@pytest.mark.unit
# @pytest.mark.parametrize('recipe, available_items, diet, best, outcome',[(rec, {"Butter": 100, "Banana" : 4}, diet_, None), ({"name": "Banana bread", "diets":["normal", "vegetarian"], "":0 }, items, Diet.VEGAN, None),  ({"name": "Banana bread", "diets":["normal", "vegetarian"], "ingredients": {"Butter" : 100, "Flour" : 2} }, {"Butter" : 100, "Flour" : 2}  , Diet.VEGETARIAN, 1) ] )
@pytest.mark.parametrize('recipe, items, diet, best, outcome', [rec, items, diet_, True, recipe_1])
def test_get_recipe(sut, recipe, items, diet, best ,outcome):
    selected_recipe = sut.get_recipe(diet,best, recipe, items)
    assert selected_recipe == outcome