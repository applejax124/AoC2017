#!/usr/bin/python

import sys

particles = []

i = 0
for line in sys.stdin:
  
  line = line.split()

  pos = line[0][3:].strip('>,')
  pos = pos.split(',')

  vel = line[1][3:].strip('>,')
  vel = vel.split(',')

  acl = line[2][3:].strip('>')
  acl = acl.split(',')

  particles.append({})

  particles[i]['pos'] = []
  for p in pos:
    particles[i]['pos'].append(int(p))

  particles[i]['vel'] = []
  for v in vel:
    particles[i]['vel'].append(int(v))

  particles[i]['acl'] = []
  for a in acl:
    particles[i]['acl'].append(int(a))

  particles[i]['dead'] = False
  
  i += 1

for j in range(1000):

  for i, particle in enumerate(particles):
    if not particle['dead']:
      particle['vel'][0] += particle['acl'][0]
      particle['vel'][1] += particle['acl'][1]
      particle['vel'][2] += particle['acl'][2]
    
      particle['pos'][0] += particle['vel'][0]
      particle['pos'][1] += particle['vel'][1]
      particle['pos'][2] += particle['vel'][2]
  
  for p1 in particles:
    for p2 in particles:
      if p1 != p2 and p1['pos'] == p2['pos']:
        if (p1['dead'] == j or not p1['dead']) and (p2['dead'] == j or not p2['dead']): 
          p2['dead'] = j
          p1['dead'] = j

count = 0
for p in particles:
  if not p['dead']:
    count += 1
print(count)
