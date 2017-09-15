import random

#initalizing variables
number= random.randint(1,11)
aceChoice=0
playerWins=0
dealerWins=0
playerCards =[]
dealerCards =[]


#Stating game and rules
print("Welcome to World Series Black Jack")
print("Reach a final score higher than the dealer without exceeding 21")
print("Over 21 is a bust and automatic win for dealer")
print("First to 5 Wins")
print("Double or nothing, how much would you like to bet? ")
bet=input()
while playerWins <5 or dealerWins <5:

    if dealerWins == 5:
        break
    if playerWins == 5:
        break

    # Creating dealers staring deck
    while len(dealerCards) != 2:
        cardD=random.randint(1, 11)
        #Adds card to deck
        dealerCards.append(cardD)
    # Creating players starting deck
    while len(playerCards) != 2:
        cardP = random.randint(1, 10)
        #If ace is drawn you are given the option to choose 1 or 11
        if cardP == 1:
            print('You drew an Ace')
            print('Would you like it to be worth 11 or 1?')
            aceV=input()
            if aceV == "11":
                cardP = 11
            if aceV == "1":
                cardD = 1
        #Adds card to deck
        playerCards.append(cardP)
        
        if len(playerCards) == 2:
            print()
            print("Your total is " + str(sum(playerCards)) + " You drew a ", playerCards)
           
    #Asks player for hit or stick
    while sum(playerCards) < 21:
        choice=str(input('"hit" or "stick?"'))
        print()
        #If hit then another random interval is drawn from 1-10
        if choice == "hit":
            number= random.randint(1,10)
            #If ace is drawn you are given the option to choose 1 or 11
            if number ==1:
                print('You drew an Ace')
                print('Would you like it to be worth 11 or 1?')
                aceV=input()
                if aceV == "11":
                    number = 11
                if aceV == "1":
                    number = 1
            #Adds card to deck
            playerCards.append(number)
    
            print("Your total is now " + str(sum(playerCards)) + " with these cards ",playerCards)
        #if stick then dealer hits until over 17
        elif choice == "stick":
            while sum(dealerCards) < 17:
                number= random.randint(1,11)
                #Adds card to deck
                dealerCards.append(number)

            print("The dealer has a total of " + str(sum(dealerCards)) + " with ", dealerCards)
            print("You have a total of " + str(sum(playerCards)) + " with ", playerCards)
            #Checking dealer's deck sum for Bust or Blackjack
            #greater than 21 is instant bust
            if sum(dealerCards) > 21:
                print("Dealer has BUSTED!")
                playerWins = playerWins +1
                print("PLAYER " +str(playerWins)+ " - " +str(dealerWins)+ " DEALER")
                break

                #excatly 21 is instant win
            elif sum(dealerCards) == 21:
                print("Dealer has BLACKJACK and wins! 21")
                dealerWins = dealerWins + 1
                print("PLAYER " +str(playerWins)+ " - " +str(dealerWins)+ " DEALER")
                break

    #Deck sums used to see who wins
            #Checking for Draw
            if sum(dealerCards) == sum(playerCards):
                print("DRAW")
                print("PLAYER " +str(playerWins)+ " - " +str(dealerWins)+ " DEALER")
                break
            #Checking dealers deck sum
            if sum(dealerCards) > sum(playerCards):
                print("DEALER WINS")
                dealerWins = dealerWins + 1
                print("PLAYER " +str(playerWins)+ " - " +str(dealerWins)+ " DEALER")
                break
         
            else:
                print("YOU WIN")
                playerWins = playerWins + 1
                print("PLAYER " +str(playerWins)+ " - " +str(dealerWins)+ " DEALER")
                break

   
    

    #excatly 21 is instant win
    if sum(playerCards) == 21:
        print("You have BLACKJACK! You Win! 21")
        playerWins = playerWins + 1
        print("PLAYER " +str(playerWins)+ " - " +str(dealerWins)+ " DEALER")
    #greater than 21 is instant bust
    elif sum(playerCards) > 21:
        print("You BUSTED! Dealer wins.")
        dealerWins = dealerWins + 1
        print("PLAYER " +str(playerWins)+ " - " +str(dealerWins)+ " DEALER")

    playerCards=[]
    dealerCards=[]
    print()
#Checking first to five for bets
if dealerWins>playerWins:
    print("Total Winnings $-" + str(bet))
else:
    bet=int(bet)+int(bet)
    print("Total Winnings $" + str(bet))
print("Thank you for playing")

        


