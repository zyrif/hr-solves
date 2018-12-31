#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the staircase function below.
def staircase(n):
    for j in range(1, n+1):
        string = ""
        for i in range(1, n+1):
            if j >= i:
                string = "#" + string
            else:
                string = " " + string
        print(string)


if __name__ == '__main__':
    n = int(input())

    staircase(n)
