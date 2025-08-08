#!/usr/bin/env python3
"""
Type-annotated function that returns a tuple with a string and squared number.
"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Create a tuple with a string and the square of a number.

    Args:
        k (str): The string key
        v (Union[int, float]): The number to square

    Returns:
        Tuple[str, float]: Tuple containing the string and squared number
    """
    return (k, v ** 2)
