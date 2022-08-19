import random
import time

class Blackjack():

    def __init__(self):
        self.player = []
        self.computer = []
        self.cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

    def card_get(self, user):
        random_card = random.choice(self.cards)
        user = user.append(random_card)
        self.cards.remove(random_card)

    def card_count_player(self):
        print(f"Players's cards: {self.player} (Total points: {sum(self.player)})")

    def card_count_computer(self):
        print(f"Computer's cards: {self.computer} (Total points: {sum(self.computer)})")
    
    def player_hand(self):
        for i in range(2):
            self.card_get(user=self.player)
        self.card_count_player()

    def player_game(self):
        game = True
        while game:
            player_command = input('Would like to get another card? ').lower()
            if player_command == 'yes' and sum(self.player) < 21:
                self.card_get(user=self.player)
                self.card_count_player()
                if sum(self.player) >= 21:
                    game = False
                    break
            else:
                game = False
                break
        print(f'Your score is {sum(self.player)}')

    def computer_game(self):
        print('Computer is playing...')
        self.card_get(self.computer)
        while sum(self.computer) - sum(self.player) <= 1 and sum(self.computer) <= 21:
            time.sleep(3)
            self.card_get(user=self.computer)
            self.card_count_computer()
            if sum(self.player) > 21 or sum(self.computer) == sum(self.player):
                break

    def winner(self):
        if sum(self.player) > sum(self.computer):
            if sum(self.player) <= 21:
                return f'Player wins with the score of {sum(self.layer)} points. Congratulation!'
            else:
                return f'Computer wins with the score of {sum(self.computer)} points.'
        elif sum(self.player) == sum(self.computer):
            return 'Draw'
        else:
            if sum(self.computer) <= 21:
                return f'Computer wins with the score of {sum(self.computer)} points.'
            else:
                return f'Player wins with the score of {sum(self.player)} points. Congratulation!'

def main():
    blackjack_game = Blackjack()
    blackjack_game.player_hand()
    blackjack_game.player_game()
    blackjack_game.computer_game()
    print(blackjack_game.winner())

if __name__ == '__main__':
    main()