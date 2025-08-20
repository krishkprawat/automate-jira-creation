#inheritance is a oops feature where once class inherit the properties of parent class.
''' single level   -- parent a - child b
multilevel - one grand parent - parent - child
multiple  -- one child - mutilple parent
and hybrid -- one parent - multiple child'''

#single

class Animal :
    def sound(self):
        print("animal can make sounds")

class Dog(Animal):
    def bark(self):
        print("bhaw bhaw bhaw")

d= Dog()
d.sound()
d.bark()


#multiple

class Engine:
    def start(self):
        print ("engine starts")

class Playmusic:
    def music(self):
        print('music plays')

class Drive(Engine,Playmusic):
    def drive(self):
        print ("driving the car")


c= Drive()
c.start()
c.music()
c.drive()


#multilevel 

class Employee:
    def employee(self):
        print ("i am employee")

class Engineer(Employee):
    def engineer(self):
        print('i am in enginnering team')

class QAEngineer(Engineer):
    def QAengineer(self):
        print('i am in QA')

qa = QAEngineer()
qa.employee()
qa.engineer()
qa.QAengineer()


#hierarchial 

class Person:
    def info(self):
        print("i am a person")

class busineesmen(Person):
    def work (self):
        print("i am businessman hahah")

class govt (Person):
    def policy(self):
        print("i m govt employee i have lot of work")


b= busineesmen()
b.info()
b.work()

g= govt()
g.info()
g.policy()