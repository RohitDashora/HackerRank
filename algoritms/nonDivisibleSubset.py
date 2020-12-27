#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'nonDivisibleSubset' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY s
#

def nonDivisibleSubset(k, s):
    # Write your code here
    counts = [0] * k
    for number in s:
        counts[number % k] += 1
    count = min(counts[0], 1)
    for i in range(1, k//2+1):
        if i != k - i:
            count += max(counts[i], counts[k-i])
    if k % 2 == 0: 
        count += 1
    return count