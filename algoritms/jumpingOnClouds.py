#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c, k):
    e=100
    i=k%n
    e = e - ((c[i] * 2) + 1)
    print (i,k,e, c[i])
    while i !=0 :
        i = (i + k) % n
        e = e - ((c[i] * 2) + 1)
    return e 
    
    