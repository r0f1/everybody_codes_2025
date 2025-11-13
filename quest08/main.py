from collections import defaultdict
from itertools import combinations, pairwise

# Part 1
with open("everybody_codes_e2025_q08_p1.txt") as f:
    pins = [int(p) for p in f.read().split(",")]
print(sum(abs(a - b) == 16 for a, b in pairwise(pins)))

# Part 2
with open("everybody_codes_e2025_q08_p2.txt") as f:
    pins = [int(p) for p in f.read().split(",")]

N = 256
d = defaultdict(list)
res = 0

for idx, (a, b) in enumerate(pairwise(pins)):
    if idx >= 2:
        if (((b - a) % N) - 1) < (((a - b) % N) - 1):
            items = [((a + i) % N) + 1 for i in range(((b - a) % N) - 1)]
        else:
            items = [((a - i - 2) % N) + 1 for i in range(((a - b) % N) - 1)]

        res += sum(len([e for e in d[k] if e not in items + [a, b]]) for k in items)

    d[a].append(b)
    d[b].append(a)

print(res)

# Part 3
with open("everybody_codes_e2025_q08_p3.txt") as f:
    pins = [int(p) for p in f.read().split(",")]

N = 256
d = defaultdict(list)
res = 0

for idx, (a, b) in enumerate(pairwise(pins)):
    if idx >= 2:
        if (((b - a) % N) - 1) < (((a - b) % N) - 1):
            items = [((a + i) % N) + 1 for i in range(((b - a) % N) - 1)]
        else:
            items = [((a - i - 2) % N) + 1 for i in range(((a - b) % N) - 1)]

        res += sum(len([e for e in d[k] if e not in items + [a, b]]) for k in items)

    d[a].append(b)
    d[b].append(a)

res = 0
for a, b in combinations(list(range(1, N + 1)), 2):
    if (((b - a) % N) - 1) < (((a - b) % N) - 1):
        items = [((a + i) % N) + 1 for i in range(((b - a) % N) - 1)]
    else:
        items = [((a - i - 2) % N) + 1 for i in range(((a - b) % N) - 1)]

    knots = sum(len([e for e in d[k] if e not in items + [a, b]]) for k in items)
    if a in d[b]:
        knots += 1

    res = max(res, knots)

print(res)
