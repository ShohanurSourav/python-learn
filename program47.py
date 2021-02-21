# class and object with method

class Student:
    roll = ""
    gpa = ""

    def set_value(self, roll, gpa):
        self.roll = roll
        self.gpa = gpa

    def display(self):
        print(f" Roll : {self.roll}, GPA : {self.gpa}")


Sourav = Student()
Sourav.set_value(1965, 3.81)
Sourav.display()

Sumaiya = Student()
Sumaiya.set_value(1752, 3.71)
Sumaiya.display()
