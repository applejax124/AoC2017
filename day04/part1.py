#!/usr/bin/python

from collections import Counter
import sys, itertools

num = 0

for line in sys.stdin:
  is_valid = True
  phrase = line.strip().split()

  print(phrase)  

  for k, p in enumerate(phrase):
    for j, s in enumerate(phrase):
      if j != k:
        if Counter(s) == Counter(p):
          is_valid = False

#
#
#    it = itertools.permutations(ph)
#
#
#
#
#
#    for j, sh in enumerate(phrase):
#      s = "".join(sh)
#      for ih in list(it):
#        i = "".join(ih)
#        if j != k and s == i:
#          is_valid = False
#
  if is_valid:
    num += 1

print(num-1)
