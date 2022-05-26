#!/usr/bin/env python3

import random

stages=['''
           +----+
           |    |
                |
                |
                |
                |
        ============''',
        '''
           +----+
           |    |
           O    |
                |
                |
                |
        ============''',
        '''
           +----+
           |    |
           O    |
           |    |
                |
                |
        ============''',
        '''
           +----+
           |    |
           O    |
           |\   |
                |
                |
        ============''',
        '''
           +----+
           |    |
           O    |
          /|\   |
                |
                |
        ============''',
        '''
           +----+
           |    |
           O    |
          /|\   |
          /     |
                |
        ============''',
        '''
           +----+
           |    |
           O    |
          /|\   |
          / \   |
                |
        ============''']

words=['able',
'about',
'account',
'acid',
'across',
'act',
'addition',
'adjustment',
'advertisement',
'after',
'again',
'against',
'agreement',
'air',
'all',
'almost',
'among',
'amount',
'amusement',
'and',
'angle',
'angry',
'animal',
'answer',
'ant',
'any',
'apparatus']


def game():
        
        chosen_word=random.choice(words)
        letters=list(chosen_word)
        guessed_letters=[]
        in_game_word=[]

        tries=0
        for i in range(0,len(letters)):
                in_game_word.append(" ")

        while tries<6:
                input_letter=input("Type a letter: ")

                if input_letter in letters and input_letter not in guessed_letters:
                        guessed_letters.append(input_letter)
                else:
                        tries+=1
                
                for i in range(0,len(letters)):
                        if letters[i] in guessed_letters:
                                in_game_word[i]=letters[i]
                        else:
                                in_game_word[i]="_"
                
                print(' '.join(in_game_word))
                if in_game_word==letters:
                        print(stages[tries])
                        play=input("You Won!!!🌈 Play again[y/n] ")
                        if play=='n'.lower():
                                play_again=False
                        break
                else:
                        print(stages[tries])
        if tries==6:
                print(' '.join(in_game_word))
                print(stages[tries])
                play=input("You lost!💀 Play again?[y/n] ")
        if play=='n'.lower():
                play_again=False

game()




