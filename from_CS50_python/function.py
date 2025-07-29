x = 'rabin'

# def myFunction():
#     x = 'Acharya'
#     print("My name is Rabin " + x);
#
# myFunction()
#
# print("My name is " + x + " Acharya.");

# global y
y = 5
print(5 + y)

def myfunc():
  global y
  y = "fantastic"

myfunc()

print("python is " + y)
