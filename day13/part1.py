#!/usr/bin/python

import sys

def main():
  
  layers = {}
  
  while True:
    try:
      d, r = sys.stdin.readline().strip().split()
      d = int(d.strip(':'))
      r = int(r)
    except:
      break
    
    layers[d] = []
    for _ in range(r):
      layers[d].append('.')

  max_d = d
  severity = 0
  curr = 0

  for d in layers:
    layers[d][0] = 'S'

  for p in range(1, max_d+2):
    if curr in layers:
      if layers[curr][0] == 'S':
        severity += curr*len(layers[curr])
    curr += 1
  
    for d in layers:
      l = len(layers[d])
      
      if l>2: 
        l2 = l + l-2
        f = p%l2
        f2 = (p-1)%l2
        if f > l-1:
          f = l2 - f
        if f2 > l-1:
          f2 = l2 - f2
      else:
        f2 = (p-1)%l
        f = p%l

      layers[d][f2] = '.'
      layers[d][f] = 'S'

  print(severity)

if __name__ == "__main__":
  main()
