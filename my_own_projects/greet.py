import sys
import argparse

# We use argparse.ArgumentParser() to create a container which specifies what the argument does. It describes what argument program accepts. 
# What we write inside argparse.ArgumentParser(--here--) is shown when we run --help. prog='ProgramName' is used to show a name of our program whose default value is your filename. description = 'The description of waht your program does.'. epilog='The epilog that you want to show on the bottom of the help page.' 
parser = argparse.ArgumentParser(prog='GreetBot',description='This little bot greets users with their name and age.',epilog='')

#parser.add_argument('argument_name') is used to tell the parser what argument script accepts.
parser.add_argument('--name')
parser.add_argument('--age', type = int)

#args = parser.parse_args() this is where the parser actually reads and processes the arguments the user gave from the command line and returns them as an object.
args = parser.parse_args()

print(f'Hello {args.name}. You are {args.age} years old.')
