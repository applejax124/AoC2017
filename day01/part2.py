#!/usr/bin/python

import sys, math

def main():
  for line in sys.stdin:
    digits = []
    for l in line:
      try:
        digits.append(int(l))
      except:
        pass
    summ = 0
    lent = math.floor(len(digits)/2)
    for i, d in enumerate(digits):
      if d == digits[(i+lent)%len(digits)]:
        summ += d
    print(summ)

if __name__ == "__main__":
  main()
