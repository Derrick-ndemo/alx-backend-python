#!/usr/bin/env python3
"""
task 1: async comprehension
"""
import asyncio
import random
from typing import Generator, List
from importlib import import_module as using


async_generator = using("0-async_generator").async_generator


async def async_comprehension() -> List[float]:
    """
    coroutine that will collect 10 random numbers using an async comprehensing
    over async_generator, then return the 10 random numbers.
    """
    return [i async for i in async_generator()]
