#!/usr/bin/python

import sys

stream = sys.stdin.readline().strip()

level = 0
summ = 0
garbage = False
cancelled = False
tracker = []

for s in stream:

  if not cancelled:

    if s == '!':
      cancelled = True

    if s == '<':
      garbage = True

    if not garbage:
      if s == '{':
        tracker.append(s)
        level += 1
      if s == '}':
        tracker.pop()
        summ += level
        level -= 1

    else:
      if s == '>':
        garbage = False

  else:
    cancelled = False

print(summ)
