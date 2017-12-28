#!/usr/bin/python

import operator

A = {}
B = {}

A[0] = 679
B[0] = 771
#A[0] = 65
#B[0] = 8921

factor_A = 16807
factor_B = 48271
divisor = 2147483647

counter = 0
mA = 0
mB = 0
mG = 0
i = 1

multiples_A = {}
multiples_B = {}

c = 0
while mG < 5000000:

  new_A = factor_A * A[i-1]
  new_B = factor_B * B[i-1]

  A[i] = new_A % divisor
  B[i] = new_B % divisor

  if A[i] % 4 == 0:
    multiples_A[mA] = A[i]
    mA += 1
  if B[i] % 8 == 0:
    multiples_B[mB] = B[i]
    mB += 1

  if mG in multiples_A and mG in multiples_B:
    binary_A = bin(multiples_A[mG])[2:]
    binary_B = bin(multiples_B[mG])[2:]

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
    mG += 1

    c+=1
    if c == 10000:
      x = int(mG / 5000000 * 100) 
      print("{}% done".format(x))
      c = 0

  i += 1

print(counter)
