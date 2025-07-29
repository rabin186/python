## NOTE: Lists don't contain values directly, they contain references to the value.

import random


animals = ['Rhino' , 'Lion' , 'Tiger']
animals.insert(1, 'wolf')
print(animals)


animals.append('Elephant')
print(animals)


for index, item in enumerate(animals):
    print(f"Index {index} in animals is: {item}")

del animals[2]    #del is an statement used to remove the values available in that given index
del animals[1:3]
print(animals)

name = ['ram' , 'Sita', 'gita']
name *= 2
print(name)


random.choice(name)
print(random.choice(name))
print(name.index('ram'))

random.shuffle(name)
print(name)

#This remove method only delete the first instance of the value i.e the only one apperaring on the first
name.remove('gita')
print(name)


# This sort method sorts the given values based on ASCII of the given values i.e ASCII of lowercase alphabets is greater then uppercase alphabets. So, a cames after Z. 
name = ['ram' , 'Sita', 'gita' , 'Hari', 'hari']
name.sort(reverse=True)
print(name)

# We can use key = str.lower to have the sort() function to treat all the items in the list as if they were lowercase without actually changing the values in the list
name.sort(key=str.lower)
print(name)

name.reverse()
print(name)



#String as a type of list

name = 'Sheru a cat'
new_name = name[0:6] + 'the ' + name[8:11]
print(name)
print(new_name)



## In python unlike in C programming language, = operator don't copy the values only references the values. i.e 

new = [1,2,3,4]
# We are referencing the try_new variable to same list that existed on new veriable not creating a new list.
try_new = new  
try_new[1] = 'Changed'
# When we change value for the list using one variable the whole list is changed.
print(new) 
print(try_new)
