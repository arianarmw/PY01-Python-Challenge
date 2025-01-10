import math
import os
import random
import re
import sys

if __name__ == '__main__':
    side_of_cube = int(input("Input side of cube: "))
    
    surface_of_cube = 6 * (side_of_cube**2)
    volume_of_cube = side_of_cube**3
    
    print("Surface area of cube: ", surface_of_cube)
    print("Volume of cube: ", volume_of_cube)