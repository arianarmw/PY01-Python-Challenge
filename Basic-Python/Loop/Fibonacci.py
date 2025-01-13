import math
import random
import os
import re
import sys

if __name__ == '__main__':
    n = int(input("Enter number: "))
    a, b = 0, 1
    
    for i in range (n):
        print(a, end= " ")
        a, b = b, a+b