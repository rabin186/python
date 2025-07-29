x = "Let's try slicing in python."

print(x)
print(x[4:11]) #11th index isn't included.

#negative Slicing
print(x[-14:-9]) #14 isn't included 
if "try" in x:
    print("Try is available.")

else:
    print("Try not available.")

#Modifying strings
#1. Replace String
print(x.replace("L" , "l"))

#2. Split String
print(x.split("i"))
