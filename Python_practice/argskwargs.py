'''args and kwargs 

when we do not have a fix numbers of argumnets

so args is a listand tuples and kwarfgs is a dictionary and if we ewant names paramters  '''



def add (*args):
    print(sum(args))
    print (args)

add (1,2,3)

def checkkargs (**kwargs):
    print(kwargs)
    for k,v in kwargs.items():
        print(k,v)

checkkargs(name="krish",location="banglore")



'''lambda- lambda are anonymus funcitons '''


add_numbers =lambda n1,n2,n3 : n1+n2+n3
print(add_numbers(1,3,5))


check_even = lambda n : n%2==0

if check_even (7):
    print("yes it is")

else:
    print("nO")