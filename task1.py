#!/usr/bin/python3
import sys

def is_prime(n):
  if n <= 1:
    return False
  for i in range(2, n):
    if n % i == 0:
      return False
  return True

def first_prime_fact(n):
  for i in range(2, n + 1):
    if is_prime(i) and n % i == 0:
      return i

def do_it(n):
  m = first_prime_fact(n)
  return str(n) + "=" + str(n // m) + "*" + str(m)

file = open(sys.argv[1])
L = file.readlines()
for x in L[:-1]:
  s = do_it(int(x))
  print(s)