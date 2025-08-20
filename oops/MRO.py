'''so mro is method resolution order used in 
python uses Method Resolution Order (MRO).
The order is left to right in inheritance: Child(ParentA, ParentB) → looks into ParentA first, then ParentB.

So, ParentA.work() is used.


Definition: The order in which Python looks for a method in classes during inheritance.

Key idea: It decides which parent’s method to call if multiple parents have the same method.

Decided at: Class creation time (not runtime).

used when multuple parent have same method and  and child doesnt override it.'''

#so, MRO is about lookup order.
#Overriding is about redefining behavior.

class ParentA:
    def work(self):
        print("Work from ParentA")

class ParentB:
    def work(self):
        print("Work from ParentB")

class Child(ParentA, ParentB):
    pass

c = Child()
c.work()  #here parent a mehtod will  run br=ecasue parent a is in first in order
