n = int(input("n: "))

while n != 1:
    if n & 1 == 1:
        n = 3 * n + 1
    n = n >> 1  # equivalent to n //= 2