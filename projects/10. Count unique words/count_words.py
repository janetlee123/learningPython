# Input: path to text file 
# Output: print message with: 
# - total number of words 
# - top 20 most frequent words
# - number of occurrences for top 20 
import os
from collections import Counter

wordlist=[]
dictofwords={}

def count_words(filepath):
    with open(filepath, "r") as f: 
        for line in f: 
            line = line.lower()
            wordlist.extend(line.split(" " or '.' or "!" or ";" or "?" or '\n'))
    
    countthis = Counter(wordlist) 
    mostcomm = countthis.most_common(20)

    filename = os.path.basename(filepath).split('/')[-1]
    print(f"20 MOST COMMON WORDS IN {filename}")
    
    num = 1
    for x,y in mostcomm:
        print(f"{num}: {x}: {y}")
        num+=1 

#count_words('/workspaces/learningPython/projects/textfile.txt')
