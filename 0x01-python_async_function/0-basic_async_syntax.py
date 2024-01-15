#!/usr/bin/env python3
"""Defining an async function named wait_random"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """This is a function  that waits for a random delay between
        0 and max_delay seconds and eventually returns it."""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)

    return delay
