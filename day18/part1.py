#!/usr/bin/python

import sys

registers = {}

instructions = []
for line in sys.stdin:
  line = line.strip().split()
  instructions.append(line)

i = 0
r = 0
while i > -1 and i < len(instructions):

  inst = instructions[i][0]
  reg = instructions[i][1]
  if reg not in registers:
    registers[reg] = 0

  if len(instructions[i]) == 3:
    val = instructions[i][2]
    if val not in registers:
      val = int(val)
    else: 
      val = registers[val]
  else:
    val = 0

  if inst == "snd":
    r = registers[reg]
  elif inst == "set":
    registers[reg] = val
  elif inst == "add":
    registers[reg] += val
  elif inst == "mul":
    registers[reg] *= val
  elif inst == "mod":
    if val != 0:
      registers[reg] %= val
  elif inst == "rcv":
    if registers[reg] != 0:
      print(r)
      break
  
  if inst == "jgz": 
    if registers[reg] > 0:
      i += val
      i -= 1
  
  i += 1
