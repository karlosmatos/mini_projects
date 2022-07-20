import random
import time

player1 = []
computer = []

def card_get(player):
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    random_card = random.choice(cards)
    player = player.append(random_card)
    cards.remove(random_card)

def card_count_player(player):
    print(f"Players's cards: {player} (Total points: {sum(player)})")

def card_count_computer(computer):
    print(f"Computer's cards: {computer} (Total points: {sum(computer)})")
   
def player_hand(player):
    for i in range(2):
        card_get(player)
    card_count_player(player)

def player_game(player):
    game = True
    while game:
        player_command = input('Would like to get another card? ').lower()
        if player_command == 'yes' and sum(player) < 21:
            card_get(player)
            card_count_player(player)
            if sum(player) >= 21:
                game = False
                break
        else:
            game = False
            break
    print(f'Your score is {sum(player)}')

def computer_game(computer, player):
    print('Computer is playing...')
    card_get(computer)
    while sum(computer) - sum(player) <= 1 and sum(computer) <= 21:
        time.sleep(3)
        card_get(computer)
        card_count_computer(computer)
        if sum(player) > 21 or sum(computer) == sum(player):
            break

def winner(player, computer):
    if sum(player) > sum(computer):
        if sum(player) <= 21:
            return f'Player wins with the score of {sum(player)} points. Congratulation!'
        else:
            return f'Computer wins with the score of {sum(computer)} points.'
    elif sum(player) == sum(computer):
        return 'Draw'
    else:
        if sum(computer) <= 21:
            return f'Computer wins with the score of {sum(computer)} points.'
        else:
            return f'Player wins with the score of {sum(player)} points. Congratulation!'

def main():
    player_hand(player1)
    player_game(player1)
    computer_game(computer, player1)
    print(winner(player1, computer))

if __name__ == '__main__':
    main()
