#!/usr/bin/python

import sys, math

grid = []

for line in sys.stdin:
  line = line.strip()
  row = []
  for l in line:
    row.append(l)
  grid.append(row)

size = len(grid)
mid = math.floor(size / 2)

r = mid
c = mid

count = 0

# 0 - up | 1 - right | 2 - down | 3 - left
direction = 0

for i in range(10000):
  
  if grid[r][c] == '.':
    direction -= 1
    grid[r][c] = '#'
    count += 1
  elif grid[r][c] == '#':
    direction += 1
    grid[r][c] = '.'
  direction %= 4 

  if direction == 0:
    r -= 1
    if r < 0:
      size += 1
      r = 0
      for g in grid:
        g.append('.')
      grid.insert(0, ['.']*size)
  elif direction == 1:
    c += 1
    if c >= size:
      size += 1
      for g in grid:
        g.append('.')
      grid.append(['.']*size)
  elif direction == 2:
    r += 1
    if r >= size:
      size += 1
      for g in grid:
        g.append('.')
      grid.append(['.']*size)
  elif direction == 3:
    c -= 1
    if c < 0:
      size += 1
      c = 0
      for g in grid:
        g.insert(0, '.')
      grid.append(['.']*size)

print(count)
