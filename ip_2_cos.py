import math

iterations = 20

def my_cos(x):
    """
    """
    partial_sum = 0
    x_pow = 1
    for n in range(0, iterations, 2):

        minus = x_pow * x ** 2 / (2 * n + 1 ) / (2 * n + 2)
        partial_sum += x_pow - minus
        x_pow = minus * x ** 2 / (2 * n + 3) / (2 * n + 4 )
    
    return partial_sum

print(my_cos(0.125))
print(math.cos(0.125))
