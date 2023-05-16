class Student:
    def __init__(self, name, contact):
        self.name = name
        self.contact = contact

    def get_data(self):
        print("Accepting data")
        self.name = input("Enter Name: ")
        self.contact = input("Enter Contact: ")

    def put_data(self):
        print("The name is " + self.name + "This is the contact " + self.contact)


class ScienceStudent(Student):
    def __init__(self, age):
        self.age = age

    def science(self):
        print("I am a Science Student")


Rob = ScienceStudent(20)
Rob.science()
Rob.get_data()
Rob.put_data()