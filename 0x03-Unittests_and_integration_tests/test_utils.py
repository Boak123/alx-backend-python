#!/usr/bin/env python3
""" Parameterize a unit test """

import unittest
from unittest.mock import patch
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
    def test_access_nested_map(self, nested_map, path, answer):
        """ Call the access_nested_map 
        function with the input data """

        result = access_nested_map(nested_map, path)

        """ Assert that the result matches the expected output """
        self.assertEqual(access_nested_map(nested_map, path), answer)
    
    if __name__ == '__main__':
        unittest.main()

