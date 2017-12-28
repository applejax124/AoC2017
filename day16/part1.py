#!/usr/bin/python

import sys

programs = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p']
#programs = ['a', 'b', 'c', 'd', 'e']

moves = sys.stdin.readline().strip().split(',')

for move in moves:

  if move[0] == 's':
    num = int(move[1:])
    for _ in range(num):
      program = programs.pop()
      programs.insert(0, program)
  elif move[0] == 'x':
    a,b = map(int, move[1:].split('/'))
    programs[a], programs[b] = programs[b], programs[a]
  elif move[0] == 'p':
    a,b = move[1:].split('/')
    ai = programs.index(a)
    bi = programs.index(b)
    programs[ai], programs[bi] = programs[bi], programs[ai]

print(''.join(programs))
