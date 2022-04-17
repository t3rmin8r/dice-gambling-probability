from dice import Dice

class Hand:
    def __init__(self) -> None:
        self.total = 0
        self.rollable_die = []
        self.holding_die = []

    def __repr__(self) -> str:
        return (
            f"Total: {self.total}\n"
            f"Rollable Die: {self.rollable_die}\n"
            f"Holding Die: {self.holding_die}\n"
        )

    def generate(self):
        self.rollable_die = [Dice() for _ in range(6)]

    def roll(self):

        # Roll all of the dice
        for dice in self.rollable_die:
            dice.roll()

    def analyze_table(self):
        die_picked_up = 0
        hold = []

        # Grab all the threes
        for dice in self.rollable_die:
            print(f"Could grab: {dice}")
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
        print(f"Grabbing: {dice}")
        self.holding_die.append(dice)
        for index, d in enumerate(self.rollable_die):
            if d.value == dice.value:
                self.rollable_die.pop(index)
                break