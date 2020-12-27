import math
import os
import random
import re
import sys

# Complete the hurdleRace function below.
def hurdleRace(k, height):
    maxpotient=0
    for hurdle in height :
        if k > hurdle : 
            continue
        elif maxpotient < (hurdle-k):
            maxpotient = hurdle-k
             
        
    print (maxpotient)
    return maxpotient