""" Volume of Concrete Program v1
Created by Joseph Wong
7/02/2022
"""

building = input("Enter building type 'r' for residential, "
                 "'c' for commercial: ")  # Ask users to enter building type
while building != "X":  # while the building type is not equal to "X"
    while building != "r" and building != "c":  # if input is not "r" or "c"
        # the program will ask them to enter 'r' or 'c'
        building = input("Please enter building type 'r' for residential, "
                         "'c' for commercial: ")
    depth = ""  # this defines depth as a variable
    if building == "c":  # if building is commercial
        depth = 0.5  # the depth is 0.5m
    elif building == "r":  # if building is residential
        depth = 0.25  # the depth is 0.25m
    length = int(input("Enter the length of the building: "))  # Input length
    width = int(input("Enter the width of the building: "))  # Input width
    volume = length * width * depth  # Calculates Volume
    # Output this statement
    print(f"The volume of concrete required for a slab "
          f"with a length of {length} and with of {width} "
          f"and a depth of {depth} is {volume} cubic metres.")
    # Continue to ask for input and producing the volume results until
    # "X" is entered for building type
    building = input("Enter building type 'r' for residential, "
                     "'c' for commercial: ")
