#!/usr/bin/env python

import unittest
from src.ui_controller import *
from mock import Mock


class TestUIController(unittest.TestCase):

    def setUp(self):
        self.ui = UIController()

    def test_constructor(self):
        self.assertEquals('UIController', self.ui.__class__.__name__)
        self.assertTrue(isinstance(self.ui.chef, Chef))

    def test_get_all_ingredients(self):
        self.ui.chef = Mock()
        result = self.ui.get_all_ingredients()
        self.ui.chef.get_all_ingredients.assert_called_with()

    def test_add_to_inventory(self):
        self.ui.chef = Mock()
        self.ui.add_to_inventory('Butter')
        self.ui.chef.add_to_inventory.assert_called_with('Butter')

    def test_remove_from_inventory(self):
        self.ui.chef = Mock()
        self.ui.remove_from_inventory('Spam')
        self.ui.chef.remove_from_inventory.assert_called_with('Spam')

    def test_clear_inventory(self):
        self.ui.chef = Mock()
        self.ui.clear_inventory()
        self.ui.chef.clear_inventory.assert_called_with()

    def test_get_image(self):
        self.ui.chef = Mock()
        img_path = self.ui.get_image('Popcorn')
        self.ui.chef.get_image.assert_called_with('Popcorn')
        
    def test_generate_recipe(self):
        self.ui.chef = Mock()
        self.ui.generate_recipe(5)
        self.ui.chef.generate_recipe.assert_called_with(5)


##########################
def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestUIController))
    return suite

if __name__ == '__main__':
    unittest.main()
