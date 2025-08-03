# def check (num):
#     num_Str = str(num)
#     reverse_num =  num_Str[::-1]
    
#     if num_Str ==  reverse_num:
#         return True
#     else:
#         return False
    
    
# print (check(156))




#real dsa

def check(num):
    
    n = num
    result =  0
    while n > 0 :
        ld =  n %10 # get the last digit
        result = (result * 10 ) + ld #add digit in reverse
        n = n //10    # remove last difit from number 
    return num == result

print(check(1230021))