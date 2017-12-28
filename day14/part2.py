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

def find_regions(matrix, r, c, region):
  
  if matrix[r][c] != '#':
    return False

  matrix[r][c] = region

  #top
  if r-1 >= 0:
    if matrix[r-1][c] == '#':
      find_regions(matrix, r-1, c, region)

  #bottom
  if r+1 < len(matrix):
    if matrix[r+1][c] == '#':
      find_regions(matrix, r+1, c, region)

  #left
  if c-1 >= 0:
    if matrix[r][c-1] == '#':
      find_regions(matrix, r, c-1, region)

  #right
  if c+1 < len(matrix[r]):
    if matrix[r][c+1] == '#':
      find_regions(matrix, r, c+1, region)

  return True

def main():

  string = sys.stdin.readline().strip()
  matrix = []

  for i in range(128):
    h = knot_hash(string+"-{}".format(i))
    s = len(h) * 4
    r = (bin(int(h,16))[2:]).zfill(s)
    matrix.append(r)

  #find regions
  regions = []
  for x in matrix:
    r = []
    for y in x:
      if y == '1':
        r.append('#')
      else:
        r.append('.')
    regions.append(r)

  r = 1
  for i, row in enumerate(regions):
    for j, item in enumerate(row):
      if find_regions(regions, i, j, r):
        r += 1

  maxx = 0
  for row in regions:
    for r in row:
      if r != '.':
        if r > maxx:
          maxx = r
  print(maxx)

if __name__ == "__main__":
  main()
