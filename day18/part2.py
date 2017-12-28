#!/usr/bin/python

from collections import deque
import sys

#Define instructions list
instructions = []
for line in sys.stdin:
  line = line.strip().split()
  instructions.append(line)

#Define program variables
registers_0 = {"p": 0, "counter": 0, "sent": 0}
registers_1 = {"p": 1, "counter": 0, "sent": 0}
queue_0 = deque()
queue_1 = deque()

#Define program 
def prog(registers, queue_in, queue_out):

  while registers["counter"] >= 0 and registers["counter"] < len(instructions):
    
    def val(r):
      if r.isalpha():
        # returns a default value of 0 if r is not a key in the dictionary
        return registers.get(r,0)
      else:
        return int(r)

    i = registers["counter"]

    inst = instructions[i][0]
    reg  = instructions[i][1]
    try:
      v  = instructions[i][2]
    except:
      v = '0'

    if inst == "set":
      registers[reg] = val(v)
    if inst == "add":
      registers[reg] = val(reg) + val(v)
    if inst == "mul":
      registers[reg] = val(reg) * val(v)
    if inst == "mod":
      registers[reg] = val(reg) % val(v)
    if inst == "jgz":
      if val(reg) > 0:
        registers["counter"] += val(v)
        continue
    if inst == "snd":
      queue_out.append(val(reg))
      registers["sent"] += 1
    if inst == "rcv":
      if len(queue_in) == 0:
        return True
      registers[reg] = queue_in.popleft()
    registers["counter"] += 1
    
  return False

#Define main
def main():
  
  while True:
    if not prog(registers_0, queue_1, queue_0):
      break
    if not prog(registers_1, queue_0, queue_1):
      break
    if len(queue_0) == 0 and len(queue_1) == 0:
      break

  print(registers_1["sent"])

#Call main
if __name__ == "__main__":
  main()
