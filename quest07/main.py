# Part 1
with open("everybody_codes_e2025_q07_p1.txt") as f:
    raw = [line.strip() for line in f]

names = raw[0].split(",")
rules = dict([[a, set(b.split(","))] for a, b in [r.split(" > ") for r in raw[2:]]])


for name in names:
    for i in range(len(name) - 1):
        if name[i + 1] not in rules.get(name[i], set()):
            break
    else:
        print(name)
        break

# Part 2
with open("everybody_codes_e2025_q07_p2.txt") as f:
    raw = [line.strip() for line in f]

names = raw[0].split(",")
rules = dict([[a, set(b.split(","))] for a, b in [r.split(" > ") for r in raw[2:]]])

res = 0
for idx, name in enumerate(names, start=1):
    for i in range(len(name) - 1):
        if name[i + 1] not in rules.get(name[i], set()):
            break
    else:
        res += idx
print(res)


# Part 3
def combinations(name, rules):
    if len(name) == 11:
        return {name}
    letters = rules.get(name[len(name) - 1], None)
    if letters is None:
        return {name}
    new_names = [f"{name}{c}" for c in letters]
    return set.union({name}, *[combinations(n, rules) for n in new_names])


with open("everybody_codes_e2025_q07_p3.txt") as f:
    raw = [line.strip() for line in f]

names = raw[0].split(",")
rules = dict([[a, set(b.split(","))] for a, b in [r.split(" > ") for r in raw[2:]]])

res = set()
for idx, name in enumerate(names, start=1):
    for i in range(len(name) - 1):
        if name[i + 1] not in rules.get(name[i], set()):
            break
    else:
        res = res.union(combinations(name, rules))

print(len([r for r in res if len(r) >= 7]))
