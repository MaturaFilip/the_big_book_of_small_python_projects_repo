"""This is recreate Bagels game"""

import random

# constants
MAX_ROUNDS = 10
NUM_DIGITS = 3


# main game
def main():
    while True: # main game loop
        # store secret random number
        secret_number = get_secret_number()

        print(f'Guess the number')
        print(f'You will have {MAX_ROUNDS} guesses.')

        num_guesses = 1
        while num_guesses <= MAX_ROUNDS:
            guess = ''
            # get valid guess
            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print(f'Guess #{num_guesses}')
                guess = input('> ')

            clues = get_clues(guess, secret_number)
            print(clues)
            num_guesses += 1

            if guess == secret_number:
                break # correct answer
                
            if num_guesses > MAX_ROUNDS:
                print('You are out of guesses.')
                print(f'The answer was {secret_number}')

        # ask player if they want to play again
        print('Do you want to play again? (yes or no)')
        if not input('> ').lower().startswith('y'):
            break
    print('Thanks for playing!')

    




# get random secret digit (length based on constant NUM_DIGITS)
def get_secret_number():
    numbers = list('1234567890')
    random.shuffle(numbers) # mutable
    secret_numbers = ''
    for i in range(NUM_DIGITS):
        secret_numbers += str(numbers[i])
    return secret_numbers



    



# get clues for player (compare secret number with guess)
def get_clues(guess, secret_number):
    if guess == secret_number:
        return "You're right!"
    
    clues = []

    for i in range(len(guess)):
        if guess[i] == secret_number[i]:
            clues.append('Fermi')
        elif guess[i] in secret_number:
            clues.append('Pico')
    if len(clues) == 0:
        return 'Bagels'
    else:
        clues.sort()
        return ' '.join(clues)


if __name__ == '__main__':
    main()