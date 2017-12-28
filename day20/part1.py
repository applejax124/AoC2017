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
  
  i += 1


for _ in range(10000):

  min_manhattan = 99999999999
  min_particle = 0

  for i, particle in enumerate(particles):

    particle['vel'][0] += particle['acl'][0]
    particle['vel'][1] += particle['acl'][1]
    particle['vel'][2] += particle['acl'][2]
  
    particle['pos'][0] += particle['vel'][0]
    particle['pos'][1] += particle['vel'][1]
    particle['pos'][2] += particle['vel'][2]
    
    manhattan = abs(particle['pos'][0]) + abs(particle['pos'][1]) + abs(particle['pos'][2])
    if manhattan < min_manhattan:
      min_manhattan = manhattan
      min_particle = i

print(min_particle)
