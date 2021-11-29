from random import randint


def find_key(roll, table):
    """Finds the lowest valid key in a dict where the keys are integers"""
    for key in table:
        if key <= roll:
            candidate = key
    return candidate


def roll(dice):
    """Rolls a dice with or without a modifier. For negative modifiers user roll('d6+-1')."""
    if "+" in dice:
        d, mod = dice.split("+")
        d = int(d[1:])
        mod = int(mod)
    else:
        d = int(dice[1:])
        mod = 0
    return randint(1, d) + mod
