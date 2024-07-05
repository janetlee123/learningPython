# identifying if a string is a palindrome 
# input : string to evaluate 
# output boolean value 


def identify_palindrome(string):
    #Check if string is a string 
    if not isinstance(string, str):
        raise TypeError("string inputted must be a string")
    
    string1=""
    #Extracting only the letters from string 
    for char in string: 
        if char.isalpha() == True: 
            string1=string1+char

    #Making all strings uppercase preventing case changes in palindrome
    string1 = string1.upper()

    #Inverting the string1 
    string2 = string1[::-1]

    if string1 == string2: 
        return True 
    return False 

#Test cases 
# print(identify_palindrome("racecar"))
# print(identify_palindrome("a2cd"))
print(identify_palindrome("Go hang a salami - I'm a lasagna hog"))

