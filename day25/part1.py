#!/usr/bin/python

import sys

tape = [0]
state = 'A'
i = 0

for _ in range(12134527):

  if state == 'A':      #STATE A
    if tape[i] == 0:
      tape[i] = 1
      i += 1
      state = 'B'
    else:
      tape[i] = 0
      i -= 1
      state = 'C'
  elif state == 'B':    #STATE B
    if tape[i] == 0:
      tape[i] = 1
      i -= 1
      state = 'A'
    else:
      tape[i] = 1
      i += 1
      state = 'C'
  elif state == 'C':    #STATE C
    if tape[i] == 0:
      tape[i] = 1
      i += 1
      state = 'A'
    else:
      tape[i] = 0
      i -= 1
      state = 'D'
  elif state == 'D':    #STATE D
    if tape[i] == 0:
      tape[i] = 1
      i -= 1
      state = 'E'
    else:
      tape[i] = 1
      i -= 1
      state = 'C'
  elif state == 'E':    #STATE E
    if tape[i] == 0:
      tape[i] = 1
      i += 1
      state = 'F'
    else:
      tape[i] = 1
      i += 1
      state = 'A'
  elif state == 'F':    #STATE F
    if tape[i] == 0:
      tape[i] = 1
      i += 1
      state = 'A'
    else:
      tape[i] = 1
      i += 1
      state = 'E'

  if i < 0:
    i = 0
    tape.insert(0, 0)
  if i == len(tape):
    tape.append(0)

count = 0
for t in tape:
  if t == 1:
    count += 1
print(count)
