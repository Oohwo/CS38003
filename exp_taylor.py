import math
def exp_talyor(x, n):
    estimation = 0
    e_to_the_x = math.exp(x)
    for num in range(n):
        estimation = estimation + ((x)**num)/(math.factorial(num))
    return(abs(estimation - e_to_the_x))
