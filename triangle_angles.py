import math

def triangle_angles(a, b, c):
  if (a == 0 or b == 0 or c == 0):
    return None
    
  angle_a = math.acos((a**2 + b**2 - c**2) / (2 * a * b)) * (180 / math.pi)
  angle_b = math.acos(((b**2 + c**2 - a**2) / (2 * b * c))) * (180 / math.pi)
  angle_c = math.acos((a**2 + c**2 - b**2) / (2 * a * c)) * (180 / math.pi)
  canConstruct = False
  if (a >= b and a >= c):
    if (b + c) > a:
      canConstruct = True
  elif (b >= a and b >= c):
    if (a + c) > b:
      canConstruct = True
  elif (c >= a and c >= b):
    if (a + b) > c:
      canConstruct = True
  if (canConstruct == False):
    return None
  return{angle_a, angle_b, angle_c}
