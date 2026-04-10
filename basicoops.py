# Base class (Parent)
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print("Name:", self.name)
        print("Age:", self.age)


# Derived class (Child)
class Student(Person):
    def __init__(self, name, age, student_id):
        # Call parent constructor
        super().__init__(name, age)
        self.student_id = student_id

    def display_student(self):
        self.display_info()
        print("Student ID:", self.student_id)


# Creating object
s1 = Student("Alice", 20, "S101")

# Calling methods
s1.display_student()