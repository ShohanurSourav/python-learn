# magic method

class Bike:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    # magic method to check the obj value r same or not
    def __eq__(self, other):
        return self.name == other.name and self.color == other.color

    def __str__(self):
        return (f"Name = {self.name}, Color = {self.color}")

    def display(self):
        print(f"Name = {self.name}, Color = {self.color}")


bike1 = Bike("Yamaha R15", "Blue")
bike2 = Bike("Yamaha FZ", "Orange")
print(str(bike1))
print(str(bike2))
print(bike1 == bike2)
