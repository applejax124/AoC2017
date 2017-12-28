#!/usr/bin/python

import sys

skip = 0
curr = 0

rope = list(range(256))
line = sys.stdin.readline().strip()
lengths = []
for l in line:
  lengths.append(ord(l))
for i in [17,31,73,47,23]:
  lengths.append(i)

for _ in range(64):
  for length in lengths:
    rev = []
    for l in range(length-1,-1,-1):
      pos = (curr+l)%256
      rev.append(rope[pos])
    for i, r in enumerate(rev):
      c = (curr+i)%256
      rope[c] = r
    curr += length + skip
    skip += 1

print(rope)
  
elements = []
for i in range(16):
  for j in range(16):
    curr = rope[(i*16)+j]
    if j == 0:
      e = curr
    else:
      e = e ^ curr
  elements.append(e)

hasht = ''

print(elements)
for e in elements:
  hasht += format(e, '02x')

print(hasht)
