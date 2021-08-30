import math

def polar2Rect(l, ang):
  x = l * math.cos(ang)
  y = l * math.sin(ang)
  return(x, y)
