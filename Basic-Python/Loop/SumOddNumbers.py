import math
import random
import re
import os
import sys

if __name__ == '__main__':
    n = int(input("Enter number: "))
    total = 0
    
    for i in range (1, n+1):
        if i % 2 != 0:
            total += i
    print("The sum of odd number is: ", total)