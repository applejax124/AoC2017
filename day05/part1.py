#!/usr/bin/python

import sys, itertools, math

instructions = []

for line in sys.stdin:
  instructions.append(int(line.strip()))

i = 0
steps = 0
while i < len(instructions):
  j = i
  i += instructions[i]
  instructions[j] += 1
  steps += 1

print(steps)
