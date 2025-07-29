# name = input("What's your Name? ")
#
#
##For writing in file
# with open('names.txt', 'a') as file:
#     file.write(f'{name}\n')
#
#
##For printing/reading from a file
# with open('names.txt', 'r' ) as file:
#     lines = file.readlines()
#
# for line in lines:
#     print(line, end='', sep='')
#
#
##For using rstrip to strip away extra spaces
# with open('names.txt', 'r' ) as file:
#      for line in file:
#         print(line.rstrip())
#
#
# #For printing names in alphabetical order
# names = []
#
# with open('names.txt') as file:
#     for line in file:
#         names.append(line.rstrip())
#
# for name in sorted(names):        
#     print(name)


##we can add reverse=True to print the names in reverse alphabetical order


##For sorting the name during reading the file itself and then printing it

with open('names.txt') as file:
    for line in sorted(file):      
        print(line.strip())
