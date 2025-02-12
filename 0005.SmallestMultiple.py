#!/usr/bin/env python3

# https://projecteuler.net/problem=5
# Smallest Multiple
# Poblem 5
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible (without remainder) by all of the numbers from 1 to 20?

import math
import time

max_divisor = 8 # 10 # 20

# Check if number is divisiable without reminder
def is_reminder(divident, divisor):
  if divident % divisor == 0:
    return False
  else:
    return True

# Check if evenly divisiable by all of the numbers
def is_evenly_divisiable(number_to_check, from_1_to_x):
  for x in range (2, from_1_to_x+1):
    # print (f"from for: x= {x}, number_to_check= {number_to_check}")
    if is_reminder(number_to_check, x):
      # print (f"from if: x= {x}, number_to_check= {number_to_check}")
      return False
  return True

# Check if the number is a prime number
def is_prime(n):
  if n<=0:
    return False
  for x in range(2, n):
    if n % x == 0:
      return False

  return True


# Method 1
start_time = time.time()

n = max_divisor

while True:
  n += 1
  if is_evenly_divisiable(n, max_divisor):
    break


end_time = time.time()
execution_time = end_time - start_time
print(f"Method 1. {n} is smallest number that is evenly divisible by all numbers from 1 to {max_divisor}")
print(f"Execution time: {execution_time:.6f} seconds")

