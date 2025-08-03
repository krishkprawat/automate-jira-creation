# check number is prime or not???


import math
def check_prime(num):
    if num <=1:
        return False
    
    for i in range (2, int(math.sqrt(num)) +1 ):
        if num % i == 0:
            return False
        
    return True
        
        
        
print (check_prime(3))

''' so we use root n here because all factors repeats after root n . so if any number is divisble till root n then there will be 
more after root n . and if we found no one divide then its a prime number 

ex = 36 
root n is 6 so from 2 to 6 there are multiple divisor  of  6 then there will be no after 6 also...'''

