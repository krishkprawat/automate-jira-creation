a,b = 0,1
for i in range(8):
    c = a+b
    print(c, end =' ') #Here, end=' ' tells Python to print a space instead of a newline after each number
    a,b=b,c

