#!/usr/bin/env python3
import random
cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
playing=True

while playing:
    playing = input("Do you want to play a game of blackjack? (y/n): ").lower()

    if playing=='n':
        break
    else:
        computer_cards=[]
        computer_cards.append(random.choice(cards))
        computer_cards.append(random.choice(cards))

        player_cards=[]
        player_cards.append(random.choice(cards))
        player_cards.append(random.choice(cards))

        print(f"Your cards: {player_cards}, current score: {sum(player_cards)}")
        print(f"Computer's first card: {computer_cards[0]}")
       
        while sum(player_cards)<=21:
            another_card=input("Type 'y' to get another card, type 'n' to pass: ").lower()
            if another_card=='y':
                player_cards.append(random.choice(cards))
            else:
                break

            print(f"Your cards: {player_cards}, current score: {sum(player_cards)}")
            print(f"Computer's first card: {computer_cards[0]}")
        
        final_player_cards=sum(player_cards)

        while sum(computer_cards)<=17:
            computer_cards.append(random.choice(cards))
        
        final_computer_cards=sum(computer_cards)
        if final_computer_cards>21:
            print("You win 🏆")
            print(f"Your score: {final_player_cards}")
            print(f"Your oponent score: {final_computer_cards}")
        elif final_player_cards>21:
            print("You lost 💀")
            print(f"Your score: {final_player_cards}")
            print(f"Your oponent score: {final_computer_cards}")
        elif final_player_cards==final_computer_cards:
            print("It's a tie 🌈")
            print(f"Your score: {final_player_cards}")
            print(f"Your oponent score: {final_computer_cards}")
        elif final_player_cards>final_computer_cards and final_computer_cards<21:
            print("You win 🏆")
            print(f"Your score: {final_player_cards}")
            print(f"Your oponent score: {final_computer_cards}")
        elif final_player_cards<final_computer_cards and final_computer_cards<21:
            print("You lost 💀")
            print(f"Your score: {final_player_cards}")
            print(f"Your oponent score: {final_computer_cards}")







