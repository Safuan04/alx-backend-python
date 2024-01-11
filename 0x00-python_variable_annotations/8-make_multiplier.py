#!/usr/bin/env python3
"""Defining make_multiplier function"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """This is a function that takes a float multiplier as argument
        and returns a function that multiplies a float by multiplier."""
    def the_multiplier(x):
        return x * multiplier

    return the_multiplier
