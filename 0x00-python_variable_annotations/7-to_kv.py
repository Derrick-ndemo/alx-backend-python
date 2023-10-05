#!/usr/bin/env python3
"""
function that takes a string k and an int OR float v as arguments
returns a tuple
"""


def to_kv(k: str, v: int | float) -> tuple:
    """
    function that takes a string k and an int OR float v as arguments
    returns a tuple
    """
    return (k, v**2)
