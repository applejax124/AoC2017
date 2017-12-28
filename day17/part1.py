#!/usr/bin/python

import sys

c_buffer = [0]
steps = int(sys.stdin.readline().strip())

index = 0
for num in range(1,2018):
  index += steps 
  index %= len(c_buffer)
  index += 1
  c_buffer.insert(index, num)

print(c_buffer)
print(c_buffer[index+1])
