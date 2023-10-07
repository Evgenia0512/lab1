import math

def calculate_u(n):
    u = 1
    for i in range(1, n + 1):
        u *= (2 * i - 1)
    return u