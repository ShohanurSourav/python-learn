# constructor

class Student:
    roll = ""
    gpa = ""

    def __init__(self, roll, gpa):
        self.roll = roll
        self.gpa = gpa

    def display(self):
        print(f" Roll : {self.roll}, GPA : {self.gpa}")


Sourav = Student(1965, 3.81)
Sourav.display()

Sumaiya = Student(1752, 3.71)
Sumaiya.display()
