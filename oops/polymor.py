# poly means many forms
'''Polymorphism = It means: the same method or operation can have 
different behaviors depending on the object.'''

'''Inheritance → Relationship between classes (child inherits parent features).

Polymorphism → Behavior of methods depending on the object.

Inheritance is about code reuse, polymorphism is about method behavior flexibility.'''

'''
Types of Polymorphism in Python

Duck Typing ("If it walks like a duck and quacks like a duck, treat it like a duck")

Operator Overloading (+, *, etc. behave differently for numbers/strings/lists).

Method Overriding (Child class changes Parent class method).

Method Overloading (not directly supported in Python, but can mimic using *args).
'''
#exmaple - length
print(len("Krish"))   # 5 (counts characters)
print(len([1, 2, 3])) # 3 (counts list elements)



class APITest:
    def run_test(self):
        print("Running API Test")

class UITest:
    def run_test(self):
        print("Running UI Test")

class HybridTest(APITest, UITest):
    def run_test(self):
        print("i am my own ")     #child replaced the method

h = HybridTest()
h.run_test()   # "Running API Test" (because APITest comes first in MRO)
