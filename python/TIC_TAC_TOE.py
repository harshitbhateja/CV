#Creating a tic-tac-toe board for game
board = [" " for i in range(9)]

#Defining a function to show the board
def list_board():
    print()
    print("|{}| |{}| |{}|".format(board[0],board[1],board[2]))    
    print("|{}| |{}| |{}|".format(board[3],board[4],board[5]))
    print("|{}| |{}| |{}|".format(board[6],board[7],board[8]))


#Defining a function for player to play the move 
def player_move(icon):
    if icon == "X":
        player_num = "Player 1"
    else:
        player_num = "Player 2"
    print("your turn "+player_num)
    pos = int(input("enter your value (1-9)"))
    if board[pos-1] == " ":
        board[pos-1] = icon
    else:
        print("Space occupied")
        player_move(icon)

#defining the function to check if any player won
def isvictory(icon):
    if (board[0] == icon and board[1] == icon and board[2] == icon) or\
       (board[3] == icon and board[4] == icon and board[5] == icon) or\
       (board[6] == icon and board[7] == icon and board[8] == icon) or\
       (board[0] == icon and board[3] == icon and board[6] == icon) or\
       (board[1] == icon and board[4] == icon and board[7] == icon) or\
       (board[2] == icon and board[5] == icon and board[8] == icon) or\
       (board[0] == icon and board[4] == icon and board[8] == icon) or\
       (board[6] == icon and board[4] == icon and board[2] == icon):
        return True
    else:
        return False

 #()=>To check the match is draw or not
       
def isdraw():
    if " " not in board:
        return True
    else:
        return False
        
#Game started    

while True:
    
    list_board()
    player_move("O")
    if isvictory("O"):
        print("Player 2 winner")
        break
    elif isdraw():
        print("DRAW MATCH")
        list_board()
        break
    list_board()
    player_move("X")
    
    if isvictory("X"):
        print("Player 2 winner")
        list_board()
        break
    elif isdraw():
        print("DRAW MATCH")
        list_board()
        break
    
    
    
    
