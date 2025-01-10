import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input("Input Grade: ").strip())
    if 0 <= n <=50:
        print("Fail")
    elif 51 <= n <=75:
            print("Pass")
    else:
        print("Excellent")