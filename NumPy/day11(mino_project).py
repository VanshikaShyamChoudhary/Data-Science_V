# 🌟 Mini Project 
# Make a Dice Simulator.
import numpy as np
# Requirements:
# Generate one random number between 1 and 6.
Dice_1=np.random.randint(1,6)
# print("You rolled: ",Dice_1)
# Print:
# You rolled: 4

# Then improve it:

# Generate two dice.
Dice_2=np.random.randint(1,6)
print("Dice 1: ",Dice_1)
print("Dice 2: ",Dice_2)

total=(Dice_1+Dice_2)
print("Total = ",total)
print("You have to move",total,"steps")
# Example:

# Dice 1: 5
# Dice 2: 2
# Total = 7
