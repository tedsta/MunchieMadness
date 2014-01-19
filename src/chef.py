#!/usr/bin/env python

class Chef:

    # Returns a list of all Ingredients that MunchieMadness knows about
    def get_all_ingredients(self):
        pass

    # Indicates that user actually has a given Ingredient
    def add_to_inventoary(self, Ingredient):
        pass

    # Oops, user doesn't actually have any of that Ingredient
    def remove_from_inventory(self, ingredient):
        pass

    # Start fresh
    def clear_inventory(self):
        pass

    # Returns address of image corresponding to an Ingredient
    def get_image(self, Ingredient):
        pass

    # This is where the magic happens. Returns a Recipe, which has:
        # title, a string like "Peanut Butter Chocoloate Chip Popcorn Sandwich"
        # ingredients, a list of strings like ['Bread', 'Peanut Butter', 'Chocolate Chips', 'Popcorn']
        # instructions, a list of strings like ['Spread peanut butter on one or both slices of bread', 'Sprinkle with Chocolate Chips', ...]
        # TODO some sort of weirdness score?
    def generate_recipe(self):
        pass

