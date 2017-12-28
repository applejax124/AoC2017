#!/usr/bin/python

import sys, re

def check_weights(l, wrong):
  x = 0
  r = 0

  if len(adj_list[l]) == 1:
    return adj_list[l][0]
  weights = []
  for node in adj_list[l][1:]:
    weights.append(check_weights(node, wrong))
  
  for i, w in enumerate(weights):
    for j, y in enumerate(weights):
      if w != y and i != j:
        x = w
        r = y 
        continue
      if r != 0 and x != 0:
        if r == y:
          wrong = x
        else:
          wrong = r
  if wrong != 0:
    print(adj_list[l][0])
    for s in adj_list[l][1:]:
      print(s, adj_list[s][0], check_weights(s,0))
    print("wrong:", wrong)
    print("x:", x)
    print("r:", r)
    print('\n')
    
  return adj_list[l][0] + sum(weights)

adj_list = {}
for line in sys.stdin:
  line = line.strip().split()
  num = re.sub('[()]', '', line[1])
  adj_list[line[0]] = [int(num)]
  for l in line[3:]:
    l = l.strip(',')
    adj_list[line[0]].append(l)

wrong = 0
check_weights('aapssr', wrong)
