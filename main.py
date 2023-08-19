#install windows-curses
#import curses
#scr=curses.initscr()
import os
import copy

import rules

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
rules.print_board(board)
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
        check_move = rules.pawn

    elif piece.lower() == "r":
        check_move = rules.rook

    elif piece.lower() == "b":
        check_move = rules.bishop

    elif piece.lower() == "n":
        check_move = rules.knight

    elif piece.lower() == "q":
        check_move = rules.queen

    elif piece.lower() == "k":
        check_move = rules.king

    if check_move(board, x1, y1, x2, y2):
        rules.move(test_board, x1, y1, x2, y2, piece)
        if rules.check(turn, test_board):
            print("invalid move due to check")
            continue
        else:
            rules.En_passent(turn, board, x2, y2)
            rules.move(board, x1, y1, x2, y2, piece)
            rules.clear_and_print(board)
    else:
        print("invalid move")
        continue

    if piece == "p" and x2 == x1 + 2 and x1 == 1:
        rules.enpassent = True
        xp = x2 - 1
        yp = y2
    elif piece == "P" and x2 == x1 - 2 and x1 == 6:
        rules.enpassent = True
        xp = x2 + 1
        yp = y2
    else:
        rules.enpassent = False

    if turn == "white":
        turn = "black"
    elif turn == "black":
        turn = "white"

    if rules.check(turn, board):
        print("check")



