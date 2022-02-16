'''
Four-in-a-Row (aka Connect Four) game exercise for "Beyond the Basic Stuff with Python"
This was my go at writing the game without any help, just looking at the sample output.
Comparing to book example, I think my code looks nicer and more efficient in some areas,
yet really confusing or repetative around streak checking and display. 
'''

import sys

BOARD_WIDTH = 7
BOARD_HEIGHT = 6
BOARD_COLUMNS = ''.join(str(i) for i in range(1, BOARD_WIDTH + 1)) # is there a better oneliner for this?

def prompt_move(turn):
    while True:
        print(f'player {turn}, enter 1 to 7 or QUIT')
        user_in = input('> ').upper()
        if user_in == 'QUIT':
            print('bye')
            sys.exit()
        elif len(user_in) != 1 or user_in not in BOARD_COLUMNS:
            print('invalid input')
        else:
            return user_in
            

def display_game(board):
    print(f' {BOARD_COLUMNS}')
    print(f'+{"-" * BOARD_WIDTH}+')
    for row in range(BOARD_HEIGHT, -1, -1):
        print('|', end='')
        for col in range(0, BOARD_WIDTH):
            if len(board[col]) >= row + 1:
                print(board[col][row], end='')
            else:
                print('.', end='')
        print('|')
    print(f'+{"-" * BOARD_WIDTH}+')


def do_move(board, move, turn):
    col = int(move) - 1
    row = len(board[col])

    # check if col is full
    if len(board[col]) == BOARD_HEIGHT:
        raise Exception('column full')
    # else add piece to tile and check for 4 in a row
    else:
        board[col].append(turn)

        # check vertical
        streak = 0
        for i in range(max(0, row - 3), row + 1): # max row is current piece
            if board[col][i] == turn:
                streak += 1
            else:
                streak = 0
            if streak == 4:
                return turn

        # check horizontal
        streak = 0
        for i in range(max(0, col - 3), min(BOARD_WIDTH - 1, col + 3) + 1):
            if len(board[i]) - 1 < row:
                streak = 0
                continue
            elif board[i][row] == turn:
                streak += 1
            else:
                streak = 0
            if streak == 4:
                return turn

        # check sw to ne diagonal
        streak = 0
        for (i, j) in ((-3, -3), (-2, -2), (-1, -1), (0, 0), (1, 1), (2, 2), (3, 3)):
            if col + i < 0 or col + i > BOARD_WIDTH - 1:
                continue
            elif row + j < 0 or row + i > len(board[col + i]) - 1:
                continue
            elif board[col + i][row + j] == turn:
                streak += 1
            else:
                streak = 0
            if streak == 4:
                return turn

        # check nw to se diagonal
        streak = 0
        for (i, j) in ((-3, 3), (-2, 2), (-1, 1), (0, 0), (1, -1), (2, -2), (3, -3)):
            if col + i < 0 or col + i > BOARD_WIDTH - 1:
                continue
            elif row + j < 0 or row + j > len(board[col + i]) - 1:
                continue
            elif board[col + i][row + j] == turn:
                streak += 1
            else:
                streak = 0
            if streak == 4:
                return turn

        return ''



def main():
    # intro
    print('''
four-in-a-row

two players take turns dropping tiles into one of seven columns, trying to make four in a row horizontally, vertically, or diagonally
''')

    # init board
    board = [[] for i in range(0, BOARD_WIDTH)]

    # draw init board
    display_game(board)

    winner = ''
    turn = 'X'

    # game loop
    while winner == '':
        user_move = prompt_move(turn)
        try:
            winner = do_move(board, user_move, turn)
            display_game(board)
            turn = 'X' if turn == 'O' else 'O'
        except Exception as e:
            print(e)
    
    print(f'player {winner} has won')
    

    

if __name__ == '__main__':
    main()