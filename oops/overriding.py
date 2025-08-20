'''Method Overriding (Child class changes Parent class method)

Definition: When a child class provides its own implementation of a method that 
already exists in its parent class.

Key idea: Child replaces parent’s version..
Decided at: Runtime (when object is created, child method is used).
.'''

class Parent:
    def work(self):
        print("Parent is working")

class Child(Parent):
    def work(self):  # Overriding
        print("Child is playing")

c = Child()
c.work()   # Child is playing
