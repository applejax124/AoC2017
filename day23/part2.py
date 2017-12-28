#!/usr/bin/python

import math

h=0
b = 57*100 + 100000
c = b + 17000

while b <= c:

  x = int(math.sqrt(b))

  prime = True

  for i in range(2, x):
    if b % i == 0:
      prime = False 
      break

  if not prime:
    h += 1

  b += 17

print(h)
