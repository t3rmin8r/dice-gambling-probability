from random import random
from dice import Dice

class Hand:
    def __init__(self, uid):
        self.uid = uid
        self.total = 0
        self.rollable_die = []
        self.holding_die = []

    def __repr__(self) -> str:
        return (
            f"<===> Player {self.uid} <===>\n"
            f"Total: {self.total}\n"
            f"Rollable Die:\n{self.rollable_die}\n"
            f"Holding Die:\n{self.holding_die}\n"
            f"<============>\n"
        )

    def generate(self):
        self.rollable_die = [Dice() for _ in range(5)]

    def roll(self):

        # Roll all of the dice
        for dice in self.rollable_die:
            dice.roll()

    def analyze_table(self):
        die_picked_up = 0
        hold = []

        # Grab all the threes
        for dice in self.rollable_die:
            if dice.value == 3:
                hold.append(dice)
                die_picked_up += 1
        for dice in hold:
            self.grab_dice(dice)

        if die_picked_up > 0:
            pass
        else:
            lowest = None
            for dice in self.rollable_die:
                if not lowest:
                    lowest = dice
                    continue
                if dice.value < lowest.value:
                    lowest = dice
            self.grab_dice(lowest)
            self.total += lowest.value
        

    def grab_dice(self, dice):
        self.holding_die.append(dice)
        for index, d in enumerate(self.rollable_die):
            if d.value == dice.value:
                self.rollable_die.pop(index)
                break

    def play_round(self):
        while len(self.rollable_die) > 0:
            self.roll()
            self.analyze_table()

    def __eq__(self, hand: object) -> bool:
        if self.uid != hand.uid:
            return self.total == hand.total
        else:
            return False

    def __lt__(self, hand: object) -> bool:
        return self.total < hand.total

    def __gt__(self, hand: object) -> bool:
        return self.total > hand.total