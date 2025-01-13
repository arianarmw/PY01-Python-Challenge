import math
import random
import re
import os
import sys

if __name__ == '__main__':
    n = int(input("Enter number: "))
    sum = 0
    
    for i in range (n):
        sum += i**2
    
    print(f'The sum of squares is: {sum}')