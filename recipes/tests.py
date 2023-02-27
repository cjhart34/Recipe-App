from django.test import TestCase
from .models import Recipe

# Create your tests here.


class RecipeModelTest(TestCase):

    def setUpTestData():
        Recipe.objects.create(name='Tea', cooking_time=5, ingredients='tea-leaves, water, sugar',
                              description='Add tea leaves to boiling water, then add sugar')

    def test_desciption(self):
        recipe = Recipe.objects.get(id=1)
        name_max_length = recipe._meta.get_field('name').max_length
        self.assertEqual(name_max_length, 120)

    def test_recipe_name(self):
        recipe = Recipe.objects.get(id=1)
        recipe_name_label = recipe._meta.get_field('name').verbose_name
        self.assertEqual(recipe_name_label, 'name')

    def test_cookingtime_helptext(self):
        recipe = Recipe.objects.get(id=1)
        recipe_cookingtime = recipe._meta.get_field('cooking_time').help_text
        self.assertEqual(recipe_cookingtime, 'In minutes')
