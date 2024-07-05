# function that sorts the words in a string 
# input string of words separated by spaces 
# output string of words sorted alphabetically 

def sort_words(string):
    sepstr = string.split()
    print(sepstr)

    sepstr.sort(key=str.lower)
    print(sepstr)
    
    strreturn = ""
    for word in sepstr:
        strreturn=strreturn +" " + word 
    return strreturn 

print(sort_words("banana ORANGE apple"))

