import random

def display_board(board):
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.
    print()
    for row in range(3):
        print("+-------" * 3 + "+")
        print(("|" + " " * 7) * 3 + "|")
        for column in range(3):
            print("|   " + str(board[row][column]) + "   ", end = "")
        print("|")
        print(("|" + " " * 7) * 3 + "|")
    print("+-------" * 3 + "+")


def enter_move(board):
    # The function accepts the board's current status, asks the user about their move, 
    # checks the input, and updates the board according to the user's decision.
    move_complete = False

    while move_complete == False:    
        try:
            new_move = int(input("Enter your move:"))
            if new_move > 9 or new_move < 0:
                raise ValueError
            new_move_row = (new_move - 1) // 3
            new_move_column = (new_move - 1) % 3
            new_placement = (new_move_row, new_move_column)
            if new_placement in make_list_of_free_fields(board):
                board[new_move_row][new_move_column] = "O"
                move_complete = True
            else:
                print("That placement is already taken.  Please try again.")
                print()
        except ValueError:
            print("Invalid number.  Please enter a number from 0 through 9.")
        except:
            print("Invalid value.  Please enter an integer from 0 through 9.")
        
        



def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares; 
    # the list consists of tuples, while each tuple is a pair of row and column numbers.
    free_spots = []
    for row in range(3):
        for item in range(3):
            if board[row][item] != "O" and board[row][item] != "X":
                free_spots.append((row, item))
    
    return free_spots


def victory_for(board):
    # The function analyzes the board's status in order to check if 
    # the player using 'O's or 'X's has won the game
    o_win = False
    x_win = False

    # Check full rows for the same entries
    for row in range(3):
        if board[row][0] == "X" and board[row][1] == "X" and board[row][2] == "X":
            x_win = True
        if board[row][0] == "O" and board[row][1] == "O" and board[row][2] == "O":
            o_win = True

    # Check full columns for the same entries
    for column in range(3):
        if board[0][column] == "X" and board[1][column] == "X" and board[2][column] == "X":
            x_win = True
        if board[0][column] == "O" and board[1][column] == "O" and board[2][column] == "O":
            o_win = True
    
    # Check diagonals for the same entries
    if (board[0][0] == "X" and board[1][1] == "X" and board[2][2] == "X") or (board[0][2] == "X" and board[1][1] == "X" and board[2][0] == "X"):
        x_win = True    
    if (board[0][0] == "O" and board[1][1] == "O" and board[2][2] == "O") or (board[0][2] == "O" and board[1][1] == "O" and board[2][0] == "O"):
        o_win = True

    if x_win == True:
        return "X"
    else:
        if o_win == True:
            return "O"
        else:
            return None
    


def draw_move(board):
    # The function draws the computer's move and updates the board.
    move_complete = False
    
    while move_complete == False:
        rand_row = random.randint(0,2)
        rand_column = random.randint(0,2)

        new_placement = (rand_row, rand_column)
        if new_placement in make_list_of_free_fields(board):
            board[rand_row][rand_column] = "X"
            move_complete = True

board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
who_won = None

while True:
    draw_move(board)
    who_won = victory_for(board)
    if who_won != None:
        break
    # End game if all spots are filled
    free_spaces = make_list_of_free_fields(board)
    if len(free_spaces) == 0:
        break
    display_board(board)
    enter_move(board)
    who_won = victory_for(board)
    if who_won != None:
        break

display_board(board)
if who_won == "O":
    print("You won!")
else:
    if who_won == "X":
        print("Computer won!")
    else:
        print("It's a CAT!")
