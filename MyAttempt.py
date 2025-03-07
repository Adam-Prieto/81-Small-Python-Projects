import random, datetime

def generateNumBirthdays(num):
    birthdays = []

    for i in range(num):
        temp = datetime.date(2001, 1, 1)
        seed = datetime.timedelta(random.randint(1, 364))
        birthdays.append(temp + seed)
    return birthdays

def checkMatch(birthdays):
    dates = {}
    for birthday in birthdays:
        if birthday in dates:
            return True  # Found a match
        dates[birthday] = True  # Store the birthday as a key in the dictionary
    return False  # No match found

def runExperiment():
    print('''Please enter a number to represent the total number of people.
        Please ensure that your number is less than 100''')
    numPeople = int(input(">"))

    while numPeople < 0 or numPeople > 100:
        print('''Please ensure that your number is between 1 and 100.''')
        numPeople = int(input(">"))

    birthdays = generateNumBirthdays(numPeople)

    if checkMatch(birthdays):
        print("Yay! There are shared birthdays in your group.")
    else:
        print("Sorry, there are no shared birthdays in your group.")

    print(f"\nNow let's see how many people share birthdays in a group of {numPeople} people.")
    print("We're going to brute force this answer by running the experiment 100,000 times.")
    print("This is called Monte Carlo experimentation (running many trials).")

    input("\nPress Enter to continue...")


    shares = 0
    for i in range(100_000):
        if i % 10_000 == 0 and i > 0:
            print(i, 'simulations run...')
        birthdays = generateNumBirthdays(numPeople)
        if checkMatch(birthdays):
            shares += 1

    percentage = round(shares / 100_000 * 100, 2)

    print(f"After 100,000 simulations, {shares} groups contain matches."
          f"\nThis means that there's a {percentage}% chance"
          f" for a group of {numPeople} people to share a birthday.")
    print("That's probably pretty surprising!")

def main():
    print('''Welcome to the Birthday Paradox Experiment!

    As a bit of background, whenever a cohort of people grows, the 
    probability that at least two people share a birthday increases
    dramatically. Probably more than you'd imagine.

    Let's explore this concept in greater detail.''')

    runExperiment()

if __name__ == '__main__':
    main()