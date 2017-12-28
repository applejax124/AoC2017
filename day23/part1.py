#!/usr/bin/python

import sys

registers = {}

instructions = []
for line in sys.stdin:
  line = line.strip().split()
  instructions.append(line)

i = 0
r = 0
count = 0
while i > -1 and i < len(instructions):

  def val(r):
    if r.isalpha():
      # returns a default value of 0 if r is not a key in the dictionary
      return registers.get(r,0)
    else:
      return int(r)

  inst = instructions[i][0]
  reg = instructions[i][1]
  try:
    v = instructions[i][2]
  except:
    v = '0'

  if inst == "set":
    registers[reg] = val(v)
  elif inst == "sub":
    registers[reg] = val(reg) - val(v)
  elif inst == "mul":
    registers[reg] = val(reg) * val(v)
    count += 1
  elif inst == "jnz": 
    if val(reg) != 0:
      i += val(v)
      i -= 1
  
  i += 1

print(count)
