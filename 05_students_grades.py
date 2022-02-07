""" Students' Grades
Created by Joseph Wong
7/02/2022
"""


def grade():  # Function to turn result into the awarded university grade
    if result >= 90:
        award = "A+"
    elif result >= 85:
        award = "A"
    elif result >= 80:
        award = "A-"
    elif result >= 75:
        award = "B+"
    elif result >= 70:
        award = "B"
    elif result >= 65:
        award = "B-"
    elif result >= 60:
        award = "C+"
    elif result >= 55:
        award = "C"
    elif result >= 50:
        award = "C-"
    elif result >= 40:
        award = "D"
    else:
        award = "E"
    print(award)


# From previous exercise
name = []  # defines name as a list
mark = []  # defines mark as a list
enter_name = str(input("Enter student's name: "))  # enter first student name
while enter_name != "X":  # while "X" is not entered as the student name
    name.append(enter_name)  # add name to list
    enter_mark = int(input("Enter exam mark (from 0 to 100): "))  # enter mark
    mark.append(enter_mark)  # add mark to list
    enter_name = str(input("Enter student's name: "))  # enter the next name

section = (mark.index(max(mark)))  # refer to the index number with best mark
# print the name of best student and best mark
# based on the index number with best mark
print(f"{name[section]} got the best mark of {max(mark)}")
# the average mark is the total sum of marks
# divided by the number of items entered
average_mark = sum(mark)/len(mark)
# print the average mark
print(f"The average mark for all students was {average_mark}.")

# List of Participated Students
print("Here's the list of students who participated:")
for student in name:
    print(student)

# List of the grades for each student
print("Here's the grades for each student according to the order of names:")
for result in mark:
    grade()
