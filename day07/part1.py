#!/usr/bin/python

import sys

def make_empty(adj_list):
  herps = []
  for l in adj_list:
    if adj_list[l] == []:
      herps.append(l)
      for h in adj_list:
        for i, k in enumerate(adj_list[h]):
          if k == l:
            adj_list[h].pop(i)

  for j in herps:
    adj_list.pop(j, adj_list[j])

adj_list = {}

for line in sys.stdin:
  line = line.strip().split()
  adj_list[line[0]] = []

  if len(line) > 2:
    for l in line[3:]:
      l = l.strip(',')
      adj_list[line[0]].append(l)


while len(adj_list) > 1:
  make_empty(adj_list)

print(adj_list)
