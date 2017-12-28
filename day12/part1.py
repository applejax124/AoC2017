#!/usr/bin/python

import sys

def dfs_recursive(matrix, node, marked):
  
  if node in marked:
    return

  marked.append(node)

  for n in matrix[node]:
    dfs_recursive(matrix, n, marked)

def main():
  matrix = {}
  
  for line in sys.stdin:
    line = line.strip().split(' <-> ')
    prog = int(line[0])
    if prog not in matrix:
      matrix[prog] = []
  
    neighbors = line[1].split()
    for n in neighbors:
      matrix[prog].append(int(n.strip(',')))
  
  count = 0
  for prog in matrix:
    marked = []
    dfs_recursive(matrix, prog, marked)
    if 0 in marked:
      count += 1

  print(count)
    
if __name__ == "__main__":
  main()
