#!/usr/bin/env python

import unittest
from src.chef import *


class TestChef(unittest.TestCase):

    def setUp(self):
        self.chef = Chef()

    def test_constructor(self):
        self.assertEquals('Chef', self.chef.__class__.__name__)

        


##########################
def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestChef))
    return suite

if __name__ == '__main__':
    unittest.main()
