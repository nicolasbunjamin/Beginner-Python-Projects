# shoutout to Aaron Bernath (Clever Programmer) for inspiration (https://www.youtube.com/watch?v=BHh654_7Cmw)

from random import randint
board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
player = ""
winner = None
tie = False

def play_game():
    randomize_turn()
    display_board()
    while winner == None and tie == False:
        turn()
        display_board()
        check_win()
        check_tie()
        switch_turns()

def randomize_turn():
    global player
    order = randint(0,1)
    if order == 1:
        #computer goes first
        player = "X"
        print ("Mr. Python will go first.")
    elif order == 0:
        #user goes first
        player = "O"
        print ("You will go first.")
    
def turn():
    global player
    position = int()
    
    # if it's computer's turn (X), choose random position
    if player == "X":
        
        # prevent overwriting by computer
        position = randint(0, 8)
        while board[position] == "O" or board[position] == "X":
            position = randint(0, 8)
        board[position] = "X"
        print ("")
        print ("Mr. Python chose " + str(position + 1))
     
    # if it's user's turn (O), input position of choice
    elif player == "O":
        
        # prevent invalid input value
        choice = input("Choose a position on the board: ")
        while choice not in \
            ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            choice = input("You can't do that. Choose again: ")
        
        # prevent overwriting by user
        position = int(choice) - 1
        while board[position] == "X" or board[position] == "O": 
            choice = input("You can't do that. Choose again: ")
            position = int(choice) - 1
        board[position] = "O"
        
def display_board():
    print ("")
    print (board[0], board[1], board[2])
    print (board[3], board[4], board[5])
    print (board[6], board[7], board[8]) 
       
def check_win():
    global winner
    # note to self: simplify this later
    r_1 = board[0] == board[1] == board[2] 
    r_2 = board[3] == board[4] == board[5] 
    r_3 = board[6] == board[7] == board[8] 
    c_1 = board[0] == board[3] == board[6] 
    c_2 = board[1] == board[4] == board[7] 
    c_3 = board[2] == board[5] == board[8] 
    d_1 = board[0] == board[4] == board[8]
    d_2 = board[2] == board[4] == board[6]
    if any([r_1, r_2, r_3, c_1, c_2, c_3, d_1, d_2]):
        if player == "X":
            winner = "X"
            print ("")
            print ("Mr. Python wins!")
        elif player == "O":
            winner = "O"
            display_board()
            print ("")
            print ("Congratulations! You win!")
        
def check_tie():
  global tie
  tie = all([cell == "X" or cell == "O" for cell in board])
  if winner == None and tie == True:
      print ("It's a tie!")            
        
def switch_turns():
    global player
    if player == "X":
        player = "O"
    elif player == "O":
        player = "X"  
        
play_game()
