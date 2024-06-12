# determine probability of rolling dice outcomes 
# use monte carlo simulation 
# input: variable number of arguments for sides of dice 
# output: table of probability of each possible outcome 
# ie: roll_dice(4,6,6) - 1 four sided and 2 six sided dice 
import random

def roll_dice(*arg):
    n_simulations = 1000000
    dice = arg
    count = 1
    maxroll = sum(dice)
    probability = []
    listoftotals=[]

    for n in range (len(dice),maxroll+1): 
        listoftotals.append(n)
        probability.append(0)


    while count <= n_simulations:
        total = get_dice_roll(arg)
        index = total-len(dice)
        probability[index]=probability[index]+1
        count+=1 

    updatedprobability = [round(((x/n_simulations)*100),2) for x in probability]
    
    x=0
    while x < len(probability):
        print(f'{listoftotals[x]} {updatedprobability[x]}%')
        x+=1


def get_dice_roll(args):
    listdice = args 
    dicetotal=0
    for dice in listdice: 
        diceroll=random.randint(1,dice)
        dicetotal=dicetotal+diceroll
        
    return dicetotal

#Checking the function 
roll_dice(4,4,6)