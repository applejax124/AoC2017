#!/usr/bin/python

import sys, math

def find_steps(directions):

  end = False
  while not end:
    end = True

    cancel = min(directions['ne'], directions['s'])
    directions['ne'] -= cancel
    directions['s'] -= cancel
    directions['se'] += cancel
  
    if cancel != 0:
      end = False  

    cancel = min(directions['nw'], directions['s'])
    directions['nw'] -= cancel
    directions['s'] -= cancel
    directions['sw'] += cancel
  
    if cancel != 0:
      end = False  

    cancel = min(directions['n'], directions['se'])
    directions['n'] -= cancel
    directions['se'] -= cancel
    directions['ne'] += cancel
  
    if cancel != 0:
      end = False  

    cancel = min(directions['n'], directions['sw'])
    directions['n'] -= cancel
    directions['sw'] -= cancel
    directions['nw'] += cancel
  
    if cancel != 0:
      end = False  

    cancel = min(directions['ne'], directions['nw'])
    directions['ne'] -= cancel
    directions['nw'] -= cancel
    directions['n'] += cancel
  
    if cancel != 0:
      end = False  

    cancel = min(directions['se'], directions['sw'])
    directions['se'] -= cancel
    directions['sw'] -= cancel
    directions['s'] += cancel
  
    if cancel != 0:
      end = False  

    cancel = min(directions['ne'], directions['sw'])
    directions['ne'] -= cancel
    directions['sw'] -= cancel
  
    if cancel != 0:
      end = False  

    cancel = min(directions['nw'], directions['se'])
    directions['nw'] -= cancel
    directions['se'] -= cancel
  
    if cancel != 0:
      end = False  

    cancel = min(directions['n'], directions['s'])
    directions['n'] -= cancel
    directions['s'] -= cancel
  
    if cancel != 0:
      end = False  

def main():
  while True:
  
    directions = {'n': 0, 'ne': 0, 'se': 0, 's': 0, 'sw': 0, 'nw': 0}
    path = sys.stdin.readline().strip().split(',')
  
    if path == ['']:
      break
  
    maxx = 0
    for p in path:
      directions[p] += 1
      find_steps(directions)
    
      summ = 0
      for d in directions:
        summ += directions[d]

      if summ > maxx:
        maxx = summ

    print(maxx)
  
if __name__ == "__main__":
  main()
