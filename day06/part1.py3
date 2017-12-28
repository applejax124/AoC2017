#!/usr/bin/python

import sys, math, itertools

blocks = list(map(int, sys.stdin.readline().strip().split())) 
seen = {}

i = 0

while True:

#  same = False
#  if len(seen) > 1:
#    same = True
#    for s in seen:
#      for r in seen:
#        if r!=s:
#          for x in range(len(blocks)):
#            if seen[s][x] != seen[r][x]:
#              same = False
#              break
#        if not same:
#          break
#      if not same:
#        break

#  if same:
#    break

  if i == 0:
    seen[0] = []
    for b in blocks:
      seen[0].append(b)
    i += 1
    continue

  max_b = 0
  for j, b in enumerate(blocks):
    if b > max_b:
      max_b = b
      max_j = j

  blocks[max_j] = 0

  while max_b > 0:
    max_j += 1
    blocks[max_j%len(blocks)] += 1
    max_b -= 1

  if blocks in seen.values():
    break
  else:
    seen[i] = []
    for r in blocks:
      seen[i].append(r)
    i += 1

print(i)
