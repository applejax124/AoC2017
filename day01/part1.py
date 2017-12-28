#!/usr/bin/python

import sys

def main():
  for line in sys.stdin:
    digits = []
    for l in line:
      try:
        digits.append(int(l))
      except:
        pass
    summ = 0
    for i, d in enumerate(digits):
      if d == digits[(i+1)%len(digits)]:
        summ += d
    print(summ)

if __name__ == "__main__":
  main()
