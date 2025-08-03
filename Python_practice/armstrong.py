'''ok so armstrong number are the numbers which is equal to the sum of its digits raised to the power of its digits'''

def checkarm(num):
    n = num   #let origianl value remain same which is num --- so chncahge num to n for modifying
    total = 0
    nod = len(str(n))
    while n > 0 :
        ld = n % 10
        total = total+(ld ** nod)
        n = n // 10
    return total == num   # num is original value which is not changed

print(checkarm(153))    
    
    
'''now to find the armstrong in given range'''

# # def check(start,end):
#     result = []
    
#     for  n in range (start, end + 1):
#         num_str = str(n)
#         num_digit= len(num_str)
        
#         total = 0
#         for digit in num_str:
#             total = total + int(digit) ** num_digit
#         if total == n:
#             result.append(n)
#     return result


# print (check(2,1000))    