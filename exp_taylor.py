# Prompt: https://cdn.discordapp.com/attachments/737416979945750528/882943580262518815/unknown.png

import math
def exp_talyor(x, n):
    estimation = 0
    e_to_the_x = math.exp(x)
    for num in range(n):
        estimation = estimation + ((x)**num)/(math.factorial(num))
    return(abs(estimation - e_to_the_x))
