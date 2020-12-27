#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the saveThePrisoner function below.
def saveThePrisoner(n, m, s):
    return (s+m-2)%n+1