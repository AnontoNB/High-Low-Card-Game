# Name: Anonto Barua
# Email: anontob@my.yorku.ca
# Student ID: 218 949 412
# Purpose: To implement a simple card game where the player starts with 100 points, and they have ten attempts (rounds)
# to reach 500 points to win. Each round, the player "bets" any amount of points which is between the lowest amount they
# can bet, and the total amount of points they have. If they can't reach the 500 points before 10 rounds, or before
# their points reach 0,they lose! Best of luck to all players!

import random

def getCardValue():
    return random.randint(2, 14)

def getCardStr(cardValue):
    if cardValue <= 9:
        return str(cardValue)
    elif cardValue == 10:
        return "T"
    elif cardValue == 11:
        return "J"
    elif cardValue == 12:
        return "Q"
    elif cardValue == 13:
        return "K"
    elif cardValue == 14:
        return "A"

def getHLGuess():
    while True:
        guess = input("High or Low (H/L)?:")
        if guess == "L" or guess == "l":
            return "LOW"
        elif guess == "H" or guess == "h":
            return "HIGH"

def getBetAmount(maximum):
    bet = 0
    while not 1 <= bet <= maximum:
        bet = int(input("Input bet amount:"))
        if 1 <= bet <= maximum:
            return bet
        else:
            print("Please try again. Remember to only enter non-negative, non-zero numbers.")

def playerGuessCorrect(card1, card2, betType):
    # card 2 same as 1 bet type anything
    if card1 == card2:
        return False
    # card 2 higher than 1 bet type lower
    elif betType == "LOW" and card2 > card1:
        return False
    # card 2 lower than 1 bet type higher
    elif betType == "HIGH" and card2 < card1:
        return False
    # card 2 lower than 1 bet type lower
    elif betType == "LOW" and card2 < card1:
        return True
    # card 2 higher than 1 bet type higher
    elif betType == "HIGH" and card2 > card1:
        return True

# Game start with message and rules
print("""--- Welcome to High-Low ---
Start with 100 points. Each round a card will be drawn and shown.
Select whether you think the 2nd card will be Higher or Lower than the 1st card.
Then enter the amount you want to bet.
If you are right, you win the amount you bet, otherwise you lose.
Try to make it to 500 points within 10 tries.""")

# Initialized values needed at start of every game
points = 100
roundCnt = 0

# Loops another round each time
while True:
    # Makes sure the game doesn't go over 10 rounds
    if roundCnt < 10:
        roundCnt += 1

    # Get the first randomized card
    initial = getCardValue()
    print("\n-------------------------------------\nOVERALL POINTS: ", points, " ROUND ", roundCnt, "/ 10")
    print("First card is a [", getCardStr(initial), "]")

    # Let the user guess if card is lower or higher than random card
    betChoice = str(getHLGuess())

    # Get the amount they'll be betting, based off their current total of points
    betAmt = int(getBetAmount(points))

    # Get the 2nd randomized number
    guessRes = getCardValue()
    print("Second card is a [", getCardStr(guessRes), "]")

    # Call the method that'll compare both card values and use the string guess of the user to return a boolean value
    boolGuess = bool(playerGuessCorrect(initial, guessRes, betChoice))

    # Round results
    if boolGuess == False:
        print("Card 1 [", getCardStr(initial), "] Card 2 [", getCardStr(guessRes), "] - You bet \'", betChoice, "\' for ", betAmt, " - YOU LOST")
        points -= betAmt
    elif boolGuess == True:
        print("Card 1 [", getCardStr(initial), "] Card 2 [", getCardStr(guessRes), "] - You bet \'", betChoice, "\' for ", betAmt, " - YOU WON")
        points += betAmt

    # Ends the game if you reach 10 rounds before reaching 500 points, if you reach less than or equal to 0 points, or
    # if you reach more than or equal to 500 points,
    if roundCnt == 10 and not points >= 500:
        print("-----------LOSE-------------\nONLY *", points, "* POINTS IN ", roundCnt, " ROUNDS!\n-----------------------------")
        break
    elif points <= 0:
        print("-----------LOSE-------------\nYOU HAVE *", points, "* POINTS AFTER ", roundCnt, " ROUNDS!\n-----------------------------")
        break
    elif points >= 500:
        print("-----------WIN-------------\nYOU HAVE *", points, "* POINTS AFTER ", roundCnt, " ROUNDS!\n-----------------------------")
        break
