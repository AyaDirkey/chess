#install windows-curses
#import curses
#scr=curses.initscr()
import os
import copy

import moves
def print_board(board):
    i=1
    print("    A  B  C  D  E  F  G  H\n")
    for row in board:
        print (i , "  ", end="")
        for column in row:
            print(column + "  ", end="")
        i += 1
        print("")

def clear():
        os.system("cls")
    #scr.clear()

#check if the target is empty or occupied by an enemy

def check_terget(board, x1, y1, x2, y2):
    if board[x2][y2] != " ":
        if board[x1][y1].isupper() == board[x2][y2].isupper():
            return False
    return True

def move(board, x1, y1, x2, y2, piece):
    board[x1][y1] = " "
    board[x2][y2] = piece

def clear_and_print(board):
    clear()
    print_board(board)

#-----------------------------------

def check_inbetween_pieces (board,x1,y1,x2,y2):
    x = x1
    y = y1
    dx = 0
    dy = 0
    if x1 < x2:
        dx = 1
    elif x1 > x2:
        dx = -1
    if y1 < y2:
        dy = 1
    elif y1 > y2:
        dy = -1

    while True:
        x = x+dx
        y = y+dy
        if x == x2 and y == y2:
            return True
        if board[x][y] != " ":
            return False

#-----------------------------------

#-----------------------------------

def check(turn, board):
    check_move=None
    if turn == "black":
        k = "k"

    elif turn == "white":
        k = "K"

    def find_king(k):
        for row in range(8):
            for column in range(8):
                if board[row][column] == k:
                    return row, column
    xk, yk = find_king(k)

    for row in range(8):
        for column in range(8):
            cur = board[row][column]
            if cur != " ":
                if (turn == "black" and cur.isupper()) or (turn == "white" and cur.islower()):
                    cur=cur.lower()
                    if cur == "p":
                        check_move = pawn
                    elif cur == "r":
                        check_move = rook
                    elif cur == "b":
                        check_move = bishop
                    elif cur == "q":
                        check_move = queen
                    elif cur == "n":
                        check_move = knight
                    elif cur== "k":
                        check_move = king
                    if check_move(board, row, column, xk, yk):
                        return True
    return False

#-----------------------------------
enpassent = False
xp = None
yp = None

def En_passent (turn, board, x2, y2):
    if enpassent == True:
        if x2 == xp and y2 == yp:
            if turn == "black" and board[x2 - 1][y2] == "P":
                board[x2 - 1][y2] = " "
                board[x2][y2] = "P"
            elif turn == "white" and board[x2 + 1][y2] == "p":
                board[x2 + 1][y2] = " "
                board[x2][y2] = "p"

#-----------------------------------

initial_board=[["r","n","b"," ","k","b","n","r"],
               ["p","p","p","p","p","p","p","p"],
               [" "," "," "," "," "," "," "," "],
               [" "," "," "," "," "," "," "," "],
               [" "," ","q"," "," "," "," "," "],
               [" "," "," "," "," "," "," "," "],
               ["P","P","P","P","P","P","P","P"],
               ["R","N","B","Q","K","B","N","R"]]

board=copy.deepcopy(initial_board)
print_board(board)
turn = "white"
while True:

    test_board = copy.deepcopy(board)
    # input coordinates
    next_move = input("enter your next move: ")
    x1 = int(next_move[0]) - 1
    y1 = ord(str(next_move[1]).upper()) - 65
    if next_move[2] == ":":
        x2 = int(next_move[3]) - 1
        y2 = ord(str(next_move[4]).upper()) - 65
    else:
        x2 = int(next_move[2]) - 1
        y2 = ord(str(next_move[3]).upper()) - 65

    if x1 > 7 or y1 > 7 or x2 > 7 or y2 > 7:
        print("invalid coordinates")
        continue
    else:
        piece = board[x1][y1]

    if turn == "white":
        if piece.islower():
            print("white to move")
            continue

    elif turn == "black":
        if piece.isupper():
            print("black to move")
            continue

    if piece == " ":
        print ("invalid move")
        continue

    if piece.lower() == "p":
        check_move = pawn

    elif piece.lower() == "r":
        check_move = rook

    elif piece.lower() == "b":
        check_move = bishop

    elif piece.lower() == "n":
        check_move = knight

    elif piece.lower() == "q":
        check_move = queen

    elif piece.lower() == "k":
        check_move = king

    if check_move(board, x1, y1, x2, y2):
        move(test_board, x1, y1, x2, y2, piece)
        if check(turn, test_board):
            print("invalid move due to check")
            continue
        else:
            En_passent(turn, board, x2, y2)
            move(board, x1, y1, x2, y2, piece)
            clear_and_print(board)
    else:
        print("invalid move")
        continue

    if piece == "p" and x2 == x1 + 2 and x1 == 1:
        enpassent = True
        xp = x2 - 1
        yp = y2
    elif piece == "P" and x2 == x1 - 2 and x1 == 6:
        enpassent = True
        xp = x2 + 1
        yp = y2
    else:
        enpassent = False

    if turn == "white":
        turn = "black"
    elif turn == "black":
        turn = "white"

    if check(turn, board):
        print("check")



curses.endwin()