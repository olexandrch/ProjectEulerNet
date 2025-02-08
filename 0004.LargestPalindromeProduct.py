#!/usr/bin/env python3

# https://projecteuler.net/problem=4
# Largest Palindrome Product
#Problem 4
# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009=91*99.
# Find the largest palindrome made from the product of two 3-digit numbers.

import math
import time

# How Many digits should be in the multipliers
n_digit = 4

max_number = int("9" * n_digit)
min_number = int("9" * (n_digit - 1))+1

# Check if the number is a polindrome
def is_polindrome(n):
  str_n=str(n)
  reverse_str=str_n[::-1]
  if str_n == reverse_str:
    return True
  else:
    return False


# Method 1
start_time = time.time()

xx = 0
yy = 0
nn = 0

for x in range(max_number, min_number, -1):
  for y in range(max_number, min_number, -1):
    n = x * y
    if is_polindrome(n):
      if n > nn:
        xx=x
        yy=y
        nn=n

end_time = time.time()
execution_time = end_time - start_time
print(f"Method 1. Max polindrome made from the product of two {n_digit}-digits {xx} and {yy}  is  {nn}")
print(f"Execution time: {execution_time:.6f} seconds")


# Method 2
start_time = time.time()

xx = 0
yy = 0
nn = 0

for x in range(max_number, min_number, -1):
  for y in range(x, min_number, -1):
    n = x * y
    if is_polindrome(n):
      if n > nn:
        xx=x
        yy=y
        nn=n
        break

end_time = time.time()
execution_time = end_time - start_time
print(f"Method 2. Max polindrome made from the product of two {n_digit}-digits {xx} and {yy}  is  {nn}")
print(f"Execution time: {execution_time:.6f} seconds")





# % ./0004.LargestPalindromeProduct.py
# Method 1. Max polindrome made from the product of two 2-digits 99 and 91  is  9009
# Execution time: 0.002326 seconds
# Method 2. Max polindrome made from the product of two 2-digits 99 and 91  is  9009
# Execution time: 0.001173 seconds

# % ./0004.LargestPalindromeProduct.py
# Method 1. Max polindrome made from the product of two 3-digits 993 and 913  is  906609
# Execution time: 0.245079 seconds
# Method 2. Max polindrome made from the product of two 3-digits 993 and 913  is  906609
# Execution time: 0.122079 seconds

# % ./0004.LargestPalindromeProduct.py
# Method 1. Max polindrome made from the product of two 4-digits 9999 and 9901  is  99000099
# Execution time: 23.339082 seconds
# Method 2. Max polindrome made from the product of two 4-digits 9999 and 9901  is  99000099
# Execution time: 11.492347 seconds