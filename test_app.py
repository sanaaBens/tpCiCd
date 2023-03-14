""" Module for importing """
from unittest import TestCase
from app import addition,soustraction,multiplication


class TestApp(TestCase):
    """ class representing the test """
    # test de l'addition
    def test_sum_true(self):
        """ function testing addition if it's true """
        self.assertEqual(addition(1, 2), 3)

    def test_sum_wrong(self):
        """ function testing addition if it's wrong """
        self.assertNotEqual(addition(1, 2), 4)
        # test de la soustraction
    def test_minus_true(self):
        """ function testing  soustraction if it's true """
        self.assertEqual(soustraction(2, 1), 1)

    def test_minus_wrong(self):
        """ function testing  soustraction if it's wrong """
        self.assertNotEqual(soustraction(2, 1), 2)
        # test de la multiplication
    def test_multiply_true(self):
        """ function testing  multiplication if it's true """
        self.assertEqual(multiplication(2, 2), 4)

    def test_multiply_wrong(self):
        """ function testing  multiplication if it's wrong """
        self.assertNotEqual(multiplication(2, 2), 5)# \r\nEOF
