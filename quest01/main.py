with open("everybody_codes_e2025_q01_p3.txt") as f:
    content = [line.strip() for line in f]

names = content[0].split(",")
instructions = [(instr[0], int(instr[1:])) for instr in content[2].split(",")]
current = 0
for d, n in instructions:
    
    # Part 1
    # if d == "R": current = min(len(names)-1, current+n)
    # else: current = max(0, current-n)

    # Part 2
    # if d == "R": current = (current + n) % len(names)
    # else: current = (current - n) % len(names)

    # Part 3
    if d == "R": current = n % len(names)
    else: current = (-n) % len(names)
    names[0], names[current] = names[current], names[0]

# print(names[current]) # Parts 1 + 2
print(names[0]) # Part 3

