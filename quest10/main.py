# Part 1
# import numpy as np

# with open("everybody_codes_e2025_q10_p1.txt") as f:
#     text = f.read().splitlines()
# arr = np.array([list(line) for line in text])
# lim_y, lim_x = arr.shape
# dragon_y, dragon_x = np.ravel(np.argwhere(arr == "D")).tolist()
# sheeps = set((x, y) for y, x in np.argwhere(arr == "S").tolist())
# possible = {(dragon_x, dragon_y)}
# for _ in range(4):
#     current = set()
#     for x, y in possible:
#         dirs = [
#             (x, y),
#             (x + 2, y + 1),
#             (x + 2, y - 1),
#             (x - 2, y + 1),
#             (x - 2, y - 1),
#             (x - 1, y + 2),
#             (x - 1, y - 2),
#             (x + 1, y - 2),
#             (x + 1, y + 2),
#         ]
#         for cx, cy in dirs:
#             if 0 <= cx < lim_x and 0 <= cy < lim_y:
#                 current.add((cx, cy))
#     possible = current
# print(len(set.intersection(sheeps, possible)))

# # Part 2
# import numpy as np


# def get_positions(x, y):
#     return [
#         (x + 2, y + 1),
#         (x + 2, y - 1),
#         (x - 2, y + 1),
#         (x - 2, y - 1),
#         (x - 1, y + 2),
#         (x - 1, y - 2),
#         (x + 1, y - 2),
#         (x + 1, y + 2),
#     ]


# with open("everybody_codes_e2025_q10_p2.txt") as f:
#     # with open("test.txt") as f:
#     text = f.read().splitlines()
# arr = np.array([list(line) for line in text])
# lim_y, lim_x = arr.shape
# dragon_y, dragon_x = np.ravel(np.argwhere(arr == "D")).tolist()
# sheeps = set((x, y) for y, x in np.argwhere(arr == "S").tolist())
# hides = set((x, y) for y, x in np.argwhere(arr == "#").tolist())

# possible = {(dragon_x, dragon_y)}

# res = 0
# for _ in range(20):
#     current = set()
#     for x, y in possible:
#         for cx, cy in get_positions(x, y):
#             if 0 <= cx < lim_x and 0 <= cy < lim_y:
#                 current.add((cx, cy))
#     possible = current

#     eaten = set.intersection(set.difference(sheeps, hides), possible)
#     res += len(eaten)
#     sheeps = {(x, y + 1) for x, y in set.difference(sheeps, eaten) if (y + 1) < lim_y}
#     eaten = set.intersection(set.difference(sheeps, hides), possible)
#     res += len(eaten)
#     sheeps = {(x, y) for x, y in set.difference(sheeps, eaten)}

# print(res)


# Part 3
import numpy as np


def get_positions(x, y):
    return [
        (x + 2, y + 1),
        (x + 2, y - 1),
        (x - 2, y + 1),
        (x - 2, y - 1),
        (x - 1, y + 2),
        (x - 1, y - 2),
        (x + 1, y - 2),
        (x + 1, y + 2),
    ]


def all_next_sheep_moves(sheeps_pos, dragon_pos):
    dx, dy = dragon_pos
    return list(
        (x, y + 1)
        for x, y in sheeps_pos
        if (y + 1) < (lim_y + 1) and (x, y + 1) != (dx, dy)
    )


def all_next_dragon_moves(dragon_pos):
    res = list()
    dx, dy = dragon_pos
    for cx, cy in get_positions(dx, dy):
        if 0 <= cx < lim_x and 0 <= cy < lim_y:
            res.append((cx, cy))
    return res


def next_move_dragon_turn(sheeps_pos, dragon_pos, previous_moves):
    pass


def next_move_sheep_turn(sheeps_pos, dragon_pos, moves):
    if len(sheeps_pos) == 0:
        return moves

    for sx, sy in all_next_sheep_moves(sheeps_pos, dragon_pos):
        moves.append(f"S>{sy}")
        sheeps_pos_new = [(sx, sy)] + [(x, y) for x, y in sheeps_pos if x != sx]
        next_move_dragon_turn(sheeps_pos_new, dragon_pos, moves)

    return moves


# with open("everybody_codes_e2025_q10_p3.txt") as f:
with open("test.txt") as f:
    text = f.read().splitlines()
arr = np.array([list(line) for line in text])
lim_y, lim_x = arr.shape
dragon_y, dragon_x = np.ravel(np.argwhere(arr == "D")).tolist()
dragon_pos = (dragon_x, dragon_y)
sheeps_pos = list((x, y) for y, x in np.argwhere(arr == "S").tolist())
hides = set((x, y) for y, x in np.argwhere(arr == "#").tolist())

moves = next_move_sheep_turn(sheeps_pos, dragon_pos, [])
print(moves)
