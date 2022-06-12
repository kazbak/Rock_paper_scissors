import random
from secrets import choice

print("Welcome! Let's play a game")
print("Rock, Paper, Scissors\n")
print("RULES OF THE GAME")
print("Rock beats Scissors\nPaper beats Rock\nScissors beats Paper\n")
print("'r'for'rock' 's' for scissors' 'p' for paper\n")

playing = True

while playing:
    user_input = input("Enter your choice ('r', 'p', 's'): ").lower ()

    if user_input == "r":
        player_action = "rock"

    elif user_input == "p": 
        player_action = "paper"
    
    elif user_input == "s":
        player_action = "scissor"

    else:
        print("Invalid input entered, try again")
        continue    
    
    game_options = ["rock", "paper", "scissor"] 

    CPU_action = random.choice(game_options)          

    print(f"\nPlayer({player_action}), CPU({CPU_action})\n")

    if player_action == CPU_action:
        print(f"Both players chose {player_action}. It's a tie!\n")

    elif user_input == "r":
        if CPU_action == "scissor":
            print("Rock beats scissors! You win!\n")
        else:
            print("Paper beats rock! You lose!\n")

    elif user_input == "p":
        if CPU_action == "rock":
            print("Paper beats rock! You win!\n")
        else:
            print("Scissors beats paper! You lose!\n")

    elif user_input == "s":
        
        if CPU_action == "paper":
            print("Scissors beats paper! You win!\n")
        else:
            print("Rock beats scissors! You lose!\n")

    choice = input("Play again? (y/n): ").lower()
    if choice =="y":
        pass
        
    if choice == "n": 
        playing = False
        print("Thanks for playing, bye!")









