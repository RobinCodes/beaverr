a = 8
b = 3
iteration = 0

while b != 0:
    iteration += 1

    a = a + (a >> 1)
    b = b + (2 - (a % 2) * 3)

    if iteration % 10_000 == 0:
        print(f"Iteration {iteration:,d}")

print(f"Finished after {iteration} iterations.")
print(f"Final values: a = {a}, b = {b}")
