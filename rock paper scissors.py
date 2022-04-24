import random

user_wins = 0
computer_wins = 0
options = ["rock", "paper", "scissors"]

while True:
    user_input = input("Type in rock, paper, scissors to play or q to quit ")
    
    if user_input == "q":
        break

    if user_input not in options:
        continue

    computer_input = options[random.randint(0,3)]
    print("Computer picked ", computer_input +".")

    if user_input == 'rock' and computer_input == 'scissors':
        print('You won!')
        user_wins += 1

    elif user_input == 'scissors' and computer_input == 'paper':
        print('You won!')
        user_wins += 1

    elif user_input == 'paper' and computer_input == 'rock':
        print('You won!')
        user_wins += 1

    else:
        print("You lost!")
        computer_wins += 1
print("Goodbye")