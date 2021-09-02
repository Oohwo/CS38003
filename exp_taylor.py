# Prompt: https://cdn.discordapp.com/attachments/737416979945750528/882943580262518815/unknown.png

import math
def exp_talyor(x, n):
    estimation = 0
    e_to_the_x = math.exp(x)
    for num in range(n):
        estimation = estimation + ((x)**num)/(math.factorial(num))
    return(abs(estimation - e_to_the_x))

# test cases
print(exp_taylor(3.0, 1)) # 19.085536923187664
print(exp_taylor(3.0, 5)) # 3.7105369231876644
print(exp_taylor(3.0, 10)) # 0.022144066044809563
print(exp_taylor(3.0, 100)) # 3.552713678800501e-15
print(exp_taylor(4.5, 10)) # 1.5386387816880926
