'''What is Method Overloading?

In general OOP (like Java/C++):

Same method name

Different parameters (number or type)

so in python we use args kwargs to achive overloading
'''

def add (*args):
    print(sum(args))
    print (args)

add (1,2,3)

def checkkargs (**kwargs):
    print(kwargs)
    for k,v in kwargs.items():
        print(k,v)

checkkargs(name="krish",location="banglore")