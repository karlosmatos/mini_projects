import random
import time

def print_board(board):
    for i in board:
        print(i)

def hrac1_vstup(board, board_size, symbols):
    hrac1 = list(map(int, input('Hraje hrac1. Zadej polohu symbolu v pořadí řádek-sloupec: ').split()))
    if board[hrac1[0]-1][hrac1[1]-1] == '.':
        board[hrac1[0]-1][hrac1[1]-1] = symbols[0]
    else:
        while board[hrac1[0]-1][hrac1[1]-1] != '.':
            hrac1 = list(map(int, input('Toto pole už je vybrané nebo mimo mimo hrací prostředí. Zkus vybrat něco jiného: ').split()))
        board[hrac1[0]-1][hrac1[1]-1] = symbols[0]    
    print_board(board)
    return board

def hrac2_vstup(board, board_size, symbols, two_players):
    robot = []
    if two_players == 'ano':
        hrac2 = list(map(int, input('Hraje hrac2. Zadej polohu symbolu v pořadí řádek-sloupec: ').split()))
        hrac2 = [i-1 for i in hrac2]
        if IndexError:
            while IndexError or board[hrac2[0]][hrac2[1]] != '.':
                hrac2 = list(map(int, input('Toto pole už je vybrané. Zkus vybrat něco jiného: ').split()))
            board[hrac2[0]][hrac2[1]] = symbols[1]
        if board[hrac2[0]][hrac2[1]] == '.':
            board[hrac2[0]][hrac2[1]] = symbols[1]
        else:
            while board[hrac2[0]][hrac2[1]] != '.':
                hrac2 = list(map(int, input('Toto pole už je vybrané. Zkus vybrat něco jiného: ').split()))
            board[hrac2[0]][hrac2[1]] = symbols[1]
        print_board(board)
        return board
    else:
        print('Počítač se připravuje na svůj tah...')
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
            if board[iradek][jsloupec] == board[iradek][jsloupec-1] == board[iradek][jsloupec-2] and board[iradek][jsloupec] in symbols:
                hra = False
                symbol = board[iradek][jsloupec]
            elif board[iradek][jsloupec] == board[iradek-1][jsloupec] == board[iradek-2][jsloupec] and board[iradek][jsloupec] in symbols:
                hra = False
                symbol = board[iradek][jsloupec]
            elif board[iradek][jsloupec] == board[iradek-1][jsloupec-1] == board[iradek-2][jsloupec-2] and board[iradek][jsloupec] in symbols:
                hra = False
                symbol = board[iradek][jsloupec]
            elif board[iradek][jsloupec] == board[iradek-2][jsloupec-1] == board[iradek-1][jsloupec-2] and board[iradek][jsloupec] in symbols:
                hra = False
                symbol = board[iradek][jsloupec]
    if hra == False:
        print(f'Vítězí hráč se symbolem: {symbol}. Gratulujeme!')
    return hra

def main():
    symbols = list(map(str, input('Zvolte si symboly, kterýma chcete hrát, např: "X" "O" "Y" "!"\n ').split()))
    board_size = list(map(int, input('Zvolte velikost boardu, např: "3x3"\n').lower().split("x")))
    board = [['.']*board_size[0] for i in range(board_size[1])]
    two_players = input('Chcete hru pro 2 hráče? "ano" | "ne"\n').lower()
    print_board(board)
    hra = True
    while hra:
        hrac1_vstup(board, board_size, symbols)
        hra = win(board, board_size, symbols, hra)
        if hra == False:
            break
        hrac2_vstup(board, board_size, symbols, two_players)
        hra = win(board, board_size, symbols, hra)



if __name__ == "__main__":
    main()
