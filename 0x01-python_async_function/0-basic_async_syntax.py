#!/usr/bin/env python3
"""Defining an async function named wait_random"""
import asyncio, random


async def wait_random(max_delay = 10):
    """This is a function  that waits for a random delay between
        0 and max_delay seconds and eventually returns it."""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)

    return delay
