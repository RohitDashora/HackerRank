#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the utopianTree function below.
def utopianTree(n):
    y=0
    if n==0 : return 1
    for i in range(n+1):
        if i==0 : y=1 
        elif i%2 !=0 : y=y*2
        else : y=y+1
    return y