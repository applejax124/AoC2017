#!/usr/bin/python

import sys

summ = 0
for line in sys.stdin:
  try:
    line = list(map(int, line.strip().split()))
    summ += max(line) - min(line)
  except:
    pass
print(summ)
