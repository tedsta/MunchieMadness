#!/usr/bin/env python

import unittest
from unittest.mock import Mock
from src.chef import *


class TestChef(unittest.TestCase):

    def setUp(self):
        self.ing_mgr = Mock()
        self.chef = Chef(self.ing_mgr)

    def test_constructor(self):
        self.assertEquals('Chef', self.chef.__class__.__name__)
        self.assertTrue(self.chef.ing_mgr)

    def test_get_all_ingredients(self):
        ingredients = self.chef.get_all_ingredients()
        self.ing_mgr.get_all_ingredients.assert_called_with()

    def test_add_to_inventory(self):
        self.assertEqual(0, len(self.chef.inventory))
        self.chef.add_to_inventory('Butter')
        self.assertEqual(1, len(self.chef.inventory))

    def test_add_to_inventory_bogus_ingredient(self):
        self.ing_mgr.verify_ingredient.return_value = False
        self.assertEqual(0, len(self.chef.inventory))
        self.chef.add_to_inventory('Cat meat')
        self.assertEqual(0, len(self.chef.inventory))

    def test_remove_from_inventory(self):
        self.chef.add_to_inventory('Cheese')
        self.assertEqual(1, len(self.chef.inventory))
        self.chef.remove_from_inventory('Cheese')
        self.assertEqual(0, len(self.chef.inventory))

    def test_clear_inventory(self):
        self.chef.add_to_inventory('Popcorn')
        self.chef.add_to_inventory('Ham')
        self.assertEqual(2, len(self.chef.inventory))
        self.chef.clear_inventory()
        self.assertEqual(0, len(self.chef.inventory))

    def test_get_image(self):
        #TODO
        pass
        
    def test_generate_recipe(self):
        # this tests the hardcoded method. a proper test would add ingredients before calling the method and assert that a Recipe is returned...
        recipe = self.chef.generate_recipe()
        self.assertTrue(recipe)
        self.assertTrue(recipe.title)
        self.assertTrue('Popcorn' in recipe.ingredients) 
        self.assertTrue(recipe.instructions)


##########################
def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestChef))
    return suite

if __name__ == '__main__':
    unittest.main()
