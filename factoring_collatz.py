"""
factorization of numbers 3n+1 for odd n in interval k through n
"""

import sympy

n = int(input("n: "))
k = int(input("k: "))

for i in range(k, n + 1):
    if i % 2 == 1:  # odd
        print(f"{i} -> {3*i+1} = {sympy.factorint(3*i+1)}")