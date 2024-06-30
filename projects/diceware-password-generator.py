#creates a list of 6 random words using diceware to be used as password 
# copied MIT wordlist.txt from https://gist.github.com/a6994f236ac07ebb45e6eca7a7312e9e.git 

#TO USE: 
# enter the file path of the wordlist.txt into the passwordgenerator

import random 
listofwords=[]
password=[]
i=1 

def passwordgenerator(filepath):
    with open(filepath, "r") as f:
        for line in f: 
            if len(line) >= 4: 
                listofwords.extend(line.split()) 

    for i in range(1,6):
        randint = random.randint(1,len(listofwords))
        password.append(listofwords[randint])
        i=i+1

    print(password)    

# checking to see if it works 
passwordgenerator("/workspaces/learningPython/projects/wordlist.txt")






