# Prompt https://cdn.discordapp.com/attachments/737416979945750528/882944054076248064/unknown.png

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

# test cases
print(triangle_angles(1, 1, 2)) # None
print(triangle_angles(8, 6, 7)) # {57.9100487437197, 75.52248781407008, 46.56746344221023}
print(triangle_angles(3, 2, 4)) # {104.47751218592992, 28.95502437185985, 46.56746344221023}
print(triangle_angles(0, 3, 3)) # None
print(triangle_angles(7, 10, 6)) # {43.53115216737246, 100.28656061147494, 36.182287221152606}
print(triangle_angles(3, 4, 5)) # {90.0, 36.86989764584401, 53.13010235415599}
