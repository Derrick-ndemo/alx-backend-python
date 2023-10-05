#!/usr/bin/env python3
"""
function that takes a list of intagers 
and floats and returns their sum as a float
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """returns sum of list of ints and floats as a float"""
    return float(sum(mxd_lst))
