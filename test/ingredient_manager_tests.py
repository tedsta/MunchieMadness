#!/usr/bin/env python

import unittest
from src.ingredient_manager import *


class TestIngredientManager(unittest.TestCase):

    def setUp(self):
        self.mgr = IngredientManager()

    def test_constructor(self):
        self.assertEquals('IngredientManager', self.mgr.__class__.__name__)

    def test_get_all_ingredients(self):
        ingredients = self.mgr.get_all_ingredients()
        self.assertTrue(ingredients)
        self.assertTrue('Bread' in ingredients)

    def test_verify_ingredient(self):
        self.assertTrue(self.mgr.verify_ingredient('Cheese'))

        


##########################
def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestIngredientManager))
    return suite

if __name__ == '__main__':
    unittest.main()
