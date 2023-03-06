import pytest
from app import * 
from unittest import TestCase


class TestApp(TestCase):
    def test_addition_true(self):
        self.assertEqual(addition(1, 2), 3)

    def test_addition_wrong(self):
        self.assertNotEqual(addition(1, 2), 4)

    def test_soustraction_true(self):
        self.assertEqual(soustraction(2, 1), 1)

    def test_soustraction_wrong(self):
        self.assertNotEqual(soustraction(2, 1), 2)

    def test_multiplication_true(self):
        self.assertEqual(multiplication(2, 2), 4)

    def test_multiplication_wrong(self):
        self.assertNotEqual(multiplication(2, 2), 5)