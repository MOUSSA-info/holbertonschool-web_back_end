#!/usr/bin/env python3
"""
Type-annotated function that returns a list of tuples with sequences and
their lengths.
"""

from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Create a list of tuples containing sequences and their lengths.

    Args:
        lst (Iterable[Sequence]): An iterable of sequences

    Returns:
        List[Tuple[Sequence, int]]: List of tuples with sequences and
        their lengths
    """
    return [(i, len(i)) for i in lst]
