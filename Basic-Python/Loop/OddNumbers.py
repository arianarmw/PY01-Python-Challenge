import math
import random
import os
import re
import sys

if __name__ == '__main__':
    n = int(input("Enter number: "))
    
    for i in range(1, n+1):
        if i % 2 != 0:
            print(i)