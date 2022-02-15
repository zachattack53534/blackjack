import random
import time

money = int(input("How much money do you want to start with? £"))
initialmoney = money
playerwins = 0
dealerwins = 0
playing = True


def Blackjack():
    global money
    global playerwins
    global dealerwins
    
    numbers = [['| A     |', '|     A |'], ['| 2     |', '|     2 |'], ['| 3     |', '|     3 |'], ['| 4     |', '|     4 |'], ['| 5     |', '|     5 |'], ['| 6     |', '|     6 |'], ['| 7     |', '|     7 |'], ['| 8     |', '|     8 |'], ['| 9     |', '|     9 |'], ['| 10    |', '|    10 |'], ['| J     |', '|     J |'], ['| Q     |', '|     Q |'], ['| K     |', '|     K |']]
    suits = ["|   ♣   |", "|   ♦   |", "|   ♥   |", "|   ♠   |"]
    card = ["┌───────┐", "|       |", "└───────┘"]
    blankcard = ['| ?     |', "|   ?   |", '|     ? |']
    
    play = True
    play1 = True
    placebet = True
    bet = 0
    
    while placebet == True:
        print()
        bet = int(input("How much would you like to bet? £"))
        if bet > money:
            print()
            print("You do not have that much money. Currently you have £" + str(money))
        else:
            placebet = False
    
    player = []
    dealer = []
    playercards = []
    dealercards = []
    playerscore = 0
    dealerscore = 0
    
    ace = 11


    for i in range(100):
        print()

    for i in range(2):
        curcard = []
        number = str(random.randint(0, 12))
        curcard.append(number)
        suitnum = str(random.randint(0,3))
        curcard.append(suitnum)
        player.append(curcard)
        
    for i in range(2):
        curcard = []
        number = str(random.randint(0, 12))
        curcard.append(number)
        suitnum = str(random.randint(0,3))
        curcard.append(suitnum)
        dealer.append(curcard)

    ace = 11
    for j in range(2):
        playerscore = 0
        for i in range(len(player)):
            if player[i][0] == "10":
                playerscore = playerscore + 10
            elif player[i][0] == "11":
                playerscore = playerscore + 10
            elif player[i][0] == "12":
                playerscore = playerscore + 10
            elif player[i][0] == "0":
                if ace == 11:
                    playerscore = playerscore + 11
                elif ace == 1:
                    playerscore = playerscore + 1
            else: 
                playerscore = playerscore + int(player[i][0]) + 1
            if playerscore > 21:
                ace = 1

    print("Your cards are: ")

    time.sleep(2)

    playercards.append(card[0] + card[0])
    playercards.append(numbers[int(player[0][0])][0] + numbers[int(player[1][0])][0])
    playercards.append(card[1] + card[1])
    playercards.append(suits[int(player[0][1])] + suits[int(player[1][1])])
    playercards.append(card[1] + card[1])
    playercards.append(numbers[int(player[0][0])][1] + numbers[int(player[1][0])][1])
    playercards.append(card[2] + card[2])

    for i in range(7):
        print(playercards[i])
    print()

    print("Value:", playerscore)

    print()

    time.sleep(2)

    print("Dealer's cards are: ")

    time.sleep(2)

    dealercards.append(card[0] + card[0])
    dealercards.append(numbers[int(dealer[0][0])][0] + numbers[int(dealer[1][0])][0])
    dealercards.append(card[1] + card[1])
    dealercards.append(suits[int(dealer[0][1])] + suits[int(dealer[1][1])])
    dealercards.append(card[1] + card[1])
    dealercards.append(numbers[int(dealer[0][0])][1] + numbers[int(dealer[1][0])][1])
    dealercards.append(card[2] + card[2])

    ace = 11
    for j in range(2):
        dealerscore = 0
        for i in range(len(dealer)):
            if dealer[i][0] == "10":
                dealerscore = dealerscore + 10
            elif dealer[i][0] == "11":
                dealerscore = dealerscore + 10
            elif dealer[i][0] == "12":
                dealerscore = dealerscore + 10
            elif dealer[i][0] == "0":
                if ace == 11:
                    dealerscore = dealerscore + 11
                elif ace == 1:
                    dealerscore = dealerscore + 1
            else: 
                dealerscore = dealerscore + int(dealer[i][0]) + 1
                if dealerscore > 21:
                    ace = 1

    print(card[0] + card[0])
    print(numbers[int(dealer[0][0])][0] + blankcard[0])
    print(card[1] + card[1])
    print(suits[int(dealer[0][1])] + blankcard[1])
    print(card[1] + card[1])
    print(numbers[int(dealer[0][0])][1] + blankcard[2])
    print(card[2] + card[2])

    print()

    print("Value: ?")

    print()
        
    while play == True:
        ace = 11
        for j in range(2):
            playerscore = 0
            for i in range(len(player)):
                if player[i][0] == "10":
                    playerscore = playerscore + 10
                elif player[i][0] == "11":
                    playerscore = playerscore + 10
                elif player[i][0] == "12":
                    playerscore = playerscore + 10
                elif player[i][0] == "0":
                    if ace == 11:
                        playerscore = playerscore + 11
                    elif ace == 1:
                        playerscore = playerscore + 1
                else: 
                    playerscore = playerscore + int(player[i][0]) + 1
                if playerscore > 21:
                    ace = 1
        if playerscore <= 21:
            question = str(input("Stick or Twist? "))
            question = question.lower()
            if question == "twist":
                for i in range(100):
                    print()
                    
                curcard = []
                number = str(random.randint(0, 12))
                curcard.append(number)
                suitnum = str(random.randint(0,3))
                curcard.append(suitnum)
                player.append(curcard)
                
                print("Your cards are:")
                time.sleep(3)
                playercards[0] = playercards[0] + card[0]
                playercards[1] = playercards[1] + numbers[int(player[-1][0])][0]
                playercards[2] = playercards[2] + card[1]
                playercards[3] = playercards[3] + suits[int(player[-1][1])]
                playercards[4] = playercards[4] + card[1]
                playercards[5] = playercards[5] + numbers[int(player[-1][0])][1]
                playercards[6] = playercards[6] + card[2]
                
                for i in range(7):
                    print(playercards[i])
                for j in range(2):
                    playerscore = 0
                    for i in range(len(player)):
                        if player[i][0] == "10":
                            playerscore = playerscore + 10
                        elif player[i][0] == "11":
                            playerscore = playerscore + 10
                        elif player[i][0] == "12":
                            playerscore = playerscore + 10
                        elif player[i][0] == "0":
                            if ace == 11:
                                playerscore = playerscore + 11
                            elif ace == 1:
                                playerscore = playerscore + 1
                        else: 
                            playerscore = playerscore + int(player[i][0]) + 1
                        if playerscore > 21:
                            ace = 1
                print()
                print("Value:", playerscore)
                
                print()
                print("Dealer's cards are:")

                print(card[0] + card[0])
                print(numbers[int(dealer[0][0])][0] + blankcard[0])
                print(card[1] + card[1])
                print(suits[int(dealer[0][1])] + blankcard[1])
                print(card[1] + card[1])
                print(numbers[int(dealer[0][0])][1] + blankcard[2])
                print(card[2] + card[2])
                
                print()
                print("Value: ?")
                    
            elif question == "stick":
                break
                
            else:
                print()
            if playerscore > 21:
                print()
                print("You are bust!")
                time.sleep(5)
                break
    for i in range(100):
        print()

    print("Your card's are: ")
    for i in range(7):
        print(playercards[i])
    print()
    if playerscore > 21:
        print("Value: Bust")
    else:
        print("Value:", playerscore)
    print()
    print("Dealer's card's are: ")
    for i in range(7):
        print(dealercards[i])
    print()
    if dealerscore > 21:
        print("Value: Bust")
    else:
        print("Value:", dealerscore)

    print()
    print()
    print("Dealer is deciding what to do...")

    time.sleep(5)

    while play1 == True:
        ace = 11
        for j in range(2):
            dealerscore = 0
            for i in range(len(dealer)):
                if dealer[i][0] == "10":
                    dealerscore = dealerscore + 10
                elif dealer[i][0] == "11":
                    dealerscore = dealerscore + 10
                elif dealer[i][0] == "12":
                    dealerscore = dealerscore + 10
                elif dealer[i][0] == "0":
                    if ace == 11:
                        dealerscore = dealerscore + 11
                    elif ace == 1:
                        dealerscore = dealerscore + 1
                else: 
                    dealerscore = dealerscore + int(dealer[i][0]) + 1
                    if dealerscore > 21:
                        ace = int(dealer[i][0]) + 1
                    if dealerscore > 21:
                        ace = 1
        if dealerscore <= 16:
            
            for i in range(100):
                    print()
            print("Dealer Twisted")
            print()
            print("Your cards are:")
            for i in range(7):
                print(playercards[i])
            print()
            if playerscore > 21:
                print("Value: Bust")
            else:
                print("Value:", playerscore)
                    
            curcard = []
            number = str(random.randint(0, 12))
            curcard.append(number)
            suitnum = str(random.randint(0,3))
            curcard.append(suitnum)
            dealer.append(curcard)
                    
            dealercards[0] = dealercards[0] + card[0]
            dealercards[1] = dealercards[1] + numbers[int(dealer[-1][0])][0]
            dealercards[2] = dealercards[2] + card[1]
            dealercards[3] = dealercards[3] + suits[int(dealer[-1][1])]
            dealercards[4] = dealercards[4] + card[1]
            dealercards[5] = dealercards[5] + numbers[int(dealer[-1][0])][1]
            dealercards[6] = dealercards[6] + card[2]
            

            ace = 11
            for j in range(2):
                dealerscore = 0
                for i in range(len(dealer)):
                    if dealer[i][0] == "10":
                        dealerscore = dealerscore + 10
                    elif dealer[i][0] == "11":
                        dealerscore = dealerscore + 10
                    elif dealer[i][0] == "12":
                        dealerscore = dealerscore + 10
                    elif dealer[i][0] == "0":
                        if ace == 11:
                            dealerscore = dealerscore + 11
                        elif ace == 1:
                            dealerscore = dealerscore + 1
                    else: 
                        dealerscore = dealerscore + int(dealer[i][0]) + 1
                        if dealerscore > 21:
                            ace = int(dealer[i][0]) + 1
                        if dealerscore < 21:
                            ace = 1        
                    
            print()
            print("Dealer's cards are:")
            print()
            time.sleep(3)
        
            for i in range(7):
                print(dealercards[i])
            print()
            print("Value:", dealerscore)
            print()
            print("Dealer is deciding what to do...")
            time.sleep(3)
        elif dealerscore > 21:
            print()
            print("Dealer Is Bust!")
            
            break
        elif dealerscore > 16:
            print()
            print("Dealer Stuck!")
            break
    print()
    print()
    if dealerscore > 21:
        if playerscore > 21:
            print("You both went bust!")
            money = money - bet
        else:
            playerwins = playerwins + 1
            print("You won with", playerscore, "because the dealer went bust")
            money = money + bet
    elif playerscore > 21:
        if dealerscore > 21:
            print("You both went bust!")
            money = money - bet
        else:
            dealerwins = dealerwins + 1
            print("Dealer won with", dealerscore, "because you went bust")
            money = money - bet
    elif len(player) == 5:
        if len(dealer) == 2 and dealerscore == 21:
            dealerwins = dealerwins + 1
            print("You had 5 cards, but the dealer beat you with a blackjack")
            money = money - bet
        else:
            playerwins = playerwins + 1
            print("You automatically won as you had 5 cards!")
            money = money + bet
    elif len(dealer) == 5:
        if len(player) == 2 and playerscore == 21:
            playerwins = playerwins + 1
            print("The dealer had 5 cards, but you beat the dealer with a blackjack")
            money = money + bet
        else:
            dealerwins = dealerwins + 1
            print("The dealer automatically won as they had 5 cards!")
            money = money - bet
    elif dealerscore > playerscore:
        dealerwins = dealerwins + 1
        print("Dealer got " + str(dealerscore) + ", beating you by " + str(dealerscore - playerscore))
        money = money - bet
    elif playerscore > dealerscore:
        playerwins = playerwins + 1
        print("You got " + str(playerscore) + ", beating the dealer by " + str(playerscore - dealerscore))
        money = money + bet
    elif playerscore == dealerscore:
        print("You both had a score of", playerscore)
    
while playing == True:
    if money == 0: break
    print()
    print()
    print("Money: £" + str(money))
    print()
    game = input("Do you want to play? ")
    game = game.lower()
    if game == "yes":
        Blackjack()
    if game == "no":
        playing = False

print()
print()
if money > initialmoney:
    print("You made a profit of £" + str(money - initialmoney))
elif money == initialmoney:
    print("You made no profit.")
elif initialmoney > money:
    print("You made a loss of £" + str(initialmoney - money))