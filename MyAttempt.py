"""My Attempt"""

from random import choice

numDigits = 3
numAttempts = 10


def main():
    print(f'''
    Welcome to Bagels!
    The objective of this game is to guess a {numDigits} digit number without repeating characters.

            Here are some clues: 
            When I say:         That means:
              Fermi               One digit is in the right position.
              Pico                One digit is in the wrong position.
              Bagels              There are no correct digits.

            Good luck!
        ''')
    while True:
        playGame()
        user_input = str(input('Play again? (y/n): '))

        if user_input.lower() != 'y':
            print('\nThank you for playing!\nGoodbye')
            return
        print("\n\n\nGAME RESET\n\n\n")


def playGame():
    computerGuess = guessNum()
    numGuesses = 0

    while numGuesses < numAttempts:

        if numAttempts > 1:
            print('''You have {} guesses left.'''.format(numAttempts - numGuesses))
        else:
            print('''You have {} guess left.'''.format(numAttempts - numGuesses))

        digits = str(input("Enter a guess: "))
        print(digits)

        if digits == computerGuess:
            print('''Correct! ''')
            break

        print(checkDigits(computerGuess, digits))

        numGuesses += 1
    print(f"Correct response: {computerGuess}")


def checkDigits(answer, guess):
    response = ""
    for i, j in zip(answer, guess):
        if j not in answer:
            continue
        if i == j:
            response += "Fermi "
            continue
        response += 'Pico '
    if len(response) < 1:
        return "Bagels\n"
    return response + "\n"


def guessNum():
    digits = list('0123456789')
    guess = []

    while len(guess) < numDigits:
        tempChoice = choice(digits)
        guess.append(tempChoice)
        digits.remove(tempChoice)

    return ''.join(guess)


if __name__ == '__main__':
    main()