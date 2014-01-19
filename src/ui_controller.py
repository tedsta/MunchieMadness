#!/usr/bin/env python

from src.chef import *

class UIController:

    # Initialization creates a Chef object to which all commands will be passed
    def __init__(self):
        self.chef = Chef()

    # Returns a list of all Ingredients that MunchieMadness knows about
    def get_all_ingredients(self):
        return self.chef.get_all_ingredients()

    # Indicates that user actually has a given Ingredient
    def add_to_inventory(self, ingredient):
        self.chef.add_to_inventory(ingredient)

    # Oops, user doesn't actually have any of that Ingredient
    def remove_from_inventory(self, ingredient):
        self.chef.remove_from_inventory(ingredient)

    # Start fresh
    def clear_inventory(self):
        self.chef.clear_inventory()

    # Returns address of image corresponding to an Ingredient
    def get_image(self, ingredient):
        return self.chef.get_image(ingredient)

    # This is where the magic happens. Returns a Recipe, which has:
        # title, a string like "Peanut Butter Chocoloate Chip Popcorn Sandwich"
        # ingredients, a list of strings like ['Bread', 'Peanut Butter', 'Chocolate Chips', 'Popcorn']
        # instructions, a list of strings like ['Spread peanut butter on one or both slices of bread', 'Sprinkle with Chocolate Chips', ...]
        # TODO some sort of weirdness score?
    def generate_recipe(self):
        return self.chef.generate_recipe()

