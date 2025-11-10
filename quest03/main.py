# Part 1
with open("everybody_codes_e2025_q03_p1.txt") as f:
    vec = sorted(set([int(i) for i in f.read().split(",")]))
print(sum(vec))

# Part 2
with open("everybody_codes_e2025_q03_p2.txt") as f:
    vec = sorted(set([int(i) for i in f.read().split(",")]))
print(sum(vec[:20]))

# Part 3
from collections import Counter

with open("everybody_codes_e2025_q03_p3.txt") as f:
    vec = [int(i) for i in f.read().split(",")]

print(Counter(vec).most_common()[0][1])
