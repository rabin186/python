def operation():
    global num1, num2, sign, result
    num1 = float(input("Enter 1st operator: "))
    num2 = float(input("Enter 2nd operator: "))
    result = 0
    print(f"Operations that can be performed:\n1. +\n2. -\n3. *\n4. /\n5. %\n6. ^")
    sign = input("Choose the operation (sign) you want to perform: ")
    match sign:
        case '+':
            result = num1+num2
        case '-':
            result = num1-num2
        case '*':
            result = num1*num2
        case '/':
            result = num1/num2
        case '%':
            result = num1%num2
        case '^':
            result = pow(num1,num2)
        case _:
            print("Not a valid operation!")
    print(f'Result: {result}')

def is_even():
    num1 = int(input("Enter the value: "))
    if num1 % 2 == 0:
        result = f"{num1} is even."
    else:
        result = f"{num1} is odd."
    return result


def write():
    f = open('history.txt' , 'a', encoding="utf-8")
    problem = str(f'{num1} {sign} {num2} = {result}\n')
    f.write(problem)
    f.close()

def write_isEven(text):
    f = open('history.txt' , 'a' , encoding="utf-8")
    problem = str(f'{text} \n')
    f.write(problem)
    f.close()


def read():
    with open('history.txt', encoding="utf-8") as f:
        read_data = f.read()
        print(read_data)

def main():
    print("Simple Calculator")
    global choice
    choice = 0
    while(choice != 4):
        print("Choose what you want to do:")
        choice = int(input("1. Perform a Operation\n2. Find odd or even\n3. View History\n4. Exit\n"))
        match choice:
            case 1:
                operation()
                write()
            case 2:
                result = is_even()
                print(result)
                write_isEven(result)
            case 3:
                read()
            case 4:
                print("Exiting..")
            case _:
                print("Not a valid choice!")


if __name__ == "__main__":
    main()
