#!/usr/bin/python

import sys

summ = 0
for line in sys.stdin:
  try:
    line = list(map(float, line.strip().split()))
  except:
    pass
  for h, i in enumerate(line):
    for k, j in enumerate(line):
      if h != k:
        if i%j == 0:
          summ += i/j
          break
print(summ)
