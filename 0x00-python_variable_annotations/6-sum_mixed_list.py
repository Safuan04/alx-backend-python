#!/usr/bin/env python3
"""Defining sum_mixed_list function"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """This is a function that takes a list mxd_lst of integers
        and floats and returns their sum as a float."""
    return sum(mxd_lst)
