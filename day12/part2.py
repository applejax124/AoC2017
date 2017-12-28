#!/usr/bin/python

import sys
from collections import Counter

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
  
  lists = []
  for prog in matrix:
    marked = []
    dfs_recursive(matrix, prog, marked)
    l = []
    for m in marked:
      l.append(m)
    lists.append(l)
    
  single = set()
  for i, l in enumerate(lists):
    lsort = sorted(l)
    lsort = ''.join(map(str,lsort))
    for j, k in enumerate(lists):
      ksort = sorted(k)
      ksort = ''.join(map(str,ksort))
      single.add(lsort)
      single.add(ksort)

  print(len(single))
  
if __name__ == "__main__":
  main()
