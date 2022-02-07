""" Thunder and Lightning
Created by Joseph Wong
7/02/2022
"""

# Constant values
SOUND_SPEED = 0.34

# Input the number of seconds between lightning and thunder
time = float(input("Enter the number of seconds "
                   "between lightning and thunder: "))
# How many kilometres the storm is away
distance = time * SOUND_SPEED
# Output the amount of kilometres the storm is away
print(distance, "km")
