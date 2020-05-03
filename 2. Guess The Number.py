from random import randint

random_int = int()
guessed_int = int()
wrong_int = []
lower_limit = 1
upper_limit = 99

def play_game():
    intro()
    generate_random()
    while guessed_int != random_int:
        take_input()
    
def intro():
    print ("Welcome to the game!")
    print ("Mr. Python has come up with a random number from " + str(lower_limit) + " to " + str(upper_limit))

def generate_random():
    global random_int 
    random_int = randint(lower_limit,upper_limit)
    
def take_input():
    global random_int
    global guessed_int
    global lower_limit
    global upper_limit
    global wrong_int
    inputted_int = input("Please guess Mr. Python's number: ")
    possible_ans = [str(x) for x in list(range(lower_limit,upper_limit+1))]
    while inputted_int not in possible_ans:
        inputted_int = input("That's an invalid answer. Guess again: ")
    while int(inputted_int) in wrong_int:
        inputted_int = input("You've tried that one. Guess again: ")
    guessed_int = int(inputted_int)
    if random_int == guessed_int:
        print ("Congratulations! You can read minds.")
    else:
        wrong_int.append(guessed_int)
        if random_int > guessed_int:
            print ("Guess highter.")
        elif random_int < guessed_int:
            print ("Guess lower.")

play_game()