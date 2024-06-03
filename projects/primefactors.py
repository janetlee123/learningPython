# function called get_prime_factors that returns a list of all primes to be multiplied to obtain number 
def get_prime_factors(num):
    primes = []
    divisor = 2 
    while divisor <= num:
        if num % divisor == 0:
            primes.append(divisor)
            num = num//divisor
        else:
            divisor +=1 
    return primes 

print(get_prime_factors(630)) 
