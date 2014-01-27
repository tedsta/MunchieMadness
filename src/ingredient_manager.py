#!/usr/bin/env python

class IngredientManager:

    ALL_INGREDIENTS = ['Bread', 'Butter', 'Ham', 'Cheese', 'Popcorn']

    # Returns a list of all Ingredients that MunchieMadness knows about
    def get_all_ingredients(self):
        return self.ALL_INGREDIENTS

    def verify_ingredient(self, ingredient):
        return ingredient in self.ALL_INGREDIENTS

    # Returns address of image corresponding to an Ingredient
    def get_image(self, Ingredient):
        pass

