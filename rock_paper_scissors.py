import random

while True:
    user = input("Enter your choice (Rock(r) , Paper(p) , Scissors(s)) : ")
    computer = random.choice([0 , 1 , -1])
    values = {'r' : 0 , 'p' : 1 , 's' : -1}
    user_value = values[user]
    default_values = {0 : 'Rock' , 1 : 'Paper' , -1 : 'Scissors'}

    print(f"Your choice : {default_values[user_value]} \nComputer choice : {default_values[computer]}")

    if user_value == computer:
        print("It's a tie")
    else:
        if( (user_value == 1 and computer == 0) or (user_value == 0 and computer == -1) or (user_value == -1 and computer == 1)):
            print("You win")
        else:
            print("You lose")
    exit = input("Do you want to play again (y/n) : ")
    if exit == 'n':
        break