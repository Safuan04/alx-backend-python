#!/usr/bin/env python3
"""Defining an async function named wait_n"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """This is a function that should
        return the list of all the delays (float values)."""
    delays_list = [(wait_random(max_delay)) for _ in range(n)]
    batch = await asyncio.gather(*delays_list)
    sorted_result = sorted(batch)
    return sorted_result
