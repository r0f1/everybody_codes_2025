import re
import itertools

def add(a, b):
    return (a[0] + b[0], a[1] + b[1])

def mul(a, b):
    return (a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0])

def div(a, b):
    return [c1 // c2 if c1 >= 0 else -((-c1) // c2) for c1, c2 in zip(a, b)]

def bounds(a):
    return -1_000_000 <= a[0] <= 1_000_000 and -1_000_000 <= a[1] <= 1_000_000

with open("everybody_codes_e2025_q02_p3.txt") as f:
    vec = f.read()

s1, s2 = re.findall(r"\[(-?\d+),(-?\d+)\]", vec)[0]

A = int(s1), int(s2)

# Part 1
# R = 0, 0
# for _ in range(3):
#     R = mul(R, R)
#     R = div(R, (10, 10))
#     R = add(R, A)
#
# print(f"[{R[0]},{R[1]}]")

# Part 2 ranges = 101 and X = add(A, (x*10, y*10))
# Part 3
count = 0
for x, y in itertools.product(range(1001), range(1001)):
    R = 0, 0
    X = add(A, (x, y))

    for _ in range(100):
        R = mul(R, R)
        R = div(R, (100_000, 100_000))
        R = add(R, X)
        if not bounds(R):
            break
    else:
        count += 1

print(count)

