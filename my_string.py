name = input("Enter your name: ")


#This + sign is an concatination sign which only adds these two things i.e a string 'Hello, ' and a variable name storing a string.
print("Hello, " + name)


#This , adds a variable, name storing a string with a whitespace between the string 'Hello, ' and name. 
print("Hello, " + name)


#f inside the print indicates this print function is an formatted print function and inside of the open and close curly braces {} is a variable or may be any operations like {3+4} which prints the result of the operation.
print(f"Hello, {name}")


# strip is again another function which removes whitespaces in either left or right side from the passed string
name = name.strip()
print(f"Hello, {name}")


# capitalize is another function which capitalizes the first letter of the passed string. 
name = name.capitalize()
print(f"Hello, {name}")


# We can also add both functions (chaining multiple functions) using code:
name = name.strip().capitalize()
print(f"Hello, {name}")


# title function can be used to capitalize name/title of any organizations. It differs from capitalize as it can capitalize other letters other than the first letter of first Word
name = name.title()
print(f"Hello, {name}")


# short way to do what we did previously
name = input("Enter your name: ").strip().title()
print(f"Hello, {name}")


# split function splits a string into multiple sub strings and in python we can also pass two data into two variables at same time 
first, last = name.split(" ")
print(f"First Name: {first}\nLast Name: {last}")
