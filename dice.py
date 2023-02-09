import random

def roll_dice():
    roll = random.randint(1, 6)
    return roll

print("Rolling the dice...")
print("The result is:", roll_dice())
