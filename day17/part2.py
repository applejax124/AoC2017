#!/usr/bin/python

import sys

c_buffer = [0]
steps = 349

index = 0
n = 0
length = len(c_buffer)
for num in range(1, 50000000):
  index += steps 
  index %= length
  index += 1
  if index == 1:
    n = num
  length += 1

print(n)
