def factorial (n):
    if n ==0 or n ==1:
        return 1
    else:
        return n * factorial (n-1)
    
    
print (factorial(8))



#another 

def fact (n):
    result = 1
    for i in range (2,n+1):
        result = result * i
        
    return result

print(fact(5))