""" Biggest Number v1
Created by Joseph Wong
4/02/2022
"""

num1 = int(input("What is the first number? "))  # input first number
num2 = int(input("What is the second number? "))  # input second number
while num1 and num2 != 0:  # while the rogue number of 0 is not entered
    if num1 > num2:  # if first number is greater than the second number
        # the highest number is the first number
        print(f"The highest number is {num1}")
    elif num2 > num1:  # if second number is greater than the first number
        # the highest number is the second number
        print(f"The highest number is {num2}")
    else:  # otherwise the numbers are equal
        print("The numbers are equal")
    # Asks to input first and second numbers again
    num1 = int(input("What is the first number? "))
    num2 = int(input("What is the second number? "))
