#!/usr/bin/env python

from collections import namedtuple

# TODO put namedtuple declaration in a utility module or something?        
Recipe = namedtuple('Recipe', ['title', 'ingredients', 'instructions', 'score'])


class Chef:

    def __init__(self, ingredient_manager, inventory = None):
        self.ing_mgr = ingredient_manager
        if inventory == None:
            self.inventory = []
        else:
            self.inventory = inventory

    # Returns a list of all Ingredients that MunchieMadness knows about
    def get_all_ingredients(self):
        return self.ing_mgr.get_all_ingredients()

    # Indicates that user actually has a given Ingredient
    def add_to_inventory(self, ingredient):
        if ingredient not in self.inventory and self.ing_mgr.verify_ingredient(ingredient):
            self.inventory.append(ingredient)

    # Oops, user doesn't actually have any of that Ingredient
    def remove_from_inventory(self, ingredient):
        if ingredient in self.inventory:
            self.inventory.remove(ingredient)

    # Start fresh
    def clear_inventory(self):
        del self.inventory[:]

    # Returns address of image corresponding to an Ingredient
    def get_image(self, ingredient):
        return self.ing_mgr.get_image(ingredient)

    def generate_recipe(self, max_score):
        ingreds = ['Bread', 'Butter', 'Ham', 'Cheese', 'Popcorn']
        instructs = ['Slice cheese', 'Pop popcorn', 'Put Ham, Cheese and Popcorn between slices of Bread', 'Spread Butter on outside of Bread', 'Grill over medium low heat, turning once', 'Cut in half and enjoy']
        score = 3
        hardcoded_result = Recipe(title='Grilled Ham, Cheese and Popcorn Sandwich', ingredients=ingreds, instructions=instructs, score=score)
        return hardcoded_result

