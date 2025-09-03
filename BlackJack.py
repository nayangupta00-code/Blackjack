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


replay = "y"
gamesPlayed = 0
winStreak = 0


while replay == "Y" or replay == "y":
    deck = [Card(rank, suit, value) for rank, value in zip(ranks,values) for suit in suits]

    print("---------------------")
    print("Welcome to Black Jack")
    print("---------------------\n")
    print("Games Played: {}".format(gamesPlayed))
    print("Current Win Streak: {}\n".format(winStreak))
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
    pNatural = False
    dNatural = False
    pAces = 0
    dAces = 0


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

        if card.rank == "Ace":
            pAces+=1



    # player drew at least one ace, giving "soft" hand
    if pAces > 0:

        # player drew pair aces giving player a hand total of 12
        if playerCount > 21:
            pAces-=1
            playerCount-= 10
            print("Player total count = 'Hard' {} \n".format(playerCount))

        # if player drew Ace and a 10 value card
        elif playerCount == 21:
            pNatural = True
            print("Blackjack! You got 21!\n")

        # Ace and below 2 through 9 value card
        else: print("Player has 'Soft' {} or {}\n".format(playerCount-10,playerCount))

    # player did not draw an ace
    else:
        print("Player total count = {} \n".format(playerCount))

    # displaying the dealer's up card and value (2nd) and adding the dealers cards to their count
    print("Dealer shows: \nFace-Down Card\n{}".format(dealerCards[1].name))
    print("Dealer known count = {}\n".format(dealerCards[1].value))

    # Adding dealer total count
    for card in dealerCards:
        # checking dealer for aces
        if card.rank == "Ace":
            dAces+=1
        # adding up dealers two cards
        dealerCount += card.value
        # if dealer drew two Aces, set hand to hard 12
        if dealerCount > 21:
            pAces-=1
            dealerCount-= 10
    # check for dealer natural 21
    if dealerCount == 21:
        dNatural = True
    # check for player Natural 21

    if playerCount == 21:
        hit = ""
    # asking if player wants to draw a card when under 21.  
    elif dealerCards[1].rank == "Ace":
        print("Checking dealer for Blackjack...")
        if  dNatural:
            print("Dealer Blackjack! Sorry\n")
            hit = ""
        else:
            print("Nobody Home\n")
            hit = input("Player hit? [Y/N] \n")
    else:
        hit = input("Player hit? [Y/N] \n")

    # while a player wants to draw, 
    # remove a card from the deck and append it to the players hand
    # add the value to the players count
    while hit == "Y" or hit == "y":
        print("Player draws: {}\n".format(deck[0].name))
        playerCards.append(deck[0])
        playerCount += deck[0].value

        if deck[0].rank == "Ace":
                pAces+=1

        deck.pop(0)
        
    # show the player what cards are in hand
        print("Player has:")
        for card in playerCards:
            print(card.name)
    # show the players current count.
    # if the count is greater than 21, the player loses

        if pAces > 0:
            # player drew pair aces giving player a hand total of 12
            if playerCount > 21:
                pAces-=1
                playerCount-= 10
                print("Player total count = {} \n".format(playerCount))
            else: print("Player has 'Soft' {} or {}\n".format(playerCount-10,playerCount))
        else:
            print("Player total count = {} \n".format(playerCount))
        if playerCount > 21:
            print("Player Busts! Game over!\n")
            pBust = True
            break
        else:
            hit = input("Player hit? [Y/N]\n")

    # cont when player either does not hit or busts out

    # show the hidden card
    # print("Dealer showed: \n{}\n".format(dealerCards[1].name))
    print("Dealer hid: \n{}".format(dealerCards[0].name))
    print("Dealer total count = {}\n".format(dealerCount))

    # dealer must draw while less than 17 and has not bust out
    # if true, dealer draws a card and adds to hand
    # if dealer draws too many and goes over 21, dealer has bust
    while dealerCount < 17 and not pNatural:
        print("Dealer draws: \n{}\n".format(deck[0].name))
        dealerCards.append(deck[0])
        dealerCount += deck[0].value
        if deck[0].rank == "Ace":
                dAces+=1

        deck.pop(0)
        if dealerCount > 21:
            if dAces > 0:
                dealerCount-=10
                dAces-=1
            else:
                print("Dealer Busted out!\n")
                # print(dealerCards.count)
                dBust = True
    # all players finished drawing cards
    print("Dealer has:")
    for card in dealerCards:
        print(card.name)
    print("Dealer total count: {} against player count: {}\n".format(dealerCount, playerCount))

    print 
    # player too high
    if pBust and dBust:
        print("Player loses. Dealer also Busts") 
        winStreak = 0
    elif pBust:
        print("Dealer wins!")
        winStreak = 0
    # player beats dealer, no bust
    elif playerCount > dealerCount:
        print("Player Wins!")
        winStreak +=1
    # draw

    elif playerCount == dealerCount:
        print("It's a Stand-Off!")
    # dealer bust
    elif dBust:
        print("Player wins! Dealer Bust")
        winStreak+=1
    else:
        print("Dealer wins!")
        winStreak = 0

    gamesPlayed+=1
    replay = input ("\nPlay again? [Y/N]\n")