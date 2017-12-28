#!/usr/bin/python

import sys

stream = sys.stdin.readline().strip()

count = 0
garbage = False
cancelled = False
tracker = []

for s in stream:

  if not cancelled:

    if s == '!':
      cancelled = True
      continue

    if not garbage:
      if s == '<':
        garbage = True
      if s == '{':
        tracker.append(s)
      if s == '}':
        tracker.pop()

    else:
      if s == '>':
        garbage = False
      else:
        count += 1

  else:
    cancelled = False

print(count)
