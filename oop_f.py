# object-oriented programming language
# classifying a set of things that  can be represented
# defining a property of a class that can be represented
# example student classes can be represented example name , age , class, contact, address, etc
class Student:
    def __init__(self, name, contact):
        self.name = name
        self.contact = contact

    def get_data(self):
        print("Accepting data")
        self.name = input("Enter Name: ")
        self.contact = input("Enter Contact: ")

    def put_data(self):
        print("The name is "+self.name + "This is the contact " + self.contact)


john = Student("laksh", 0)
john.get_data()
john.put_data()
