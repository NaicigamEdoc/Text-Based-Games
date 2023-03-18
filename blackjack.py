#Text-Based Blackjack Game
#Coded by NaicigamEdoc
import random
import time
def deal(target):
    cardToDeal = random.choice(cards)
    target.append(cardToDeal)
    cards.remove(cardToDeal)
    if total(target) > 21:
        if target == dealerHand:
            print("Dealer busted!")
            winner[0] = "player"
            return(0)
        else:
            print("You busted!")
            winner[0] = "dealer"
            return(0)
    if target == playerHand:
        list(playerHand)
def total(target):
    total = 0
    for i in range(len(target)):
        if (target[i] == "AoC") or (target[i] == "AoH") or (target[i] == "AoS") or (target[i] == "AoD"):
            if aceValue[0] == 1:
                total += 1
            else:
                total += 11
        if (target[i] == "2oC") or (target[i] == "2oH") or (target[i] == "2oS") or (target[i] == "2oD"):
            total += 2
        if (target[i] == "3oC") or (target[i] == "3oH") or (target[i] == "3oS") or (target[i] == "3oD"):
            total += 3
        if (target[i] == "4oC") or (target[i] == "4oH") or (target[i] == "4oS") or (target[i] == "4oD"):
            total += 4
        if (target[i] == "5oC") or (target[i] == "5oH") or (target[i] == "5oS") or (target[i] == "5oD"):
            total += 5
        if (target[i] == "6oC") or (target[i] == "6oH") or (target[i] == "6oS") or (target[i] == "6oD"):
            total += 6
        if (target[i] == "7oC") or (target[i] == "7oH") or (target[i] == "7oS") or (target[i] == "7oD"):
            total += 7
        if (target[i] == "8oC") or (target[i] == "8oH") or (target[i] == "8oS") or (target[i] == "8oD"):
            total += 8
        if (target[i] == "9oC") or (target[i] == "9oH") or (target[i] == "9oS") or (target[i] == "9oD"):
            total += 9
        if (target[i] == "10oC") or (target[i] == "10oH") or (target[i] == "10oS") or (target[i] == "10oD") or (target[i] == "JoC") or (target[i] == "JoH") or (target[i] == "JoS") or (target[i] == "JoD") or (target[i] == "QoC") or (target[i] == "QoH") or (target[i] == "QoS") or (target[i] == "QoD") or (target[i] == "KoC") or (target[i] == "KoH") or (target[i] == "KoS") or (target[i] == "KoD"):
            total += 10
    return(total)
def list(target):
    if target == playerHand:
        print("******** LIST OF PLAYER'S CARDS ********")
        print(target)
        print("Total points (player):", total(target), "\n")
    elif (target == dealerHand) and (dealerTurnHasHappened[0] == 1):
        print("******** LIST OF DEALER'S CARDS ********")
        print(target)
        print("Total points (dealer):", total(target), "\n")
    else:
        print("******** LIST OF DEALER'S CARDS (as far as you know) ********")
        dealerKnownCard = [target[1]]
        print(dealerKnownCard)
        print("Total points (dealer, as far as you know):", total(dealerKnownCard), "\n")
def listOptions():
    print("Options: ")
    print("hit - deals one card to the player\nstay - passes the turn to the dealer, highest points/last to bust wins (after the dealer's turn)\nlistp - lists your cards, and your point total\nlistd - lists the dealers cards, and their point total\nacevalue1 - sets the value of aces to 1\nacevalue11 - sets the value of aces to 11\n")
def menu():
    completion = 0
    while not completion == 1:
        choice = input('What would you like to do? ("options" for options) ')
        if choice == "listp":
            list(playerHand)
        elif choice == "listd":
            list(dealerHand)
        elif choice == "hit":
            if deal(playerHand) == 0:
                completion = 1
        elif choice == "stay":
            completion = 1
            dealerTurn()
        elif choice == "options":
            listOptions()
        elif choice == "acevalue1":
            aceValue[0] = 1
            list(playerHand)
        elif choice == "acevalue11":
            aceValue[0] = 11
            list(playerHand)
        else:
            print("Invalid input.")
def dealerTurn():
    dealerTurnHasHappened[0] = 1
    completion = 0
    list(dealerHand)
    time.sleep(2)
    while not completion == 1:
        if total(dealerHand) >= 17:
            if total(dealerHand) > total(playerHand):
                list(dealerHand)
                print("The dealer won! They have more points!")
                winner[0] = "dealer"
                completion = 1
            elif total(playerHand) > total(dealerHand):
                list(dealerHand)
                print("You won! You have more points")
                winner[0] = "player"
                completion = 1
            else:
                list(dealerHand)
                print("It was a push. You tied in points.")
                winner[0] = "tie"
                completion = 1
        else:
            if deal(dealerHand) == 0:
                completion = 1
            list(dealerHand)
            time.sleep(1)
def startGame():
    for i in range(2):
        deal(playerHand)
        deal(dealerHand)
        if total(playerHand) == 21:
            print("Blackjack! You won.")
            winner[0] = "player"
        if total(dealerHand) == 21:
            print("The dealer got blackjack! They won.")
            winner[0] = "dealer"
#MAIN
while True:
    choice = [" ", " "]
    cards = ["AoC", "2oC", "3oC", "4oC", "5oC", "6oC", "7oC", "8oC", "9oC", "10oC", "JoC", "QoC", "KoC", "AoH", "2oH", "3oH", "4oH", "5oH", "6oH", "7oH", "8oH", "9oH", "10oH", "JoH", "QoH", "KoH", "AoS", "2oS", "3oS", "4oS", "5oS", "6oS", "7oS", "8oS", "9oS", "10oS", "JoS", "QoS", "KoS", "AoD", "2oD", "3oD", "4oD", "5oD", "6oD", "7oD", "8oD", "9oD", "10oD", "JoD", "QoD", "KoD"]
    dealerHand = []
    playerHand = []
    winner = ["placeholder", "placeholder2"]
    aceValue = [1]
    dealerTurnHasHappened = [0]
    while True:
        choice[0] = input("Do you want to play blackjack? (y/n) ")
        if choice[0] in ("y", "n"):
            break
        print("Invalid input!")
    if choice[0] == "n":
        print("Ok!")
        break
    else:
        startGame()
        while winner[0] == "placeholder":
            menu()
        continue
