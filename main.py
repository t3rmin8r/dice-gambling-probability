from dice import Dice
from hand import Hand

h1 = Hand()
h1.generate()

print(h1)
h1.roll()
print(h1)
h1.analyze_table()
print(h1)