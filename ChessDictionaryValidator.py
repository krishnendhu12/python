name=input("Krishnendhu: ")
USN=input("1AY24BT023: ")
def is_valid_chess_board(board):
    white_king = 0
    black_king = 0

    for piece in board.values():
        if piece == 'wking':
            white_king += 1
        elif piece == 'bking':
            black_king += 1

    if white_king == 1 and black_king == 1:
        return True
    else:
        return False
