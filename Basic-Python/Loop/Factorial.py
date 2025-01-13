import math
import random
import re
import os
import sys

if __name__ == '__main__':
    n = int(input("Enter number: "))
    factorial = 1
    
    for i in range(1, n+1):
        factorial *= i
    
    print(f'The result of {n}! = {factorial}')