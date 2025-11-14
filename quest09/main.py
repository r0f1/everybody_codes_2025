from itertools import permutations


def is_child(child, parent1, parent2):
    return all(c in (p1, p2) for c, p1, p2 in zip(child, parent1, parent2))


def overlap(child, parent):
    return sum(c == p for c, p in zip(child, parent))


# Part 1
with open("everybody_codes_e2025_q09_p1.txt") as f:
    lines = [line.strip().split(":")[1] for line in f]

for a, b, c in permutations(lines, 3):
    if is_child(a, b, c):
        print(overlap(a, b) * overlap(a, c))
        break

# Part 2
with open("everybody_codes_e2025_q09_p2.txt") as f:
    lines = [line.strip().split(":")[1] for line in f]

scores = [
    overlap(a, b) * overlap(a, c)
    for a, b, c in permutations(lines, 3)
    if b > c and is_child(a, b, c)
]
print(sum(scores))

# Part 3
with open("everybody_codes_e2025_q09_p3.txt") as f:
    lines = [[int(num), dna.strip()] for num, dna in [line.split(":") for line in f]]

trees = [
    {a[0], b[0], c[0]}
    for a, b, c in permutations(lines, 3)
    if b > c and is_child(a[1], b[1], c[1])
]

current_trees = trees
trees_merged = []
prev_len = len(current_trees)

while prev_len != len(trees_merged):
    prev_len = len(trees_merged)

    trees_merged = [current_trees[0]]
    for tree_old in current_trees[1:]:
        for tree_merged in trees_merged:
            if any(to in tree_merged for to in tree_old):
                tree_merged.update(tree_old)
                break
        else:
            trees_merged.append(tree_old)

print(sum(max(trees_merged, key=len)))
