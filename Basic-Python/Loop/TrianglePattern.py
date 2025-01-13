import math
import random
import re
import os
import sys

if __name__ == '__main__':
    n = int(input("Enter number: "))
    
    for i in range (1, n+1):
        for j in range (1, i+1):
            print(i, end=" ")
        print()