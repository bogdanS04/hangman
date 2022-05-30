from gamedata import data
from art import logo,vs
import random
import os

def clear():
    return os.system('cls')
playing = True
score=0
while playing:

    print(logo)
    
    if score == 0:
         compare_a=random.choice(data)
         compare_b=random.choice(data)
         while compare_a==compare_b:
             compare_b=random.choice(data)
    
    
    print(f"Your current score is {score}")    

    print(f"Compare A: {compare_a['name']}, a {compare_a['description']}, from {compare_a['country']}")

    print(vs)

    print(f"Compare B: {compare_b['name']}, a {compare_b['description']}, from {compare_b['country']}")

    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    if compare_a['follower_count']>compare_b['follower_count'] and guess=='a':
        compare_a=compare_b
        compare_b=random.choice(data)
        score+=1
        clear()
    elif compare_a['follower_count']<compare_b['follower_count'] and guess=='b':
        compare_a=compare_b
        compare_b=random.choice(data)
        score+=1
        clear()
    else:
        clear()
        print(logo)
        print(f"You lost, your score is: {score}")
        playing=False



