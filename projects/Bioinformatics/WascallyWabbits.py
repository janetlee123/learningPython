#Given : n <= 40 and k <=5 
#Returns:  The total number of rabbit pairs that will be present after n
# months, if we begin with 1 pair and in each generation, every pair of reproduction-age rabbits produces a litter of k
# rabbit pairs (instead of only 1 pair).

#Initializing the values 
n=41
k=6
f1=1
f2=1
offspring=0


#Obtaining values from user asking user again where n > 40 or k > 5 
while n > 40: 
    n=int(input("Please enter number of months < 40 : "))

while k > 5:
    k = int(input("Please enter number of rabbit pairs < 5: "))

#Calculating population 
for x in range(n-1):
    fn=f1+offspring
    #Update Values 
    f2=f1
    f1=fn 
    offspring=f2*k

print(str(fn))




    

    
    


