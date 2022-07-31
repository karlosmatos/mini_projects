import random
import time

class Game:

    def __init__(self, symbols:list , board_size:list , question_two_players:str):
        self.symbols = symbols
        self.board_size = board_size
        self.question_two_players = question_two_players
        self.board = [['.']*board_size[0] for i in range(board_size[1])]

    def print_board(self):
        for i in self.board:
            print(i)
    
    def select_new_field(self, player:list):
        player = list(map(int, input('This field is already selected or out of play. Try selecting something else: ').split()))
        player = [i-1 for i in player]
    
    def effort_settlement_player(self, player:list, symbol:str):
        while IndexError or self.board[player[0]][player[1]] != '.':
            player = self.select_new_field(player)
        self.board[player[0]][player[1]] = symbol
        return self.board

    def player1_entry(self):
        player1 = list(map(int, input('Player1 playing. Specify the position of the symbol in row-column order: ').split()))
        player1 = [i-1 for i in player1]
        try:
            if self.board[player1[0]][player1[1]] == '.':
                self.board[player1[0]][player1[1]] = self.symbols[0]
            else:
                self.effort_settlement_player(player1, self.symbols[0])
        except:
            self.effort_settlement_player(player1, self.symbols[0])   
        self.print_board()
        return self.board

    def player2_entry(self):
        robot = []
        if self.question_two_players == 'yes':
            player2 = list(map(int, input('Player2 playing. Specify the position of the symbol in row-column order: ').split()))
            player2 = [i-1 for i in player2]
            try:
                if self.board[player2[0]][player2[1]] == '.':
                    self.board[player2[0]][player2[1]] = self.symbols[1]
                else:
                    self.effort_settlement_player(player2, self.symbols[1])
            except:
                self.effort_settlement_player(player2, self.symbols[1])   
        else:
            print('The computer is preparing for its move...')
            time.sleep(3)
            robot = [random.randint(0, self.board_size[0]) for i in range(self.board_size[1]-1)]
            while self.board[robot[0]-1][robot[1]-1] != '.':
                robot = [random.randint(0, self.board_size[0]) for i in range(self.board_size[1]-1)]
            self.board[robot[0]-1][robot[1]-1] = self.symbols[1]
        self.print_board()
        return self.board

    def win(self):
        game_running = True
        for iradek in range(self.board_size[0]):
            for jsloupec in range(self.board_size[1]):
                if self.board[iradek][jsloupec] == self.board[iradek][jsloupec-1] == self.board[iradek][jsloupec-2] and self.board[iradek][jsloupec] in self.symbols: #řádek
                    game_running = False
                    symbol = self.board[iradek][jsloupec]
                elif self.board[iradek][jsloupec] == self.board[iradek-1][jsloupec] == self.board[iradek-2][jsloupec] and self.board[iradek][jsloupec] in self.symbols: #sloupec
                    game_running = False
                    symbol = self.board[iradek][jsloupec]
                elif self.board[iradek][jsloupec] == self.board[iradek-1][jsloupec-1] == self.board[iradek-2][jsloupec-2] and self.board[iradek][jsloupec] in self.symbols: #diagonal zpravo doleva nahoru
                    game_running = False
                    symbol = self.board[iradek][jsloupec]
                elif self.board[iradek-1][jsloupec-1] == self.board[iradek-2][jsloupec] == self.board[iradek][jsloupec-2] and self.board[iradek-1][jsloupec-1] in self.symbols: #diagonal zpravo doleva dolů
                    game_running = False
                    symbol = self.board[iradek-1][jsloupec-1]
        if game_running == False:
            print(f'The winner is the player with {symbol}. Congratulations!')
        return game_running

def main():
    symbols = list(map(str, input('Choose the symbols you want to play with, e.g. "X" "O" "Y" "!"\n ').split()))
    board_size = list(map(int, input('Select the size of the board, e.g. 3x3\n').lower().split('x')))
    question_two_players = input('Want a 2-player game? yes | no\n').lower()
    game = Game(symbols, board_size, question_two_players)
    game.print_board()
    game_running = True
    while game_running:
        game.player1_entry()
        game_running = game.win()
        if game_running == False:
            break
        game.player2_entry()
        game_running = game.win()



if __name__ == "__main__":
    main()
