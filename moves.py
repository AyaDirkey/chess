import main

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