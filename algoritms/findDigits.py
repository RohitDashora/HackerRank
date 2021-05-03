#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'findDigits' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def findDigits(n):
    r=0
    n1=n
    while n1 >=1 :
        k=n1%10
        n1=int(n1/10)
        if k!= 0 :
            if n%k == 0 : 
                r =r+1
        print(n1,k,r)
    return r
