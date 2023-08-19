#install windows-curses
#import curses
#scr=curses.initscr()
import os


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
def rook(board,x1,y1,x2,y2):
    if check_terget(board, x1, y1, x2, y2):
        if x1 == x2 or y1 == y2:
            if bool(check_inbetween_pieces(board, x1, y1, x2, y2)):
                return True
    return False

def bishop(board,x1,y1,x2,y2):
    if check_terget(board, x1, y1, x2, y2):
        if abs(x2-x1) == abs(y2-y1):
            if bool(check_inbetween_pieces (board, x1, y1, x2, y2)):
                return True
    return False

def knight(board,x1,y1,x2,y2):
    if check_terget(board, x1, y1, x2, y2):
        dx = x2 - x1
        dy = y2 - y1
        if (abs(dx) == 1 and abs(dy) == 2) or (abs(dx) == 2 and abs(dy) == 1):
            return True
    return False

def queen(board,x1,y1,x2,y2):
    if rook(board, x1, y1, x2, y2) or bishop(board, x1, y1, x2, y2):
        return True
    return False

def king(board,x1,y1,x2,y2):
    dx = x2 - x1
    dy = y2 - y1
    if (abs(dx) == 1 and abs(dy) == 0) or (abs(dx) == 0 and abs(dy) == 1) or (abs(dx) == 1 and abs(dy) == 1):
        if queen(board, x1, y1, x2, y2):
            return True
    return False

def pawn(board,x1,y1,x2,y2):
    if y2 == y1:
        if check_inbetween_pieces(board, x1, y1, x2, y2):
            if board[x2][y2] == " ":
                if board[x1][y1].islower():
                    if x2 == x1 + 1:
                        return True
                    elif x2 == x1 + 2 and x1 == 1:
                        return True
                else:
                    if x2 == x1 - 1:
                        return True
                    elif x2 == x1 - 2 and x1 == 6:
                        return True
    elif abs(y2-y1)==1 and abs(x2-x1)==1:
        if board[x2][y2]!=" " and board[x2][y2].isupper()!=board[x1][y1].isupper():
            return True
    return False
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




