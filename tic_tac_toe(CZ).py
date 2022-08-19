import random
import time

class Game:

    def __init__(self, symbols:list , board_size:list , otazka_dva_hraci:str):
        self.symbols = symbols
        self.board_size = board_size
        self.otazka_dva_hraci = otazka_dva_hraci
        self.board = [['.']*board_size[0] for pole in range(board_size[1])]

    def print_board(self):
        for pole in self.board:
            print(pole)
    
    def vyber_noveho_pole(self, hrac:list):
        hrac = list(map(int, input('Toto pole je už vybrané nebo mimo hrací prostředí. Zkus vybrat něco jiného: ').split()))
        hrac = [vstup-1 for vstup in hrac]
    
    def snaha_usazeni_hrace(self, hrac:list, symbol:str):
        while IndexError or self.board[hrac[0]][hrac[1]] != '.':
            hrac = self.vyber_noveho_pole(hrac)
        self.board[hrac[0]][hrac[1]] = symbol
        return self.board

    def hrac1_vstup(self):
        hrac1 = list(map(int, input('Hraje Hráč č.1. Zadej pozici symbolu v pořadí řádek-sloupec: ').split()))
        hrac1 = [vstup-1 for vstup in hrac1]
        try:
            if self.board[hrac1[0]][hrac1[1]] == '.':
                self.board[hrac1[0]][hrac1[1]] = self.symbols[0]
            else:
                self.snaha_usazeni_hrace(hrac1, self.symbols[0])
        except:
            self.snaha_usazeni_hrace(hrac1, self.symbols[0])   
        self.print_board()
        return self.board

    def hrac2_vstup(self):
        robot = []
        if self.otazka_dva_hraci == 'ano':                          #Pokud je odpověď na otázku pro 2 hráče 'ano', tak jse algoritmus rozhodne pro funkce hráče2
            hrac2 = list(map(int, input('Hraje Hráč č.2. Zadej pozici symbolu v pořadí řádek-sloupec: ').split()))
            hrac2 = [vstup-1 for vstup in hrac2]
            try:
                if self.board[hrac2[0]][hrac2[1]] == '.':
                    self.board[hrac2[0]][hrac2[1]] = self.symbols[1]
                else:
                    self.snaha_usazeni_hrace(hrac2, self.symbols[1])
            except:
                self.snaha_usazeni_hrace(hrac2, self.symbols[1])   
        else:                                                       #Pokud je odpověď na otázku pro 2 hráče jiná než 'ano', tak je hráč2 zastoupen rozhodováním počítače
            print('Počítač se připravuje na svůj tah...')
            time.sleep(3)
            robot = [random.randint(0, self.board_size[0]) for pozice in range(self.board_size[1]-1)]
            while self.board[robot[0]-1][robot[1]-1] != '.':
                robot = [random.randint(0, self.board_size[0]) for pozice in range(self.board_size[1]-1)]
            self.board[robot[0]-1][robot[1]-1] = self.symbols[1]
        self.print_board()
        return self.board

    def win(self):
        bezici_hra = True
        for iradek in range(self.board_size[0]):
            for jsloupec in range(self.board_size[1]):
                if self.board[iradek][jsloupec] == self.board[iradek][jsloupec-1] == self.board[iradek][jsloupec-2] and self.board[iradek][jsloupec] in self.symbols: #řádek
                    bezici_hra = False
                    symbol = self.board[iradek][jsloupec]
                elif self.board[iradek][jsloupec] == self.board[iradek-1][jsloupec] == self.board[iradek-2][jsloupec] and self.board[iradek][jsloupec] in self.symbols: #sloupec
                    bezici_hra = False
                    symbol = self.board[iradek][jsloupec]
                elif self.board[iradek][jsloupec] == self.board[iradek-1][jsloupec-1] == self.board[iradek-2][jsloupec-2] and self.board[iradek][jsloupec] in self.symbols: #diagonal zpravo doleva nahoru
                    bezici_hra = False
                    symbol = self.board[iradek][jsloupec]
                elif self.board[iradek-1][jsloupec-1] == self.board[iradek-2][jsloupec] == self.board[iradek][jsloupec-2] and self.board[iradek-1][jsloupec-1] in self.symbols: #diagonal zpravo doleva dolů
                    bezici_hra = False
                    symbol = self.board[iradek-1][jsloupec-1]
        if bezici_hra == False:
            print(f'Vítězí hráč se symbolem: {symbol}. Gratulujeme!')
        return bezici_hra

def main():
    symbols = list(map(str, input('Zvolte si symboly, kterýma chcete hrát, např: "X" "O" "Y" "!"\n ').split())) #vybrání symbolů
    board_size = list(map(int, input('Zvolte velikost self.boardu, např: "3x3"\n').lower().split("x"))) #výběr velikosti hracího boardu
    otazka_dva_hraci = input('Chcete hru pro 2 hráče? "ano" | "ne"\n').lower() #otázka na hru pro 2 hráče
    hra = Game(symbols, board_size, otazka_dva_hraci)
    hra.print_board()
    bezici_hra = True
    while bezici_hra:
        hra.hrac1_vstup()
        bezici_hra = hra.win()
        if bezici_hra == False:
            break
        hra.hrac2_vstup()
        bezici_hra = hra.win()



if __name__ == "__main__":
    main()
