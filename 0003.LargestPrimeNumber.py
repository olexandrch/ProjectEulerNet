#!/usr/bin/env python3

# https://projecteuler.net/problem=2
# Largest Prime Factor
# Problem 3
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143?

import math
import time

number = 600851475143 # 13195 # 600851475143


# Rounded up Square Root of the number
def sq_root_up(n):
  if n<=0:
    return 0
  return int(math.ceil(math.sqrt(n)))

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

primes = []

for x in range(1, sq_root_up(number)):
  if number % x == 0 and is_prime(x):
    primes.append(x)
    quotient = int(number/x)
    if is_prime(quotient):
      primes.append(quotient)

primes.sort()

end_time = time.time()
execution_time = end_time - start_time
print(f"Method 1. Prime factors of the number {number} are {primes}, Max prime number is {max(primes)}")
print(f"Execution time: {execution_time:.6f} seconds")


# Method 2
start_time = time.time()

primes = []

x=2
if number % x == 0 and is_prime(x):
  primes.append(x)
  quotient = int(number/x)
  if is_prime(quotient):
    primes.append(quotient)


for x in range(1, sq_root_up(number),2):
  if number % x == 0 and is_prime(x):
    primes.append(x)
    quotient = int(number/x)
    if is_prime(quotient):
      primes.append(quotient)

primes.sort()

end_time = time.time()
execution_time = end_time - start_time
print(f"Method 2. Prime factors of the number {number} are {primes}, Max prime number is {max(primes)}")
print(f"Execution time: {execution_time:.6f} seconds")
