#!/usr/bin/env python3

# https://projecteuler.net/problem=1
# Multiples of 3 or 5
# Problem 1
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

import time

# Method 1
start_time = time.time()
max = 1000000
total = 0

for x in range(0, max, 1):
    if (x % 3 == 0) or (x % 5 == 0):
        total += x

end_time = time.time()
execution_time = end_time - start_time
print(f"Method 1 Total: {total}, Execution time: {execution_time:.6f} seconds")

# Method 2
start_time = time.time()
total = 0

for x in range(0, max, 3):
  total += x
#  print("x=", x, "total = ", total)

for x in range(0, max, 5):
  if (x % 3 == 0):
    continue
  total += x
#  print("x=", x, "total = ", total)

end_time = time.time()
execution_time = end_time - start_time
print(f"Method 2 Total: {total}, Execution time: {execution_time:.6f} seconds")

# Method 3 - List comprehention
start_time = time.time()
total = 0

total = sum([x for x in range(max) if (x % 3 == 0 or x % 5 == 0)])

end_time = time.time()
execution_time = end_time - start_time
print(f"Method 3 Total: {total}, Execution time: {execution_time:.6f} seconds")
