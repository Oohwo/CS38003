# Prompt: https://cdn.discordapp.com/attachments/737416979945750528/882943827797745684/unknown.png

import math

def polar2Rect(l, ang):
  x = l * math.cos(ang)
  y = l * math.sin(ang)
  return(x, y)

# test case
print(polar2Rect(2, math.pi)) # (-2.0, 2.4492935982947064e-16)
