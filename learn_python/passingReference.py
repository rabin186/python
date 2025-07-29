def func(some_parameter):
    some_parameter.append('Hello')

spam = [1, 2, 3]
func(spam)
print(spam)

## NOTE: In python, if we pass an Mutable object like list, dictionary to a function, python doesn't pass the actual object neither copy the object instead passes an reference to the same object in memory.

## In this example, when we call func(spam), the function parameter some_parameter becomes another name for the same list spam.

