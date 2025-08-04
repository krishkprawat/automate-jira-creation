#printn the factors of a number 
from math import *
def check(num):
    result = []
    for i in  range (1, int(sqrt(num))+1):
        if num % i == 0:
            result.append(i)
            if num//i != i:
                result.append(num//i)
    return result

print(check(36))

'''num = 36 , root n = 6
i  1  - 36    
    2- 18
    3- 12
    4- 9
    6- 6
     so now till 6 there are theess factors . so append  all i in result but make sure in last we hav two 6
     so not include last 6 two times. so use if num//i != i then append num//i
'''