import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input("Input your age: ").strip())
    if n < 13:
        print("Child")
    elif 13 <= n <=19:
        print("Teenager")
    elif 20 <= n <=64:
        print("Adult")
    else:
        print("Senior")