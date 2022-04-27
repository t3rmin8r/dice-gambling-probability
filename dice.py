import random


class Dice:
    def __init__(self) -> None:
        self.value = 0

    def roll(self):
        self.value = random.randint(1, 6)

    def __repr__(self) -> str:
        return f"{self.value}"
