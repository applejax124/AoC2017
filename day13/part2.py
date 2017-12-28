#!/usr/bin/python

import sys

layers = []

for line in sys.stdin:
  d, r = line.strip().split()
  d = int(d.strip(':'))
  r = int(r)
  cycle = r*2 - 2
  layers.append([cycle, d])

  notcaught = False
  start = -1
  while not notcaught:
    notcaught = True
    start += 1

    for scan in layers:
      depth = scan[1] + start
      cycle = scan[0]
      if depth%cycle == 0:
        notcaught = False

print(start)
