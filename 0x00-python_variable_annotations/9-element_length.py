#!/usr/bin/env python3
"""Defining element_length function"""
from typing import List, Tuple, Sequence, Iterable


def element_length(lst: Iterable
                   [Sequence]) -> List[Tuple[Sequence, int]]:
    """This is a function that takes an iterable (lst) containing
        elements of the Sequence type and returns a list of tuples."""
    return ((i, len(i)) for i in lst)
