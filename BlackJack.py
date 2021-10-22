import random

from numpy.lib.arraysetops import isin


class players:
    def __init__(self, player):
        self.player = player
        self.hand = []
        self.totalCards = 0
    def printHand(self):
        print(self.hand)

    def printValue(self):
        return self.value

class cardManager:
    def __init__(self):
        self.deckUnique = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
    def realDeckGenerator(self):
        realDeck = []
        counter = 0

        while counter <4:
            copyDeck = self.deckUnique.copy()
            realDeck.append(copyDeck)
            counter +=1

        realDeck = [card for groupCards in realDeck for card in groupCards]
        
        return realDeck
    
    def takeCard(self, realDeck, player):
        player.hand.append(realDeck[0])
        realDeck.pop(0)
        return realDeck

class cardValue:
    def __init__(self, hand):
        self.hand = hand
        self.values = {'A':[1,11], '2':2,'3':3,'4':4,'5':5,'6':6,'7':7,
                        '8':8,'9':9,'10':10,'J':10,'Q':10,'K':10}
    def comparator(self):
        handValue1 = 0
        handValue11 = 0

        if 'A' in self.hand: #If there's an A

            for card in self.hand: #Loop hand with As

                if card == 'A': #When it reach the A
                    handValue1 = handValue1 + self.values[card][0]
                    handValue11 = handValue11 = self.values[card][1]

                else: #When it doesn't
                    handValue11 = handValue11 = self.values[card]
                    handValue1 = handValue1 + self.values[card]
                    
            return handValue1, handValue11

        else:
            for card in self.hand():
                handValue1 = handValue1 + self.values[card]
            return handValue1 





p1 = players('Sebas')
cpu = players('CPU')
manager = cardManager()
deck = manager.realDeckGenerator()

manager.takeCard(deck, p1)





    




