import random

def roll_die(sides):
    return random.randint(1, sides)
def roll_dice(number_dice, sides, modifier=0):
    total = 0
    for _ in range(number_dice):
        total += roll_die(sides)
    return total + modifier

def roll_d20 (modifier=0, advantage=False, disadvantage=False):
    first = roll_die(20)
    if advantage or disadvantage:
        second = roll_die(20)
        chosen = max(first, second) if advantage else min(first, second)
    else:
        chosen = first
    return {
        "raw": chosen,
        "total": chosen + modifier,
        "critical_hit": chosen == 20,
        "critical_fail": chosen == 1,
    }
    
def ability_modifier(score):
    return (score - 10) // 2
