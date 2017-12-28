#!/usr/bin/python

import sys

registers = {}
maximum = 0

for line in sys.stdin:
  line = line.strip().split()
  if line[0] not in registers:
    registers[line[0]] = 0
  #check increase or decrease
  increase = False
  if line[1] == "inc":
    increase = True
  else:
    increase = False

  #check existence
  if line[4] not in registers:
    registers[line[4]] = 0

  #check conditions
  if line[5] == "==":
    if registers[line[4]] == int(line[6]):
      if increase:
        registers[line[0]] += int(line[2])
      else:
        registers[line[0]] -= int(line[2])
  elif line[5] == "!=":
    if registers[line[4]] != int(line[6]):
      if increase:
        registers[line[0]] += int(line[2])
      else:
        registers[line[0]] -= int(line[2])
  elif line[5] == ">=":
    if registers[line[4]] >= int(line[6]):
      if increase:
        registers[line[0]] += int(line[2])
      else:
        registers[line[0]] -= int(line[2])
  elif line[5] == "<=":
    if registers[line[4]] <= int(line[6]):
      if increase:
        registers[line[0]] += int(line[2])
      else:
        registers[line[0]] -= int(line[2])
  elif line[5] == ">":
    if registers[line[4]] > int(line[6]):
      if increase:
        registers[line[0]] += int(line[2])
      else:
        registers[line[0]] -= int(line[2])
  elif line[5] == "<":
    if registers[line[4]] < int(line[6]):
      if increase:
        registers[line[0]] += int(line[2])
      else:
        registers[line[0]] -= int(line[2])
  if registers[line[0]] > maximum:
    maximum = registers[line[0]]

print(max(registers.values()))
print(maximum)
