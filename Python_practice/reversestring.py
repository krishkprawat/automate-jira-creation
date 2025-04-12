'''take input as string and make a function and reverse it '''

name = input("enter the name here")

def reverse1(name):
    reversed=name[::-1]
    return(reversed)

print(reverse1(name))


#using the reverse method -- first convert string to list then do method reverse and finaly join back into a string.

# note - reverse onnly works in a list , dont use it in string, if want ot use in string then [:-1] is a wayto do it.

girl = input("enter girl name")

def change(girl):
    newgirl= list(girl)
    newgirl.reverse()
    return ("".join(newgirl))

print(change(girl))






