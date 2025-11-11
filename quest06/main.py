# Part 1
with open("everybody_codes_e2025_q06_p1.txt") as f:
    vec = f.read()

knights = [int(c == "a") for c in vec if c in "Aa"]
res = 0
for i, k in enumerate(knights):
    if k == 0:
        res += sum(knights[i:])
print(res)

# Part 2
with open("everybody_codes_e2025_q06_p2.txt") as f:
    vec = f.read()

res = 0
for letter in ["a", "b", "c"]:
    people = [int(c == letter) for c in vec if c in (letter, letter.upper())]
    for i, k in enumerate(people):
        if k == 0:
            res += sum(people[i:])
print(res)

# Part 3
with open("everybody_codes_e2025_q06_p3.txt") as f:
    vec = f.read()

res = 0
for letter in ["a", "b", "c"]:
    novices = [int(c == letter) for c in vec] * 1000
    mentors = [int(c == letter.upper()) for c in vec] * 1000
    for i, m in enumerate(mentors):
        if m == 1:
            lb = max(0, i - 1000)
            ub = min(i + 1 + 1000, len(novices))
            res += sum(novices[lb:ub])
print(res)
