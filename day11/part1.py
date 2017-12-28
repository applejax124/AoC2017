#!/usr/bin/python

import sys, math

#while True:
#
#  directions = {'n':(0,1), 'ne':(math.sqrt(2)/2,math.sqrt(2)/2), 'se':(math.sqrt(2)/2,-1*math.sqrt(2)/2), 
#                's':(0,-1), 'sw':(-1*math.sqrt(2)/2,-1*math.sqrt(2)/2), 'nw':(-1*math.sqrt(2)/2,math.sqrt(2)/2)}
#  start = [0,0]
#  
#  path = sys.stdin.readline().strip().split(',')
#  if path == ['']:
#    break
#  
#  for p in path:
#    start[0] += directions[p][0]
#    start[1] += directions[p][1]
#  
#  print(start)

while True:

  directions = {'n': 0, 'ne': 0, 'se': 0, 's': 0, 'sw': 0, 'nw': 0}
  path = sys.stdin.readline().strip().split(',')

  if path == ['']:
    break

  for p in path:
    directions[p] += 1

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

  summ = 0
  for d in directions:
    summ += directions[d]
  print(directions)
  print(summ)
