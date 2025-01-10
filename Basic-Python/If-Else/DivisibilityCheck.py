import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input("Input your number: ").strip())
    if n % 3 == 0 and n % 5 == 0:
        print("Divisible by 3 and 5")
    elif n % 3 == 0:
        print("Divisible by 3")
    elif n % 5 == 0:
        print("Divisible by 5")
    else:
        print("Not Divisible")