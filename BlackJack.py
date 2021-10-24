import random
import time


class players:
    def __init__(self, player):
        self.name = player
        self.hand = []
        self.totalCards = 0
        self.points = 0
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
    def __init__(self):
        self.values = {'A':[1,11], '2':2,'3':3,'4':4,'5':5,'6':6,'7':7,
                        '8':8,'9':9,'10':10,'J':10,'Q':10,'K':10}
    def comparator(self, hand, player):
        handValue1 = 0
        handValue11 = 0

        if 'A' in hand: #If there's an A

            for card in hand: #Loop hand with As

                if card == 'A': #When it reach the A
                    handValue1 = handValue1 + self.values[card][0]
                    handValue11 = handValue11 + self.values[card][1]

                else: #When it doesn't
                    handValue11 = handValue11 + self.values[card]
                    handValue1 = handValue1 + self.values[card]


            #This condition select the most convenient value and assign it to totalCard
            if handValue1 >21 or handValue11 >21: 
                if handValue1 < handValue11: #Assign the lowest value if either of them is greater than 21
                    player.totalCards = handValue1
                else:
                    player.totalCards = handValue11

            elif handValue11 ==21 or handValue1 ==21:
                if handValue11 == 21:
                   player.totalCards = handValue11
                else:
                   player.totalCards = handValue1 
            
            else:  #if both are lower they select the lowest difference between the handValue and 21
                if   21 - handValue1 < 21 - handValue11:
                     player.totalCards = handValue1
                else:
                    player.totalCards = handValue11
                    
        else: #if there's no A just loop'n sum
            for card in hand:
                handValue1 = handValue1 + self.values[card]
            player.totalCards = handValue1


def winLoosecheck(player1, player2):

    if player1.totalCards ==21 and player2.totalCards != 21:#player1 got 21 p2 not
        print(player1.name, 'wins!')
        player1.points += 1
    elif player1.totalCards <= 21 and player2.totalCards > 21:#p1 got lower or equal to 21 and p2 greater to 21
        print(player1.name, 'wins!')
        player1.points += 1
    elif player1.totalCards > 21 and player1.totalCards < player2.totalCards:#p1 greater 21 but lower than p2
        print(player1.name, 'wins!')
        player1.points += 1  
    elif player1.totalCards <= 21 and player2.totalCards < player1.totalCards: #p1 low or equal to 21 and p2 lower to p1
        print(player1.name, 'wins!')
        player1.points += 1 
    elif  player1.totalCards ==  player2.totalCards: #If they got the same value
        if  len(player1.hand) <  len(player2.hand): 
            print(player1.name, 'wins!')
            player1.points += 1 
        elif len(player1.hand) ==  len(player2.hand):
            print('Tie')
        else:
            print(player2.name, 'wins!','\n')
            player2.points += 1 
    else:
        print(player2.name, 'wins!','\n')
        player2.points += 1


cpu = players('CPU')
manager = cardManager()
value= cardValue()

p1 = players(input('Insert your name: '))
deck = manager.realDeckGenerator()
random.shuffle(deck)
manager.takeCard(deck, p1)
manager.takeCard(deck, cpu)
value.comparator(p1.hand, p1)
print(p1.hand, 'Total: ',p1.totalCards)

while True:
    takeCard = input('Take another card? yes/no ')
    takeCard.lower()
    if takeCard == 'yes':
        manager.takeCard(deck, p1)
        value.comparator(p1.hand, p1)
        print(p1.hand, 'Total: ',p1.totalCards, '\n')
        continue

    elif takeCard == 'no': #CPU turn
        print('CPU Turn')
        time.sleep(2)
        value.comparator(cpu.hand, cpu)
        while True:
            if cpu.totalCards < 21:
                manager.takeCard(deck,cpu)
                value.comparator(cpu.hand, cpu)

            elif cpu.totalCards == 21:
                print(p1.name,' hand: ', p1.hand, '\n', cpu.name,' hand: ', cpu.hand, '\n')
                time.sleep(1)
                winLoosecheck(p1,cpu)
                break

            else:
                print(p1.name,'hand: ', p1.hand, '\n', cpu.name,' hand: ', cpu.hand, '\n')
                time.sleep(1)
                print('\n')
                winLoosecheck(p1,cpu)
                break
    else:
        print('Please, write "yes" or "no"', '\n')
    break


    

    


    

    

        
    












    




