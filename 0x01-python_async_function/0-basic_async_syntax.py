#!/usr/bin/env python3
"""
Asynchronous coroutine that takes an integer argument
that waits for a random delay between 0 and max_delay
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    :param: max_delay
    :return: return a randowm delay
    """
    wait_time = random.uniform(0, max_delay)
    await asyncio.sleep(wait_time)
    return wait_time
