import math
import os
import random
import re
import sys

if __name__ == '__main__':
    price = int(input("Input price (ex. 12500): "))
    discount = int(input("Input discount percentage (ex. 10): "))
    
    discount_value = price * (discount / 100)
    final_price = price - discount_value
    
    print("Discount get: ", discount_value)
    print("Final price: ", final_price)