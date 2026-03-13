import random

def play():
    print("Dice Roll Game")

    input("Zar atmak icin Enter'a bas...")

    dice = random.randint(1, 6)

    print("Zar sonucu:", dice)