#!/usr/bin/python

import sys

mat = [ '.#.', '..#', '###' ]

two_orig = []
two_new = []
for _ in range(6):
  line = sys.stdin.readline().strip().split(' => ')
  l0 = line[0].split('/')
  l1 = line[1].split('/')
  two_orig.append(l0)
  two_new.append(l1)

three_orig = []
three_new = []
for line in sys.stdin:
  line = line.strip().split(' => ')
  l0 = line[0].split('/')
  l1 = line[1].split('/')
  three_orig.append(l0)
  three_new.append(l1)

def replace(matrix, n):

  if n == 0:
    return matrix 

  new_matrix = []
  
  length = len(matrix)
  if length % 2 == 0:
    r2 = 0
    for r in range(0, length, 2):
      for c in range(0, length, 2):
        m = ['','']
        m[0] += matrix[r][c]
        m[0] += matrix[r][c+1]
        m[1] += matrix[r+1][c]
        m[1] += matrix[r+1][c+1]
        if c == 0:
          new_matrix.append('')
          new_matrix.append('')
          new_matrix.append('')
        for i, orig in enumerate(two_orig):
          zipm  = []
          for z in zip(*m):
            s = ''
            for x in z:
              s += x
            zipm.append(s)
          zipmr = []
          for z in zip(*m[::-1]):
            s = ''
            for x in z:
              s += x
            zipmr.append(s)
          if m == orig or m[::-1] == orig or zipm == orig or zipm[::-1] == orig or zipmr == orig or zipmr[::-1] == orig:
            new_matrix[r2]   += two_new[i][0]
            new_matrix[r2+1] += two_new[i][1]
            new_matrix[r2+2] += two_new[i][2]
      r2 += 3 
  else:
    r2 = 0
    for r in range(0, length, 3):
      for c in range(0, length, 3):
        m = ['','', '']
        m[0] += matrix[r][c]
        m[0] += matrix[r][c+1]
        m[0] += matrix[r][c+2]
        m[1] += matrix[r+1][c]
        m[1] += matrix[r+1][c+1]
        m[1] += matrix[r+1][c+2]
        m[2] += matrix[r+2][c]
        m[2] += matrix[r+2][c+1]
        m[2] += matrix[r+2][c+2]
        if c == 0:
          new_matrix.append('')
          new_matrix.append('')
          new_matrix.append('')
          new_matrix.append('')
        for i, orig in enumerate(three_orig):
          zipm  = []
          for z in zip(*m):
            s = ''
            for x in z:
              s += x
            zipm.append(s)
          zipmr = []
          for z in zip(*m[::-1]):
            s = ''
            for x in z:
              s += x
            zipmr.append(s)
          if m == orig or m[::-1] == orig or zipm == orig or zipm[::-1] == orig or zipmr == orig or zipmr[::-1] == orig:
            new_matrix[r2]   += three_new[i][0]
            new_matrix[r2+1] += three_new[i][1]
            new_matrix[r2+2] += three_new[i][2]
            new_matrix[r2+3] += three_new[i][3]
      r2 += 4 

  return replace(new_matrix, n-1)

final_matrix = replace(mat, 18)
count = 0
for row in final_matrix:
  for c in row:
    if c == '#':
      count += 1
print(count)
