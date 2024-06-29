#creates a list of 6 random words using diceware to be used as password 
# copied MIT wordlist.txt from https://gist.github.com/a6994f236ac07ebb45e6eca7a7312e9e.git 
import random 
wordlist=[]

def passwordgenerator():
    with open(wordlist.txt, "r") as f:
        for line in f: 
            wordlist.extend(line.split()) 

    print(wordlist[0])

passwordgenerator()






