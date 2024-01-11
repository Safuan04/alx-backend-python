#!/usr/bin/env python3
"""Defining safe_first_element function"""
from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """This is a function that takes a sequence (lst) of any type
    and returns the first element of the sequence."""
    if lst:
        return lst[0]
    else:
        return None
