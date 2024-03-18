def instructions_yes_no(question):
    while True:
        instructions = input(question).lower()

        # Lists of valid responses
        yes = ["yes", "y", "yea", "yeah", "ya"]
        no = ["no", "n", "nope", "na", "never"]

        if instructions in yes:
            print('''
            
**** Instructions ****

To begin, decide on a score goal (eg: The first one to get a score of 50 wins).

For each round of the game, you win points by rolling dice. The winner of the round is the one who gets 13 (or slightly
less).

If you win the round, then your score will increase by the number of points that you earned.

If your first roll of two dice is a double (eg: both dice show a three), then your score will be DOUBLE the number of
points.

If you lose the round, then you don't get any points.

If you and the computer tie (eg: you both get a score of 11, then you will have 11 points added to your score).

Your goal is to try to get to the target score before the computer.

Good luck.

            ''')
            return "yes"

        elif instructions in no:
            print("You choose not to read the instructions")
            return "no"

        else:
            print("please enter yes / no")


def roll_yes_no(question):
    while True:

        roll_again = input(question).lower()

        yes = ["yes", "y", "yea", "yeah", "ya"]
        no = ["no", "n", "nope", "na", "never"]

        if roll_again in yes:
            print("Rolls again")
            return "yes"

        elif roll_again in no:
            print("does not roll again")
            return "no"

        else:
            print("please enter yes / no")


def points(question):
    while True:
        round_number = input(question).lower()

        try:
            num = int(round_number)
            print(f"you chose {num}")
            return round_number

        except ValueError:
            if round_number == "infinite" or round_number == "i":
                print("you chose infinite")
                return "infinite"
        print("Please enter a number 1-10 or 'infinite'")


# main routine
keep_going = ""
while keep_going == "":
    print()
    print("🎲🎲Roll it Thirteen🎲🎲")
    print()

    want_instructions = instructions_yes_no("Do you want to read the instructions? ")

    number_rounds = points("How many points do you want to set as the goal? ")

    want_roll = roll_yes_no("do you want to roll again? ")

    print("code continues")

    keep_going = input("Press <Enter> to keep going or any key to quit ")
    print()
    print("thank you for playing roll it 13")
