# Initiale Code for Card Game 

import random

class Card:

    #card whole deck of 52
    def __init__(self):
        Card.card_whole = []
        
        for _ in range(1,53):
            Card.card_whole.append(_)

#        Actual list 
#        print(Card.card_whole)
        random.shuffle(Card.card_whole)
        print(Card.card_whole)

#       Splitting the whole deck into two 

        self.deck_1 = Card.card_whole[:25]
        self.deck_2 = Card.card_whole[25:]

        print(f'Deck 1 is : {self.deck_1}')
        print(f'Deck 2 is : {self.deck_2}')

        

    def deck_split(self):

        base_deck = {
                    '1':1,
                    '2':2,
                    '3':3,
                    '4':4,
                    '5':5,
                    '6':6,
                    '7':7,
                    '8':8,
                    '9':9,
                    '10':10,
                    'j':11,
                    'q':12,
                    'k':13,
                    'a':14
                    } 

        #Testing sample top cards 

#        player1_t_card = input('Enter an sample card: ')
#        player2_t_card = input('Enter an player 2 card: ')

#        for _ in len(player1_t_card):
        self.game_end = True

        while self.game_end == True:

            for _ in range(0,25):
                    
                i = 25
                player1_card = self.deck_1[i-1]
                player2_card = self.deck_2[i-1]

                print(player1_card)
                print(player2_card)

                if base_deck[player1_card] > base_deck[player2_card]:
                    print('Player 1 won, card added to their deck')
                elif base_deck[player1_card] < base_deck[player2_card]:
                    print('Player 2 won, card added to their deck')
                else:
                    print('WAR MODE ON')   
            game_end = False


#    def card_split(self):
#
#        shuf_cards = random.shuffle(Card.card_whole)
#        print(shuf_cards)
#        pass

my_card = Card()

my_card.deck_split()
