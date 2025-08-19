'''Reverse only the alphabetic characters in the string while keeping
    spaces and any non-letter characters in their original positions.
'''

'''step 1 - collct all letters 
step 2 - reverse them 
step 3 - go to original string
if character is letter - take from reversed list 
if character is not a letter - keep it as it is

step 4 - build final string'''


def collect(s):
    letters = []    #this is reversed list
    for c in s:
        if c.isalpha():
            letters.append(c)
    letters.reverse()

    result = ""   #final string
    for c in s:
        if c.isalpha():
            result += letters.pop(0)    #if alpha then add the reversed leeters in to te result string
        else:
            result += c   #if not alpha then add as it is
    return result

print(collect("a,b$c"))


'''other approach'''

def reverse_letters(s):
    chars = list(s)  #change stirng to list beacuse we have to swap the characters an string is imutable

    left,right = 0, len(chars)-1  #pointer initialize

    while left < right : 
        if not chars[left].isalpha():   #if left character is not letter then move one step to right
            left +=1
        
        elif not chars[right].isalpha(): #if right  character is not letter then move one step to left
            right -=1

        else:   

            chars[left], chars[right]=chars[right], chars[left]   #if both are letters then swap it 
            left+=1
            right-=1

        return "".join(chars)    # join is a sting method it takes iterables and concatenate then
        #into a single sting using the seperator ""
    
print(reverse_letters("a,b$c"))