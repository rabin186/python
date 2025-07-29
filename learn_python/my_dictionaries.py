## Unlike an lists, dictionaries have key-values pair and key acts like an index in list.In dictionary there is no first item like in list i.e. list[0] 

animal1 = ['cat', 'dog', 'monkey']
animal2 = ['dog' ,'cat', 'monkey']
print(animal1 == animal2)

pet1 = {'name':'Kitty' , 'species':'cat', 'age':'3'}
pet2 = {'species':'cat','name':'Kitty' , 'age':'3'}
print(pet1 == pet2)

## We can use these three dictionary methods to return keys, values and items of a dictionary.
for i in pet1.keys():
    print(i, end=" ")
print()

## To see the keys in list like structure.
print(list(pet1.keys()))

for i in pet2.items():
    print(i, end=" ")
print()

for i in pet1.values():
    print(i, end=" ")
print()

## Get method is used to view whether a key exists or not in the given dictionary.
picnic_items = {'fruits':'5','vegetables':'7'}
print('I am bringing ' + str(picnic_items.get('fruits',0)) + 'kg of fruits.')
print('I am bringing ' + str(picnic_items.get('fish',0)) + 'kg of  fish.')

## We can also set a default value for a key in dictionary if value in the given key isn't available.
friends = {'name':'Ram','age':'19'}
friends.setdefault('course','CSIT')
print(friends['course'])
print(friends)



message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}

for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1

print(count)
