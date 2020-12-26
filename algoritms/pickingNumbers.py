#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def pickingNumbers(a):
    d=[]
    for i in a :
        d1 = (a.count(i)+ a.count(i-1))
        d.append(d1)
    return max(d)