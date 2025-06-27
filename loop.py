# # Here, students is an list
#
# students = ["ram" , "shyam" , "hari"]
#
# for student in students:
#     print(student)
#
# for i in range(len(students)):
#     print(i + 1, students[i])
#

# # Here, stdents is an dictionary
#
# students = {
#         "Ram" : "Red",
#         "Shyam" : "Green",
#         "Hari" : "Blue",
# }
#
# for student in students:
#     print(student, students[student], sep=", ")

students = [
        {"name" : "Ram" , "House" : "Red" , "Address" : "Gongabhu"},
       {"name" : "Shyam" , "House" : "Green" , "Address" : "Nepaltar"},
        {"name" : "Hari" , "House" : "Blue" , "Address" : "Macchapokhari"}  
]


for student in students:
    print(student["name"] , student["House"] , student["Address"] ,sep = ", ")
