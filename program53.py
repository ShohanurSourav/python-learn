# multilevel inheritance
class A:
    def display1(self):
        print("I am inside A class")


class B(A):
    def display2(self):
        # display1()
        print("I am inside B class")


class C(B):
    def display3(self):
        # display1()
        # display2()
        super().display1()
        super().display2()
        print("I am inside C class")


ob1 = C()
ob1.display3()


# multiple inheritance


class A:
    def display(self):
        print("I am inside A class")


class B:
    def display(self):
        # display()
        print("I am inside B class")


class C(A, B):
    # A -> display()
    # B -> display()
    def display(self):
        print("I am inside C class")


ob1 = C()
ob1.display()
