'''Duck typing means:
If an object behaves like a certain type (has the right methods/attributes), Python treats it as that type.

Why Duck Typing helps QA automation?

Flexibility → Same test works for multiple types of objects.

Reusability → Code doesn’t need to check class types.'''
#Imagine:

'''You want something that can send a message.

You don’t care whether it’s a phone, email, or whatsapp.

As long as it has a send() method, it works. '''

class Email:
    def send(self):
        print("sendig email msg")

class whatsapp:
    def send(self):
        print("sending whatsapp msg")


def notify(sender):
    sender.send()


e=Email()
w= whatsapp()

notify(e)
notify(w)
#The function notify(sender) just calls .send() — it does not check the class type.
