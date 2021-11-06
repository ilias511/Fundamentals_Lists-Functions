import random
import asyncio

async def play(x):
    player_hand = [random.randint(1, 10), random.randint(1,10)]
    dealer = [x, random.randint(1, 10)]
    print(f"Player's card are {player_hand}")
    print(f"Dealers's card are X, {dealer[1]}")
    player_hand = sum(player_hand)

    print(f"Player's card sum is {player_hand}")

    player_decision = input("Do you want to draw a card or fold?")

    while player_decision!='fold':   # player cards
        player_hand+=random.randint(1,10)
        print(f'Now player has {player_hand}')
        if player_hand>21:
            print('You have busted')
            print('Dealer wins')
            break
        else:
            pass
        player_decision = input("Do you want to draw a card or fold?")
    dealer_bust = False
    dealer_sum = sum(dealer)
    print(f'The dealer has {dealer_sum}')
    while dealer_sum<21:
        if dealer_sum<16:
            dealer_sum+=random.randint(1,10)
            await asyncio.sleep(1)
            print(f'The dealer has {dealer_sum}')
        if dealer_sum>21:
            dealer_bust = True
            break
        if 21>dealer_sum>=16:
            break

    if dealer_bust:
        print(f'Dealer has {dealer_sum} and its too many ')
        print('Player wins')
    else:
        if player_hand>dealer_sum:
            print('Player has won 100 bitcoins')
        elif player_hand<dealer_sum:
            print('The dealer has won')
        else:
            print('its draw you get your money back')

asyncio.run(play(x=random.randint(1, 10)))