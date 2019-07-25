#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 24 11:40:58 2019

@author: awesome_k
"""

import random
import time

myScore = 0
compScore = 0
draw = 0

rps = ['r', 's', 'p']

playAgain = 'y'

while playAgain == 'y':
    myChoice = input('Make a move! r/s/p')
    compChoice = random.choice(rps)

    if myChoice[0].lower() == compChoice:
        print('Draw!')
        time.sleep(2)
        draw = draw + 1
    elif myChoice[0].lower() == 'r' and compChoice == 's':
        print('You chose rock and the computer chose scissors. You win!')
        time.sleep(2)
        myScore = myScore + 1
    elif myChoice[0].lower() == 'r' and compChoice == 'p':
        print('You chose rock and the computer chose paper. You lose!')
        time.sleep(2)
        compScore = compScore + 1
    elif myChoice[0].lower() == 'p' and compChoice == 'r':
        print('You chose paper and the computer chose rock. You win!')
        time.sleep(2)
        myScore = myScore + 1
    elif myChoice[0].lower() == 'p' and compChoice == 's':
        print('You chose paper and the computer chose scissors. You lose!')
        time.sleep(2)
        compScore = compScore + 1
    elif myChoice[0].lower() == 's' and compChoice == 'r':
        print('You chose scissors and the computer chose rock. You lose!')
        time.sleep(2)
        compScore = compScore + 1
    elif myChoice[0].lower() == 's' and compChoice == 'p':
        print('You chose scissors and the computer chose paper. You win!')
        time.sleep(2)
        myScore = myScore + 1
    else:
        print('Invalid entry.')
        time.sleep(2)

    playAgain = input('Do you want to play again? (y/n)')
    if playAgain == 'n':
        print('Thanks bye!')
    if playAgain == 'sc':
        print('Human ' + str(myScore), 'Computer ' + str(compScore), 'Draw ' + str(draw))