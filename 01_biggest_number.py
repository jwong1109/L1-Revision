num1 = int(input("What is the first number? "))
num2 = int(input("What is the second number? "))
while num1 and num2 != 0:
    if num1 > num2:
        print(f"The highest number is {num1}")
    elif num2 > num1:
        print(f"The highest number is {num2}")
    else:
        print("The numbers are equal")
    num1 = int(input("What is the first number? "))
    num2 = int(input("What is the second number? "))
