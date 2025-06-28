import random

print(random.randrange(1,100))

a = 'rabin'
str(a)
print(a.encode())  #encode converts a normal string into a bytes objects which can be used in data transmision or writing a binary files etc.

class myclass():
  def __len__(self): 
    return 0

myobj = myclass()
print(bool(myobj))

x = 200.0
print(isinstance(x, float))

