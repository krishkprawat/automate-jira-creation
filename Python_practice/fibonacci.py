a,b = 0,1
for i in range(8):
    c = a+b
    print(c, end =' ') #Here, end=' ' tells Python to print a space instead of a newline after each number
    a,b=b,c

print ("----------other way---------------")

fib =[0,1]

for i in range(8):
    fib.append(fib[-1]+fib[-2])
print(fib)
print(' '.join(map(str,fib)))   # we can do this lso to convert list intp the string 
    
