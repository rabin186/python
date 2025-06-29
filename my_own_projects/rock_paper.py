import random
options = ['Rock','Paper','Scissors']
choice = 0
players_score , computers_score = (0,0)
print("Rock Paper Scissors Game")
print("1. Play\n2. Exit ")
while choice != 2:
    choice = int(input("What do you want to do? "))
    if choice == 1:
        players_choice = input("Enter Your Choice(Rock, Paper, Scissors): ").capitalize()
        computer_choice = random.choice(options)
        print(f"Computers Choice: {computer_choice}")

        match players_choice:
            case 'Rock':
                if computer_choice == 'Rock':
                    print("Draw!")
                elif computer_choice == 'Paper':
                    print("Computer Wins!")
                    computers_score += 1
                elif computer_choice == 'Scissors':
                    print("You Won🥳🥳")
                    players_score += 1

            case 'Paper':
                if computer_choice == 'Paper':
                    print("Draw!")
                elif computer_choice == 'Rock':
                    print("Computer Wins!")
                    computers_score += 1
                elif computer_choice == 'Scissors':
                    print("You Won🥳🥳")
                    players_score += 1

            case 'Scissors':
                if computer_choice == 'Scissors':
                    print("Draw!")
                elif computer_choice == 'Rock':
                    print("Computer Wins!")
                    computers_score += 1
                elif computer_choice == 'Paper':
                    print("You Won🥳🥳")
                    players_score += 1

            case _:
                print("Invalid Choice!")

        print(f"Computers Score: {computers_score}\tPlayers Score: {players_score}")
    elif choice == 2:
        print("Thanks for playing!")
    else:
        print("Invalid choice!")
