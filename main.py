#usr/bin/python3
from random import randint

# A simple rock paper scissors game

still_playing =  True

while still_playing:
    player = input("Rock, Paper, Scissors? (q -> quit)\n")
    options = ["Rock", "Paper", "Scissors"]
    computer = options[randint(0, 2)]

    if player == computer:
        print("Tie!")
    else:
        if player.title == options[0]:
            if computer == options[1]:
                print("You lose! ",computer," beats ",player)
            else:
                print("You win!",player," beats ",computer)
        elif player.title == options[1]:
            if computer == options[2]:
                print("You lose!",computer," beats ",player)
            else:
                print("You win!",player," beats ",computer)
        else:
            if computer == options[0]:
                print("You lose!",computer," beats ",player)
            else:
                print("You win!",player," beats ",computer)
        
    if player == "q":
        still_playing = False
