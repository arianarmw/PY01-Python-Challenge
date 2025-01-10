import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input("Input your number: ").strip())
    if n % 2 != 0:
        print("Odd")
    elif 2 <= n < 10:
        print("Small Even")
    else:
        print("Large Even")