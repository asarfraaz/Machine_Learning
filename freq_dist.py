""" 
    Program to create a frequency distribution table
"""

from random import choices
from collections import Counter
import matplotlib as mpl
mpl.use('TkAgg') # Applicable only on Mac for virtual environments

import matplotlib.pyplot as plt

bag = ['R', 'R', 'R', 'B', 'B'] # a bag containing 3 Red balls and 2 Blue balls

# To simulate a person picking a ball at random
# and repeating this 4 times [ assuming he picks a ball, puts it back in the
# bag and picks up another new ball everytime ]

event = choices(bag, k=4) # pick a ball from the bag and repeat it 4 times
print(event)

# number of Red balls in the game
count = event.count('R')
print(count)

# simulate this game being played for 75 players
def play_game(players=75):
    person = 0
    all_events = list() # Represents number of red balls picked up in each game
    while person < players:
        event = choices(bag, k=4)
        count = event.count('R')
        all_events.append(count)
        person += 1

    print(all_events)

    freq_table = Counter() # frequency counter
    freq_table.update(all_events)
    print(freq_table)
    return freq_table

if __name__ == "__main__":
    freq = play_game()

    xvalues = freq.keys()
    yvalues = freq.values()
    plt.bar(xvalues, yvalues)
    plt.show()
