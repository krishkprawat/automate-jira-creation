def check(s):
    s = s.lower()
    left = 0
    right = len(s)-1
    
    while left < right :
        if s[left] != s [right]:
            return  "number is  not palidnrome"
            
        left += 1
        right -= 1
        
    return "palindrome yes!!!"

print(check("krish"))
print(check ("madam"))