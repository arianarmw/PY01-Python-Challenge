import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input("Input temperature: ").strip())
    
    if n < 0 :
        print("Freezing")
    elif 0 <= n <= 20:
        print("Cold")
    elif 21 <= n <= 35:
        print("Warm")
    else:
        print("Hot")