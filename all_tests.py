#!/usr/bin/env python

# import all the lovely files
import unittest
import test.ui_controller_tests
import test.chef_tests
import test.ingredient_manager_tests

# get suites from test modules
suite1 = test.ui_controller_tests.suite()
suite2 = test.chef_tests.suite()
suite3 = test.ingredient_manager_tests.suite()

# collect suites in a TestSuite object
suite = unittest.TestSuite()
suite.addTest(suite1)
suite.addTest(suite2)
suite.addTest(suite3)

# run suite
unittest.TextTestRunner(verbosity=2).run(suite)
