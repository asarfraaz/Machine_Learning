""" 
    Program to calculate mean and standard deviation 
    from a frequency distribution table
"""

from random import choices
from collections import Counter
from statistics import mean, pstdev
from freq_dist import play_game

import matplotlib as mpl
mpl.use('TkAgg')

import matplotlib.pyplot as plt

freq = play_game()
# Assume that we only have 'freq', the frequency distribution table

# If we play the above game 5 times.
# Let's assume that the below list represents the number of red balls
# obtained in each game

events = [2, 3, 2, 3, 1]

# The average number of red balls picked up in each game is
avg = sum(events)/5 # since there are 5 games played
print(avg)

# This can also be easily done using the following functions
mn = mean(events)
std_dev = pstdev(events)
print("Mean :", mn, "Std Dev:", std_dev)

# Lets extend this to 'freq'
events = freq.elements()
print(list(events))
mn = mean(freq.elements())
std_dev = pstdev(freq.elements())
print(f"Mean : {mn:.2f} Std Dev: {std_dev:.2f}")


xvalues = freq.keys()
yvalues = freq.values()
plt.bar(xvalues, yvalues)
plt.show()
