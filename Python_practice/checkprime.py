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

#find all prime numbers in given range

def findallprime (start, end):
    
    for n in range (start, end +1):
        if  n <=2 :
            continue
        
        for i in range (2, int(math.sqrt(n))  +1):
            if n % i ==0 :
                break
            
        else:
            print(n)
            


print(findallprime(0,2))                