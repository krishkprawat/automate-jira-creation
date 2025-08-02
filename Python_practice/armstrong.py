'''ok so armstrong number are the numbers which is equal to the sum of its digits raised to the power of its digits'''


# def check_Armstrong(num):
#     num_str = str(num)
#     n = len(num_str)
    
#     total = 0
    
#     for digit in num_str:
#         total = total+ int(digit) ** n 
#     return total == num

# print(check_Armstrong(153))
    
    
    
'''now to find the armstrong in given range'''

def check(start,end):
    result = []
    
    for  n in range (start, end + 1):
        num_str = str(n)
        num_digit= len(num_str)
        
        total = 0
        for digit in num_str:
            total = total + int(digit) ** num_digit
        if total == n:
            result.append(n)
    return result


print (check(2,1000))    