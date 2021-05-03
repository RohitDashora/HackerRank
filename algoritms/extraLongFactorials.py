#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'extraLongFactorials' function below.
#
# The function accepts INTEGER n as parameter.
#

def extraLongFactorials(n):
    n1=n
    r=1
    while n1 !=0:
       r=r*n1
       n1=n1-1
    print(r)