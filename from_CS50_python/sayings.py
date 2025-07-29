#This file is created to learn how to import functions we created into another file.

def main():
    hello("World!")
    goodbye("World!")

def hello(name):
    print(f"Hello, {name}")

def goodbye(name):
    print(f"Goodbye, {name}")

#This if condition allows us to only run main function is we are running this file not while importing functions into another project
if __name__ == "__main__":
    main()



