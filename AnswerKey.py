"""Answer Key"""
import random

NUM_DIGITS = 3
MAX_GUESSES = 10


def main():
    print('''Welcome to Bagels, a deductive logic game

    I am thinking of a {}-digit number with no repeated digits.
    Try to guess what it is. Here are some clues: 
    When I say:         That means
       Pico             One digit is correct but in the wrong position.
       Fermi            One digit is correct and in the right position.
       Bagels           No digit is correct.

    For example if the secret number was 248 and your guess what 843, the 
    clues would be: Fermi Pico'''.format(NUM_DIGITS))

    while True:
        # This stores the secret number the player needs to guess.
        secretNum = getSecretNum()
        print('I have thought up a number.')
        print(' You have {} guesses left.'.format(MAX_GUESSES))

        numGuesses = 1
        while numGuesses <= MAX_GUESSES:
            guess = ''
            # Loop until entering a valid guess
            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print('Guess #{}: '.format(numGuesses))
                guess = input('> ')

            clues = getClues(guess, secretNum)
            print(clues)
            numGuesses += 1

            if guess == secretNum:
                break
            if numGuesses > MAX_GUESSES:
                print('You ran out of guesses.')
                print('The secret number was: {}'.format(secretNum))

        # Ask the player if they want to play again
        print('Do you want to play again? (yes/no)')
        if not input('> ').lower().startswith('y'):
            break


def getSecretNum():
    """Returns string of length NUM_DIGITS"""
    numbers = list('123457890')
    random.shuffle(numbers)

    # Get the first NUM_DIGITS digits in the list for the secret number
    secretNum = ''
    for i in range(NUM_DIGITS):
        secretNum += str(numbers[i])
    return secretNum


def getClues(guess, secretNum):
    """Returns a string with pico, fermi, bagels clues for a guess.
    and secret number pair."""
    if guess == secretNum:
        return 'You got this!'

    clues = []

    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            # A correct digit is in the correct place
            clues.append('Fermi ')
        elif guess[i] in secretNum:
            # A correct digit in the incorrect place
            clues.append('Pico ')
    if len(clues) == 0:
        return 'Bagels'
    else:
        # Sort the clues into alphabetical order so their original order
        # doesn't give information away.
        clues.sort()
        # Make a single string from the list of string clues.
        return ''.join(clues)


if __name__ == '__main__':
    main()