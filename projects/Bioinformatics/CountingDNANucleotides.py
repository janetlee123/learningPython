#Given: a string s of up to 1000 nt.
#Returns: Four integers counting the number of times symbols "A", "C", "G", and "T" occur in s

s = input("Please enter the string:") 
A=G=C=T=0 
while len(s)>1000:
    s = input("Please enter a string of less than 1000 nt in length:")

for element in s:
    if element=="A":
        A=A+1
    elif element == "G":
        G=G+1
    elif element == "C":
        C=C+1 
    elif element == "T":
        T=T+1
    else: 
        print ("ERROR: string contains letter other than ACTG")
        exit

print(str(A)+" "+str(C) + " " +str(G)+ " " + str(T))

  