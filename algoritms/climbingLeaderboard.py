#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'climbingLeaderboard' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY ranked
#  2. INTEGER_ARRAY player
#


def BinSearchInsert(array, element):
    #array is reverse sorted
    maxI=0 
    minI=len(array)-1
    midI=math.floor(len(array)/2)
    
    while True:
        print( element, maxI, midI, minI)
        if element > array[maxI] :
            #array.insert(maxI, element)
            out=maxI
            break
        if element < array[minI] : 
            #array.insert(minI+1, element)
            out=minI+1
            break
        if element < array[midI] :
            if abs(minI - midI) == 1 : 
                #array.insert(minI, element)
                out=minI
                break
            else :
                maxI=midI
                midI=math.floor((minI+maxI)/2)
                continue
        if element > array[midI] :
            if abs(maxI - midI) ==1 :
                #array.insert(midI, element)
                out=midI
                break
            else: 
                minI=midI
                midI= math.floor((minI-maxI)/2)
    print(out)
    return out
        

def climbingLeaderboard(ranked, player):
    ranked=list(dict.fromkeys(ranked)) 
    ranked.sort(reverse=True)
    rank=[]
    for score in player :
        r1=ranked  
        if score not in r1 :                      
            index=BinSearchInsert(r1, score)
        else : index = r1.index(score)
        rank.append(index+1)
    return rank



