#!/usr/bin/python

import sys

skip = 0
curr = 0

rope = list(range(256))
line = sys.stdin.readline().strip()
lengths = map(int, line.split(','))

for length in lengths:

  rev = []
  for l in range(length-1,0,-1):
    pos = (curr+l)%256
    rev.append(rope[pos])

  for i, r in enumerate(rev):
    c = (curr+i)%256
    rope[c] = r
  curr += length + skip
  skip += 1

print(rope[0]*rope[1])
