import random

name = input("Enter your name: ")
print("\nGood luck", name)

words = [
        'rainbow', 'computer', 'science', 'programming',
         'python', 'mathematics', 'player', 'condition',
         'reverse', 'water', 'board', 'geeks'
]

word = random.choice(words)

print('\nGuess the characters!')

guesses = ''
turns = len(word)

while turns > 0:
    fails = 0
    for char in word:
        if char in guesses:
            print(char, end=' ')
        else:
            print('_')
            fails += 1
    if fails == 0:
        print('\nYou won')
        print("\nThe word is: ", word)
        break

    print()
    guess = input("\nGuess a character: ")
    guesses += guess

    if guess not in word:
        turns -= 1
        print('Wrong! You have ', turns, 'more turns!')

    if turns < 0:
        print("YOU LOST!")
        print('\nEND OF THE GAME')