#!/usr/bin/python

import math

right = True
up = False
down = False
left = False

square_w = 1

x = 0
y = 0

matrix = {(0,0): 1}
val = 0

counter = 1

while val < 277678:
  val = 0

  #figure out right bounds
  if right:
    x += 1
    if x > math.floor(square_w/2) or counter == 1:
      counter = 0
      right = False
      up = True
      square_w += 2

  #figure out up bounds
  elif up:
    y += 1
    if y == math.floor(square_w/2):
      up = False
      left = True
 
  #figure out left bounds
  elif left:
    x -= 1
    if -1*x == math.floor(square_w/2):
      left = False
      down = True
  
  #figure out down bounds
  elif down:
    y -= 1
    if -1*y == math.floor(square_w/2):
      down = False
      right = True

   #calculate things
  if x >= 0 and y >= 0:
    if (x-1, y) in matrix:
      val += matrix[(x-1, y)]    
    if (x+1, y) in matrix:
      val += matrix[(x+1, y)]    
    if (x, y-1) in matrix:
      val += matrix[(x, y-1)]    
    if (x, y+1) in matrix:
      val += matrix[(x, y+1)]    
    if (x-1, y-1) in matrix:
      val += matrix[(x-1, y-1)]    
    if (x-1, y+1) in matrix:
      val += matrix[(x-1, y+1)]    
    if (x+1, y-1) in matrix:
      val += matrix[(x+1, y-1)]    
    if (x+1, y+1) in matrix:
      val += matrix[(x+1, y+1)]    

  elif x >= 0 and y < 0:
    if (x-1, y) in matrix:
      val += matrix[(x-1, y)]    
    if (x+1, y) in matrix:
      val += matrix[(x+1, y)]    
    if (x, y-1) in matrix:
      val += matrix[(x, y-1)]    
    if (x, y+1) in matrix:
      val += matrix[(x, y+1)]    
    if (x-1, y-1) in matrix:
      val += matrix[(x-1, y-1)]    
    if (x-1, y+1) in matrix:
      val += matrix[(x-1, y+1)]    
    if (x+1, y-1) in matrix:
      val += matrix[(x+1, y-1)]    
    if (x+1, y+1) in matrix:
      val += matrix[(x+1, y+1)]    

  elif x < 0 and y >= 0:
    if (x-1, y) in matrix:
      val += matrix[(x-1, y)]    
    if (x+1, y) in matrix:
      val += matrix[(x+1, y)]    
    if (x, y-1) in matrix:
      val += matrix[(x, y-1)]    
    if (x, y+1) in matrix:
      val += matrix[(x, y+1)]    
    if (x-1, y-1) in matrix:
      val += matrix[(x-1, y-1)]    
    if (x-1, y+1) in matrix:
      val += matrix[(x-1, y+1)]    
    if (x+1, y-1) in matrix:
      val += matrix[(x+1, y-1)]    
    if (x+1, y+1) in matrix:
      val += matrix[(x+1, y+1)]    

  elif x < 0 and y < 0:
    if (x-1, y) in matrix:
      val += matrix[(x-1, y)]    
    if (x+1, y) in matrix:
      val += matrix[(x+1, y)]    
    if (x, y-1) in matrix:
      val += matrix[(x, y-1)]    
    if (x, y+1) in matrix:
      val += matrix[(x, y+1)]    
    if (x-1, y-1) in matrix:
      val += matrix[(x-1, y-1)]    
    if (x-1, y+1) in matrix:
      val += matrix[(x-1, y+1)]    
    if (x+1, y-1) in matrix:
      val += matrix[(x+1, y-1)]    
    if (x+1, y+1) in matrix:
      val += matrix[(x+1, y+1)]    

  matrix[(x,y)] = val

  print(x, y, val)
