#!/usr/bin/env python3
""" Complex type - list of floats """
from typing import list


def sum_list(input_list: List[float]) -> float:
     """ Type-annotated function sum_list that takes a float argument.
        Args:
            input_list: float type.
        Return:
            The sum as a float.
    """
    return sum(input_list)
