from matplotlib import pyplot as plt
import time
import random

class Player():
    def __init__(self,colour):
        self.colour=colour
        self.ownedcountries=[]
    def attack(self,targetCountry,attackerCountry):
        """
        both targetCountry and attackerCountry are locations (x,y)
        """
        if targetCountry not in self.ownedcountries:
            print("You don't own this country")
            return False
        if ((attackerCountry[0]-targetCountry[0])**2+(attackerCountry[1]-targetCountry[1])**2)**0.5==1:
            # Input of how many troops to deploy
            while True:
                attackingTroops=int(input("How many troops would you like to send in? (1,2 or 3)\n"))
                if attackingTroops in [1,2,3]:
                    break
                else:
                    print("\nPick 1, 2 or 3 troops\n") # need to have a check if the attacker country has this many troops - also detract these troops
            targetCountryTroops=2 # how many troops the target country has
            if targetCountryTroops==1:
                defendingTroops=1
            else:
                defendingTroops=2
            # attacking throws
            attackerthrows=[]
            for n in range(attackingTroops):
                attackerthrows.append(random.randint(1,6))
            # defender throws
            defenderthrows=[]
            for n in range(defendingTroops):
                defenderthrows.append(random.randint(1,6))
            #sorting both throws from largest to smallest
            attackerthrows.sort(reverse=True)
            defenderthrows.sort(reverse=True)
            # seeing how many soilders each lost
            attackerLoss,targetloss=0,0
            if defendingTroops < attackingTroops:
                for n in range(defendingTroops):
                    if attackerthrows[n]>defenderthrows[n]:
                        targetloss+=1
                    else:
                        attackerLoss+=1
            else:
                for n in range(attackingTroops):
                    if attackerthrows[n]>defenderthrows[n]:
                        targetloss+=1
                    else:
                        attackerLoss+=1

            # unless country has been taken, after each fight, ask attacker if they want to resume (which loops back to begining of attack) or withdraw (it will say how many troops each have in total) 
        else:
            print("Countries are too far away")
            return False
    def moveTroops(self,oldCountry,newCountry):
        # check for path between countries
    def addTroop(self,numberOfTroopsToAdd):
        while numberOfTroopsToAdd!=0:
            addToCountry=input("Name a country you would like to add a troop to\n")
            if countries[addToCountry]["colour"]==self.colour:
                numberOfTroops=input("How many troops would you like to add here?\n")
                countries[addToCountry]["troops"]+=numberOfTroops
                numberOfTroopsToAdd-=numberOfTroops
            else:
                print("This is not your country!\n")
    def numberOfExtraTroops():
        numberOfCountries=0
        for country in countries:
            if countries[country]["colour"]==self.colour:
                numberOfCountries+=1
        numberOfTroops=numberOfCountries/3
        # impliment continents here
        # maybe impliment the card trade-ins


# All the countries
countries = {
    "Great Britain":{
    "location":(1,2),
    "troops":0,
    "colour":"b"
    },
    "France":{
    "location":(1,1),
    "troops":0,
    "colour":"b"
    },
    "Germany":{
    "location":(2,1),
    "troops":0,
    "colour":"k"
    },
    "Denmark":{
    "location":(2,2),
    "troops":0,
    "colour":"k"
    },
    "Spain":{
    "location":(1,0),
    "troops":0,
    "colour":"r"
    },
    "Portugal":{
    "location":(0,0),
    "troops":0,
    "colour":"r"
    },
    "Ireland":{
    "location":(0,2),
    "troops":0,
    "colour":"r"
    }
}

def displayMap() # display this after every change
    global countries
    name,x,y,colour=[],[],[],[]
    for country in countries:
        name.append(country+": "+str(countries[country]["troops"]))
        x.append(countries[country]["location"][0])
        y.append(countries[country]["location"][1])
        colour.append(countries[country]["colour"])
    fig, ax = plt.subplots()
    ax.scatter(x, y, colour)
    for i, txt in enumerate(name):
        ax.annotate(txt, (x[i], y[i]))



# =================== game =================== #
# establish players names and colours
noPlayers=input("How many players are there?\n")
selectedColours=[]
players={}
for n in range(noPlayers):
    while True:
        name=input(f"Player {n+1}, what is your name?")
        if name not in players:
            break
        else:
            print("Name taken\n")
    print("What colour do you want to be?")
    if "k" not in selectedColours:
        print("Black\t\tk")
    if "b" not in selectedColours:
        print(Blue"\t\tb")
    if "r" not in selectedColours:
        print(Red"\t\tr")
    if "g" not in selectedColours:
        print(Green"\t\tg")
    if "c" not in selectedColours:
        print(Cyan"\t\tc")
    if "m" not in selectedColours:
        print(Magenta"\t\tm")
    print("")
    colour=input()
    selectedColours.append(colour)
    players[name]=Player(colour)


# Claiming country
displayMap()


# People putting troops on each country untill all are taken - 30 troops each


# People adding troops to their land untill they have placed a certain amount

# for each player

# When have mutiple troops to divvy out - can call the addTroop function


# 







