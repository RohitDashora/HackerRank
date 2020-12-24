#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    k = s[-2:]
    p = s[:2]
    if k == "PM" :
        if int(p) < 12 :
            p= str(int(p)+12)
    elif k == "AM" :
        if p == "12" :
            p = "00"
    s2 = p + s[2:8]
    return (s2)
        #
    # Write your code here.
    #

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
