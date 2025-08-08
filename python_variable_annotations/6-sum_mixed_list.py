#!/usr/bin/env python3
"""
Type-annotated function that sums a mixed list of integers and floats.
"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Sum all numbers in a mixed list of integers and floats.

    Args:
        mxd_lst (List[Union[int, float]]): List of integers and floats to sum

    Returns:
        float: Sum of all numbers in the list
    """
    return sum(mxd_lst)
