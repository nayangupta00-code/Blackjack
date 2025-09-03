import random

#BlackJack

#Create deck
#each deck has 4 suits: diamond, heart, spade, club
#each suit has 13 cards: Ace, 2-10, J, Q, K
#there can be more than one deck
suits = ["Spade","Club","Heart","Diamond"]
ranks = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
values = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10 , 10, 10]
class Card:
    def __init__(self, rank, suit, value):
        self.name = rank + " of " + suit + "s"
        self.rank = rank
        self.suit = suit
        self.value = value

deck = [Card(rank, suit, value) for rank, value in zip(ranks,values) for suit in suits]


print("Welcome to Black Jack")
# print("Shuffling \n")
random.shuffle(deck)
# print(deck[0].name)
# print(deck[0].value)

# class Player:
#     def __init(self, name, bankroll):
#         self.name = name
#         self.bankroll = bankroll

# p1 = Player()
# p2 = Player()

# setting up player vs dealer
playerCards = []
playerCount = 0
dealerCards = []
dealerCount = 0
pBust = False
dBust = False

# giving player and dealer 2 cards each, alternating
playerCards.append(deck[0])
deck.pop(0)
dealerCards.append(deck[0])
deck.pop(0)
playerCards.append(deck[0])
deck.pop(0)
dealerCards.append(deck[0])
deck.pop(0)

# display the player two cards and add the values to the player's count
print("Player has:")
for card in playerCards:
    print(card.name)
    playerCount += card.value
print("Player total count = {} \n".format(playerCount))

# displaying the dealer's up card (2nd) and adding the dealers cards to their count
print("Dealer shows: \n{} \n".format(dealerCards[1].name))
for card in dealerCards:
    dealerCount += card.value

# asking if player wants to draw a card.
hit = input("Player hit? [Y/N] \n")

# while a player wants to draw, 
# remove a card from the deck and append it to the players hand
# add the value to the players count
while hit == "Y" or hit == "y":
    print("Player draws: {}\n".format(deck[0].name))
    playerCards.append(deck[0])
    playerCount += deck[0].value
    deck.pop(0)
    
# show the player what cards are in hand
    print("Player has:")
    for card in playerCards:
        print(card.name)
# show the players current count.
# if the count is greater than 21, the player loses
    print("Player total count = {}\n".format(playerCount))
    if playerCount > 21:
        print("Player Busts! Game over!")
        pBust = True
        break
    else:
        hit = input("Player hit? [Y/N]\n")

# cont when player either does not hit or busts out

# display the dealers cards
#  first the up card and then the hidden
print("Dealer showed: \n{}".format(dealerCards[1].name))
print("Dealer had: \n{}".format(dealerCards[0].name))

# dealer must draw while less than 17 and has not bust out
# if true, dealer draws a card and adds to hand
# if dealer draws too many and goes over 21, dealer has bust
while dealerCount < 17 and not pBust:
    print("Dealer draws: {}\n".format(deck[0].name))
    dealerCards.append(deck[0])
    dealerCount += deck[0].value
    deck.pop(0)
    if dealerCount > 21:
        dBust = True
# all players finished drawing cards
print("Dealer has:")
for card in dealerCards:
    print(card.name)
print("Dealer total count: {} against player count: {}".format(dealerCount, playerCount))

print 
# player too high
if pBust: 
    print("Dealer wins!")
# player beats dealer, no bust
elif playerCount > dealerCount:
    print("Player Wins!")
# draw
elif playerCount == dealerCount:
    print("Tie game!")
# dealer bust
elif dBust:
    print("Dealer Busted out!")
else:
    print("Dealer wins!")