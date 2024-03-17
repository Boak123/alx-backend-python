#!/usr/bin/env python3
"""Complex types - integers and floats """
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """ Type-annotated function sum_mixed_list that takes a lists of integers and float argument.
        Args:
            input_list: integers and float type.
        Return:
            The sum as a float.
    """
    return sum(mxd_lst)
