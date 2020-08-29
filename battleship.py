import random


#Building a 5x5 board with an empty list and for loop
board = []

for x in range(0,5):
  board.append(["[ ]"] * 5)

def print_board(board):
  for row in board:
    print (" ".join(row))

#Welcome screen
print("=======================")
print("Welcome to BATTLESHIP!")
print("=======================")

#Ask player 1 and player 2 for their name and save it in a list

player_1 = input("Player 1, what is your name? ")
player_2 = input("Player 2, what your name:? ")
players = [player_1, player_2]

#Define players, randomly assign who goes first
def randomize_player(players):
    return random.choice(players)
    
#Randomly choose battleship location
def randomize_row(board):
  return random.randint(0,len(board)-1)
def randomize_col(board):
  return random.randint(0,len(board[0])-1)

#Randomly choose player
if randomize_player(players) == player_1:
  print(" ")
  print(player_1, "will start the game.\n")
else:
  print(" ")
  print(player_2, "will start the game.\n")
  
# 1st ship row and ship column location
ship_row_1 = randomize_row(board)
ship_col_1 = randomize_col(board)

# 2nd ship row and column location
ship_row_2 = randomize_row(board)
ship_col_2 = randomize_col(board)

#Call function to print the board
print_board(board)

player_start = randomize_player(players)

#Ask players what row and column they want to choose

hit_count = 0

for turn in range(4):
     guess_row = int(input("Try to find the battleships. \n What row from 0-4 would you like to choose?"))
    
     guess_col = int(input("Try to find the battleships. \n What column from 0-4 would you like to choose?"))


     

#If the player correctly guesses the column and row
     if (guess_row == ship_row_1 and guess_col == ship_col_1) or (guess_row == ship_row_2 and guess_col == ship_col_2):
            hit_count = hit_count + 1
            board[guess_row][guess_col] = "*"
            print ("Congratulations! ")
            if hit_count == 1:
                   print("You sunk the first battleship!") 
            elif hit_count == 2:
                   print("You sunk the second battleship! You win!")
                   print_board(board)
                   break

#If the player guesses the wrong column and row, or if they have repeated a previous answer
     else:
            if (guess_row < 0 or guess_row > 4)  or (guess_col < 0 or guess_col > 4):
                   print ("Sorry wrong area. Choose again: ")
            elif(board[guess_row][guess_col] == "X"):
                   print ("You have already guessed this coordinate.")
            else:
                 print ("You did not guess any of the battleships. Next player.")
                 board[guess_row][guess_col] = "X"
            print (turn + 1, "turn")
     print_board

#Give the players the location of the ships
print ("Ship 1 got away!They were hiding in this location:")    
print (ship_row_1, ship_col_1) 

print ("Ship 2 got away!They were hiding in this location:")    
print (ship_row_2, ship_col_2)
