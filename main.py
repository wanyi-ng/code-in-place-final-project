import random

options = ["rock", "paper", "scissor"]

def main():
    init_game()

def init_game():
    print("Let's play 'Rock, Paper, Scissor'!")
    
    user_input = input("What will you do? ")
    computer_input = random.choice(options)

    print("You played: " + user_input + ".\n" "Computer plays: " + computer_input + ".")

    if user_input == computer_input:
        print("Draw.")
    elif user_input == "rock" and computer_input == "paper" or user_input == "paper" and computer_input == "scissor" or user_input == "scissor" and computer_input == "rock":
        print("You lose. Computer win.")
    elif user_input == "rock" and computer_input == "scissor" or user_input == "paper" and computer_input == "rock" or user_input == "scissor" and computer_input == "paper":
        print("You win. Computer lose.")

main()