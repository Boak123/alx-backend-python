#!/usr/bin/env python3
""" Parameterize a unit test """

import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize



class TestAccessNestedMap(unittest.TestCase):
    """ a class that testednestedmap that inherits
    from unittest.testcase
    """


    @parameterized.expand([
        nested_map={"a": 1}, path=("a",)
        nested_map={"a": {"b": 2}}, path=("a",)
        nested_map={"a": {"b": 2}}, path=("a", "b")])
    def test_access_nested_map(self, nested_map, path, expected):
         """Tests `access_nested_map`'s output."""
         self.assertEqual(access_nested_map(nested_map, path), expected)
