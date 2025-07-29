##This is a tuple. It is different from lists as we use parenthesis instead of square bracket in it and as an string an tuple is also immutable.

animals = ('Elephant' ,  'Rhino' ,  'Wolf',)

print(animals[0])
print(animals[0:3])
print(len(animals))


## We can also convert tuple, lists and string into each other.

name = 'Shyam'
name = list(name)
print(name)

name = tuple(name)
print(name)
