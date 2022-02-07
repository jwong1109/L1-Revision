""" Students' Average Mark v1
Created by Joseph Wong
7/02/2022
"""

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
