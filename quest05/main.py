from functools import cmp_to_key


def get_quality(raw):
    id, vec = raw.split(":")
    ns = [int(i) for i in vec.split(",")]

    sword = [{"m": ns[0]}]
    for n in ns[1:]:
        for s in sword:
            if n < s["m"] and "s" not in s:
                s["s"] = n
                break
            if n > s["m"] and "l" not in s:
                s["l"] = n
                break
        else:
            sword.append({"m": n})

    return (
        int(id),
        int("".join(str(s["m"]) for s in sword)),
        [int(f"{s.get('s', '')}{s['m']}{s.get('l', '')}") for s in sword],
    )


def compare_swords(a, b):
    if a[1] == b[1]:
        for x, y in zip(a[2], b[2]):
            if x == y:
                continue
            return x - y
        return a[0] - b[0]
    return a[1] - b[1]


# Part 1
with open("everybody_codes_e2025_q05_p1.txt") as f:
    raw = f.read()

print(get_quality(raw)[1])


# Part 2
with open("everybody_codes_e2025_q05_p2.txt") as f:
    raw = [line.strip() for line in f]

qualities = [get_quality(r)[1] for r in raw]
print(max(qualities) - min(qualities))


# Part 3
with open("everybody_codes_e2025_q05_p3.txt") as f:
    raw = [line.strip() for line in f]

swords = sorted(
    [get_quality(r) for r in raw], key=cmp_to_key(compare_swords), reverse=True
)
print(sum([i * s[0] for i, s in enumerate(swords, start=1)]))
