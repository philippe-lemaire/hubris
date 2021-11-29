import random


def roll(dice):
    if "+" in dice:
        d, mod = dice.split("+")
        d = int(d[1:])
        mod = int(mod)
    else:
        d = int(dice[1:])
        mod = 0
    return random.randint(1, d) + mod
