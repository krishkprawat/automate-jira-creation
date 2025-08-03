def check (num):
    num_Str = str(num)
    reverse_num =  num_Str[::-1]
    
    if num_Str ==  reverse_num:
        return True
    else:
        return False
    
    
print (check(156))