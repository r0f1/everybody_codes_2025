import math

# Part 1
with open("everybody_codes_e2025_q04_p1.txt") as f:
    vec = [int(i) for i in f]

fac = math.prod([x / y for x, y in zip(vec, vec[1:])], start=2025)
print(int(fac))

# Part 2
with open("everybody_codes_e2025_q04_p2.txt") as f:
    vec = [int(i) for i in f]

fac = math.prod([x / y for x, y in zip(vec, vec[1:])])
print(math.ceil(10_000_000_000_000 / fac))

# Part 3
with open("everybody_codes_e2025_q04_p3.txt") as f:
    raw = [line.strip() for line in f]

start, mid, end = int(raw[0]), raw[1:-1], int(raw[-1])
vec = [(0, start)] + [[int(k) for k in x.split("|")] for x in mid] + [(end, 0)]
fac = math.prod([x[1] / y[0] for x, y in zip(vec, vec[1:])], start=100)
print(int(fac))
