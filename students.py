# with open('students.csv', 'r') as file:
#     for line in file:
#         row = line.rstrip().split(",")
#         print(f'{row[0]} is in {row[1]} house.')
#
#


# students = []
# with open('students.csv', 'r') as file:
#     for line in file:
#         name, house = line.rstrip().split(",")
#         students.append(f'{name} is in {house} house.')
#         
# for student in sorted(students):
#     print(student)


# students = []
# with open('students.csv', 'r') as file:
#     for line in file:
#         name, house = line.rstrip().split(",")
#         student = {"name": name, "house": house}
#         # student['name'] = name
#         # student['house'] = house
#         students.append(student)


# def get_name(student):
#     return student["name"]


# for student in sorted(students, key = lambda student: student["name"]):
#     print(f'{student['name']} is in {student['house']} house.')



#Note: The split function splits the passed string when 
#the passed element/letter is found (in this case ',') 
#i.e when the function founds , it splits the string into 
#two strings.
