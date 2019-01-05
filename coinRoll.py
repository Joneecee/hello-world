# coinRoll.py
# 4/1/19
# Takes input from the user as weight of a particular coin
# Converts that weight to the number of coins
# Calculates the number of coin rolls that number of coins can produce
# Python version 3.6.8

def cents(num):
    weightCents = float(input("Weight of cents?"))
    numCents = int(weightCents / 2.5)
    rollCents = int(numCents / 50)
    if rollCents > 1:
        print(str(weightCents) + " grams of cents would make " + str(rollCents) + " rolls of cents!")
    else:
        print(str(weightCents) + " grams of cents would make 1 roll of cents!")

def nickels(num):
    weightNickels = float(input("Weight of cents?"))
    numNickels = int(weightNickels / 5)
    rollNickels = int(numNickels / 40)
    if rollCents > 1:
        print(str(weightNickels) + " grams of nickels would make " + str(rollNickels) + " rolls of nickels!")
    else:
        print(str(weightNickels) + " grams of nickels would make 1 roll of nickels!")

def dimes(num):
    weightDimes = float(input("Weight of dimes?"))
    numDimes = int(weightDimes / 2.26)
    rollDimes = int(numDimes / 50)
    if rollDimes > 1:
        print(str(weightDimes) + " grams of dimes would make " + str(rollDimes) + " rolls of dimes!")
    else:
       print(str(weightDimes) " grams of dimes would make 1 roll of dimes!" )

def quarters(num):
    weightQuarters = float(input("Weight of quarters?"))
    numQuarters = int(weightQuarters / 5.65)
    rollQuarters = int(numQuarters / 40)
    if rollQuarters > 1:
        print(str(weightQuarters) + " grams of quarters would make " + str(rollQuarters) + " rolls of quarters!")
    else:
        print(str(weightQuarters) + " grams of quarters would make 1 roll of quarters!")

# Ask the user which type of coin they want to calculate the number of rolls of

def typeCoin(int):
    typeCoin = int(input("Which coin do you want to calculate the weight of?\n"
                     "1 for Cents\n"
                     "2 for Nickels\n"
                     "3 for Dimes\n"
                     "4 for Quarters\n"
                     "5 to quit")

    if typeCoin == 1:
               cents()
    elif typeCoin == 2:
               nickels()
    elif typeCoin == 3:
               dimes()
    elif typeCoin == 4:
               quarters()
    elif typeCoin == 5:
                   break
    else:
               print("Please select a type of coin to calculate.")

while typeCoin != 5:
                   typeCoin()




    
