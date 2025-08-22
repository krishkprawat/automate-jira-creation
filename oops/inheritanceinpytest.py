#example of inheritece in python


class Setup:
    def launch(self):
        print("launhed browser")

    def close(self):
        print("browesr closed")

class Testlogin (Setup):
    def login(self):
        print("logged in")

class Testcheckout(Setup):
    def checkout(self):
        print ("checput this jeanss")

login=Testlogin()
check=Testcheckout()
login.launch()
