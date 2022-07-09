import random
import time

def print_board(board):
    for i in board:
        print(i)

def hrac1_vstup(board, board_size, symbols):
    hrac1 = list(map(int, input('Player1 playing. Specify the position of the symbol in row-column order: ').split()))
    hrac1 = [i-1 for i in hrac1]
    try:
        if board[hrac1[0]][hrac1[1]] == '.':
            board[hrac1[0]][hrac1[1]] = symbols[0]
        else:
            while board[hrac1[0]][hrac1[1]] != '.':
                hrac1 = list(map(int, input('This field is already selected or out of play. Try selecting something else: ').split()))
                hrac1 = [i-1 for i in hrac1]
            board[hrac1[0]][hrac1[1]] = symbols[0]
    except IndexError:
        while IndexError or board[hrac2[0]][hrac2[1]] != '.':
            hrac2 = list(map(int, input('This field is already selected or out of play. Try selecting something else: ').split()))
            hrac2 = [i-1 for i in hrac2]
        board[hrac2[0]][hrac2[1]] = symbols[1]
    except:
        while board[hrac1[0]][hrac1[1]] != '.':
            hrac1 = list(map(int, input('This field is already selected or out of play. Try selecting something else: ').split()))
            hrac1 = [i-1 for i in hrac1]
        board[hrac1[0]][hrac1[1]] = symbols[0]    
    print_board(board)
    return board

def hrac2_vstup(board, board_size, symbols, two_players):
    robot = []
    if two_players == 'yes':
        hrac2 = list(map(int, input('Player2 playing. Specify the position of the symbol in row-column order: ').split()))
        hrac2 = [i-1 for i in hrac2]
        try:
            if board[hrac2[0]][hrac2[1]] == '.':
                board[hrac2[0]][hrac2[1]] = symbols[1]
            else:
                while board[hrac2[0]][hrac2[1]] != '.':
                    hrac2 = list(map(int, input('This field is already selected or out of play. Try selecting something else: ').split()))
                    hrac2 = [i-1 for i in hrac2]
                board[hrac2[0]][hrac2[1]] = symbols[1]
        except IndexError:
            while IndexError or board[hrac2[0]][hrac2[1]] != '.':
                hrac2 = list(map(int, input('This field is already selected or out of play. Try selecting something else: ').split()))
                hrac2 = [i-1 for i in hrac2]
            board[hrac2[0]][hrac2[1]] = symbols[1]
        except:
            while board[hrac2[0]][hrac2[1]] != '.':
                hrac2 = list(map(int, input('This field is already selected or out of play. Try selecting something else: ').split()))
                hrac2 = [i-1 for i in hrac2]
            board[hrac2[0]][hrac2[1]] = symbols[1]    
        print_board(board)
        return board
    else:
        print('The computer is preparing for its move...')
        robot = [random.randint(0, board_size[0]) for i in range(board_size[1]-1)]
        time.sleep(3)
        while board[robot[0]-1][robot[1]-1] != '.':
            robot = [random.randint(0, board_size[0]) for i in range(board_size[1]-1)]
        board[robot[0]-1][robot[1]-1] = symbols[1]
        print_board(board)
        return board

def win(board, board_size, symbols, hra):
    hra = True
    for iradek in range(board_size[0]):
        for jsloupec in range(board_size[1]):
            if board[iradek][jsloupec] == board[iradek][jsloupec-1] == board[iradek][jsloupec-2] and board[iradek][jsloupec] in symbols: #row
                hra = False
                symbol = board[iradek][jsloupec]
            elif board[iradek][jsloupec] == board[iradek-1][jsloupec] == board[iradek-2][jsloupec] and board[iradek][jsloupec] in symbols: #column
                hra = False
                symbol = board[iradek][jsloupec]
            elif board[iradek][jsloupec] == board[iradek-1][jsloupec-1] == board[iradek-2][jsloupec-2] and board[iradek][jsloupec] in symbols: #diagonal right to left up
                hra = False
                symbol = board[iradek][jsloupec]
            elif board[iradek-1][jsloupec-1] == board[iradek-2][jsloupec] == board[iradek][jsloupec-2] and board[iradek-1][jsloupec-1] in symbols: #diagonal right to leftdown
                hra = False
                symbol = board[iradek-1][jsloupec-1]
    if hra == False:
        print(f'The winner is the player with {symbol}. Congratulations!')
    return hra

def main():
    symbols = list(map(str, input('Choose the symbols you want to play with, e.g. "X" "O" "Y" "!"\n ').split()))
    board_size = list(map(int, input('Select the size of the board, e.g. 3x3\n').lower().split('x')))
    board = [['.']*board_size[0] for i in range(board_size[1])]
    two_players = input('Want a 2-player game? yes | no\n').lower()
    print_board(board)
    hra = True
    while hra:
        hrac1_vstup(board, board_size, symbols)
        hra = win(board, board_size, symbols, hra)
        if hra == False:
            break
        hrac2_vstup(board, board_size, symbols, two_players)
        hra = win(board, board_size, symbols, hra)



if __name__ == '__main__':
    main()
