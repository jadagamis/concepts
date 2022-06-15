class Person:
    def __init__(self, first_name, last_name):
        self.firstname = first_name
        self.lastname = last_name

    def print_name(self):
        print(self.firstname, self.lastname)



class Student(Person):
    def __init__(self, first_name, last_name, *subject):
        super().__init__(first_name, last_name)
        self.subject = subject

    pass


x = Person("kotaro", "bubbl")
x.subject = "software design", "information systems"
x.print_name()
print(f"does {str(x.subject)}")

