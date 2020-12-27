#!/bin/python3

import math
import os
import random
import re
import sys
from collections import OrderedDict
from itertools import repeat
#
# Complete the 'climbingLeaderboard' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY ranked
#  2. INTEGER_ARRAY player
#
def BinSearchInsert(array, element, lastIndex):
    #array is reverse sorted
    maxI=0 
    minI=lastIndex
    midI=math.floor((minI-maxI)/2)
    while True:
        if element == array[maxI] : 
            out =maxI
            break
        if element == array[minI] : 
            out =minI
            break
        if element == array[midI] : 
            out =midI
            break
        if element > array[maxI] :
            out=maxI
            break
        if element < array[minI] : 
            out=minI+1
            break
        if element < array[midI] :
            if abs(minI - midI) == 1 : 
                out=minI
                break
            else :
                maxI=midI
                midI=math.floor((minI+maxI)/2)
                continue
        if element > array[midI] :
            if abs(maxI - midI) ==1 :
                out=midI
                break
            else: 
                minI=midI
                midI= math.floor((minI-maxI)/2)
    return out
        

def climbingLeaderboard(ranked, player):
    ranked1= list(OrderedDict(zip(ranked, repeat(None))))
    rank=[]
    index=len(ranked1)-1
    index0=len(ranked1)-1
    for score in player :
        index=BinSearchInsert(ranked1, score, min(index,index0))                  
        rank.append(index+1)
    return rank

