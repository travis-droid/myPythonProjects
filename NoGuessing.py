import random
print('''
=============================================================================================
==============================NUMBER GUESSING GAME===========================================
=============================================================================================
#############################################################################################
=====================================GOOD LUCK===============================================
''')
name = input('Enter your name: ')
print(f'\nHello {name}, Welcome to the Number Guessing Game\n')
print('You have 7 chances to guess the correct number\n\n')

low = int(input('Enter the lower bound: '))
high = int(input('Enter the higher bound: '))

print(f'\nGuess the corrent number in the range of {low} and {high}.\n')

num = random.randint(low, high)
chance = 7
guess = 0

while guess < chance:
    guess +=1
    Guess = int(input('Enter your Guess: '))

    if Guess == num:
        print(f'\nYou have guessed the number correctly! The number is {num}. You guessed it in {guess} attempts!')
        break
    elif guess >= chance and Guess != num:
        print(f'Sorry the number was {num}, Better luck next time')
    elif Guess > num:
        print('The number is to high, Try a lower number')
    elif Guess < num:
        print("The number is too low, try a Higher number")

