from random import shuffle

# Set up constants
HEARTS = chr(9829)
DIAMONDS = chr(9830)
CLUBS = chr(9824)
SPADES = chr(9827)
SUITS = (HEARTS, DIAMONDS, CLUBS, SPADES)
BACKSIDE = 'backside'

MONEY = 5000


def get_bet():
    """Prompt user for a valid bet."""
    while True:
        try:
            print(f"Please enter your bet from the following range: Bet range 1-{MONEY}")
            bet = int(input('> '))
            if 1 <= bet <= MONEY:
                return bet  # Valid bet, return it
            else:
                print(f"Bet must be between 1 and {MONEY}. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a valid number for the bet.")


def generate_deck():
    """Generate and shuffle a deck of cards."""
    deck = []
    for suit in SUITS:
        for i in range(2, 11):
            deck.append([str(i), suit])
        for face in ('J', 'Q', 'K', 'A'):
            deck.append([face, suit])
    shuffle(deck)
    return deck


def get_hands(deck):
    """Deal two cards each to the player and dealer."""
    player_hand = [deck.pop(), deck.pop()]
    dealer_hand = [deck.pop(), deck.pop()]
    return player_hand, dealer_hand


def get_hand_value(cards):
    """Calculate the value of a hand of cards."""
    value = 0
    num_aces = 0

    for card in cards:
        if card[0] in ('J', 'Q', 'K'):
            value += 10
        elif card[0] == 'A':
            num_aces += 1
        else:
            value += int(card[0])

    for _ in range(num_aces):
        value += 10 if value + 10 <= 21 else 1

    return value


def show_cards(cards):
    """Display the cards in a human-readable format."""
    rows = ['', '', '', '', '']

    for card in cards:
        rank, suit = card if card != BACKSIDE else ('##', ' ')  # Handle the backside case
        rows[0] += '____'
        rows[1] += f'|{rank.ljust(2)} |'
        rows[2] += f'| {suit} |'
        rows[3] += f'|_{rank.rjust(2, "_")}| '

    print('\n'.join(rows))


def display_hands(player_hand, dealer_hand, show_dealer_hand):
    """Display both player and dealer hands."""
    if show_dealer_hand:
        print("\nDealer's Hand:")
        show_cards(dealer_hand)
        print(f'Value: {get_hand_value(dealer_hand)}')
    else:
        print("\nDealer's Hand:")
        show_cards([BACKSIDE, dealer_hand[1]])

    print("\n\nYour Hand:")
    show_cards(player_hand)
    print(f'Value: {get_hand_value(player_hand)}')


def calc_winner(player_hand, dealer_hand, deck):
    """Determine the winner of the game."""
    while get_hand_value(dealer_hand) < 17:
        dealer_hand.append(deck.pop())

    display_hands(player_hand, dealer_hand, show_dealer_hand=True)

    player_score = get_hand_value(player_hand)
    dealer_score = get_hand_value(dealer_hand)

    if player_score > 21:
        return 'Loss'
    elif dealer_score > 21 or player_score > dealer_score:
        return 'Win'
    elif player_score == dealer_score:
        return 'Tie'
    else:
        return 'Loss'


def get_player_move():
    """Get the player's choice for their next move."""
    print('Please select an option for this hand:\n(H)it, (S)tand, (D)ouble Down')
    choice = input('> ').upper()

    while choice not in ('H', 'S', 'D'):
        print('Please select a valid option:\n(H)it, (S)tand, (D)ouble Down')
        choice = input('> ').upper()

    return choice


def play_match():
    """Play a single round of Blackjack."""
    player_bet = get_bet()
    deck = generate_deck()
    player_hand, dealer_hand = get_hands(deck)

    print('Bet accepted.\nHere are the starting hands.')
    display_hands(player_hand, dealer_hand, show_dealer_hand=False)

    choice = get_player_move()
    result = ''
    global MONEY

    if choice == 'D':
        if player_bet * 2 <= MONEY:
            player_bet *= 2
            player_hand.append(deck.pop())
            print(f"Your bet is now {player_bet}. One more card.")
            result = calc_winner(player_hand, dealer_hand, deck)
        else:
            print("Insufficient funds for Double Down!")

    while choice == 'H':
        player_hand.append(deck.pop())

        # Player busts, end game immediately
        if get_hand_value(player_hand) > 21:
            display_hands(player_hand, dealer_hand, show_dealer_hand=True)
            MONEY -= player_bet
            print(f'Remaining money: {MONEY}')
            if MONEY == 0:
                return 'Bust'

        display_hands(player_hand, dealer_hand, show_dealer_hand=False)
        choice = get_player_move()

    if choice == 'S':
        display_hands(player_hand, dealer_hand, show_dealer_hand=True)
        result = calc_winner(player_hand, dealer_hand, deck)

    if result == 'Loss':
        print(f'You lose.\nNew score: {MONEY - player_bet}')
        MONEY -= player_bet
        if MONEY == 0:
            return 'Bust'
    elif result == 'Win':
        print(f'You Win!\nNew score: {MONEY + player_bet}')
        MONEY += player_bet
    elif result == 'Tie':
        print(f'Draw. Bet is returned.\nNew Score: {MONEY + player_bet}')
        MONEY += player_bet


def main():
    """Run the main game loop."""
    print('''Welcome to Blackjack!

    The goal of the game is to get as close to 21 without
    going over.''')

    while True:
        has_busted = play_match()

        if has_busted == 'Bust':
            print('You lost all your money. Goodbye!')
            return

        print("Play again? (Y/N)")
        choice = input('> ').upper()
        if choice != 'Y':
            break

    print('Thank you for playing!')


if __name__ == '__main__':
    main()
