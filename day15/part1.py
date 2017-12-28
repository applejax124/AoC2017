#!/usr/bin/python

import operator

A = {}
B = {}

#A[0] = 679
#B[0] = 771
A[0] = 65
B[0] = 8921

factor_A = 16807
factor_B = 48271
divisor = 2147483647

counter = 0
c = 0

for i in range(1, 40000000+1):

  new_A = factor_A * A[i-1]
  new_B = factor_B * B[i-1]

  A[i] = new_A % divisor
  B[i] = new_B % divisor

  binary_A = bin(A[i])[2:]
  binary_B = bin(B[i])[2:]

  rev_binary_B = binary_B[::-1]
  rev_binary_A = binary_A[::-1]

  while len(rev_binary_B) < 16:
    rev_binary_B += '0'
  while len(rev_binary_A) < 16:
    rev_binary_A += '0'

  if rev_binary_A[0:16] == rev_binary_B[0:16]:
    same = True
  else:
    same = False
  
  if same:
    counter += 1 

  c += 1
  if c == 1000000:
    c = 0
    x = int(i/40000000 * 100)
    print("{}% done".format(x))

print(counter)
