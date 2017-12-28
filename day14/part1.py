#!/usr/bin/python

import sys

def knot_hash(line):
  
  skip = 0
  curr = 0

  rope = list(range(256))
  string = []
  for l in line:
    string.append(ord(l))
  for x in [17, 31, 73, 47, 23]:
    string.append(x)
  
  for _ in range(64):
    for s in string:
      rev = []
      for l in range(s-1,-1,-1):
        pos = (curr+l)%256
        rev.append(rope[pos])
      for i, r in enumerate(rev):
        c = (curr+i)%256
        rope[c] = r
      curr += s + skip
      skip += 1
  
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
  
  for e in elements:
    hasht += format(e, '02x')

  return hasht 

def main():

  string = sys.stdin.readline().strip()
  matrix = []

  for i in range(128):
    h = knot_hash(string+"-{}".format(i))
    r = format(int(h,16), '#06b')
    print(r)
    matrix.append(r[2:])

  counter = 0
  for x in matrix:
    for y in x:
      if y == '1':
        counter += 1
  print(counter)

if __name__ == "__main__":
  main()
