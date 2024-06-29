# Input: path to text file 
# Output: print message with: 
# - total number of words 
# - top 20 most frequent words
# - number of occurrences for top 20 
import re 

wordlist=[]
dictofwords={}

def count_words(filepath):
    with open(filepath, "r") as f: 
        for line in f: 
            wordlist.extend(re.split(" .!?;:",line))
    
    print(f"wordlist: {wordlist}")

    for word in wordlist: 
        dictofwords.append(word)

    print(f'dictionary: {dictofwords}')
print(count_words("textfile.txt"))
