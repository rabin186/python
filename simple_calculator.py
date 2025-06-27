def operation():
    global x, y, sign, result
    x = float(input("Enter 1st operator: "))
    y = float(input("Enter 2nd operator: "))
    result = 0
    print(f"Operations that can be performed:\n1. +\n2. -\n3. *\n4. /\n5. %")
    sign = input("Choose the operation (sign) you want to perform: ")
    match sign:
        case '+':
            result = x+y
        case '-':
            result = x-y
        case '*':
            result = x*y
        case '/':
            result = x/y
        case '%':
            result = x%y
        case _:
            print("Not a valid operation!")
    print(f'Result: {result}')

def is_even():
    x = int(input("Enter the value: "))
    if x % 2 == 0:
        print(f"{x} is even.")
    else:
        print(f"{x} is odd.")

def write():
    f = open('history.txt' , 'a', encoding="utf-8")
    problem = str(f'{x} {sign} {y} = {result}\n')
    f.write(problem)
    f.close()

def read():
    with open('history.txt', encoding="utf-8") as f:
        read_data = f.read()
        print(read_data)

def main():
    print("Simple Calculator")
    global i
    i = 0
    while(i != 4):
        print("Choose what you want to do:")
        i = int(input("1. Perform a Operation\n2. Find odd or even\n3. View History\n4. Exit\n"))
        match i:
            case 1:
                operation()
                write()
            case 2:
                is_even()
            case 3:
                read()
            case 4:
                print("Exiting..")
            case _:
                print("Not a valid choice!")



main()
