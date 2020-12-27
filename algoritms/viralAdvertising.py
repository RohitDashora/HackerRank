#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the viralAdvertising function below.
def viralAdvertising(n):
    share=5
    clike=0
    for i in range(n):
        liked=math.floor(share/2)
        share= liked*3
        clike=clike+liked
    return clike