# Given: DNA string t length at most 1000 nt. 
# Returns: transcribed RNA string of t, new_string

new_string=""

#Takes the string of DNA and places it in variable t
t=input ("Please enter string of DNA:")

#Checks to see if the string t contains less than 1000 characters
#If so, then it asks user to re-enter a string of < 1000 characters long
while len(t) > 1000: 
    print("Please enter a string of less than 1000 nt long")
    t=input("Please enter string of DNA:")

#transcribing DNA to RNA requires all T nucleotides to be changed to U
#Loops through every character in the string t
# if the character is equal to T, then the character is exchanged for a U
for element in t:
    if element == "T":
        new_string=new_string+"U"
    elif element =="C" or element =="G" or element == "A": 
        new_string=new_string+element
    #If the nucleotide is not an A,C,T, or G, then error message shows, code exits 
    else:
        print("Error in DNA sequence, nucleotide: "+element+ "does not exist")
        exit

print(new_string)

    


