import math
import os
import random
import re
import sys

# Complete the designerPdfViewer function below.
def designerPdfViewer(h, word):
    width=len(word)
    maxlen=0
    for letter in word:
        if maxlen < h[(ord(letter)-96)-1] :
            maxlen =h[(ord(letter)-96)-1] 
    return maxlen * width