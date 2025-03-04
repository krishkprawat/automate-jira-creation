# name = "gobs"
# for i in name:
#     print(i)
#     if(i=="b"):
#         print("this is soemthing special")
        

# colors = ["Red","blue","yesllow"]
# for color in colors:
#     print(color)
#     for i in color:
#         print (i)

'''range'''

# for k in range(2,5): #start , stop , step
#     print (k+1)


#counting vowels in a given word --- 

vowels=['a','e','i','o','u']
string = "ishika"
count =0
for char in string:
    if char in vowels:
        count +=1
print(count)


#Counting the Number of Occurrences of a Character in a String


name="ishika"
character="k"
count = 0
for char in name:
    if char==character:
        count +=1
print(count)  #1


#writing a fibonaci series :

a,b=0,1
for i in range (8):
    c = a+b
    print(c)
    a,b = b,c

fin= [0,1]

for i in range(8):
    fin.append(fin[-1]+fin[-2])

print(fin)



#finding a max num in list

numbers =[1,52,6,5,6,0,885]
maxnum = numbers[0]

for num in numbers:
    if num > maxnum:
        maxnum = num
print(maxnum)



#converting a list into a string


# list = ["k","r","i","s","h","i","k","a"]
# string = ''.join(list)
# print ( string)

#adding two list element together

list_A = [1,2,3]
list_B = [3,4,5]

result = []
for i in range(0,3):
    result.append(list_A[i]+list_B[i])
print(result)