""" Calories Burned
Created by Joseph Wong
7/02/2022
"""

# Constant Values
BICYCLING_CALORIES = 200  # bicycling calories burned per hour
JOGGING_CALORIES = 475  # jogging calories burned per hour
SWIMMING_CALORIES = 275  # swimming calories burned per hour
WEIGHT_LOSS = 0.454  # 0.454kg of weight lost:
EVERY_CALORIES = 3500  # for every 3500 calories burned

# Input hours spent on each activity
bicycling_hours = int(input("Enter the number of hours spent on bicycling: "))
jogging_hours = int(input("Enter the number of hours spent on jogging: "))
swimming_hours = int(input("Enter the number of hours spent on swimming: "))

# Total calories burned
total_calories = bicycling_hours * BICYCLING_CALORIES + jogging_hours \
                 * JOGGING_CALORIES + swimming_hours * SWIMMING_CALORIES
# Output total calories burned
print(total_calories, "total calories burned")
# Kilograms worked off based on the constant values
# of 0.454kg of weight lost for every 3500 calories burned
kilograms_worked_off = total_calories/EVERY_CALORIES * WEIGHT_LOSS
# Output kilograms worked off
print(kilograms_worked_off, "kilograms worked off")
