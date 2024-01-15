#!/usr/bin/env python3
"""Defining a function task_wait_n"""
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """This is a function that should
        return the list of all the delays (float values)."""
    delays_list = [task_wait_random(max_delay) for _ in range(n)]
    batch = await asyncio.gather(*delays_list)
    sorted_result = sorted(batch)
    return sorted_result
