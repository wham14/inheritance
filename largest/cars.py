


class Car:
    def __init__(self, make, model,color, yom):
        self.make = make
        self.model = model
        self.color = color
        self.yom = yom

    def display(self):
        print(f"Dream car is {self.make}, and it`s {self.model}, and it`s {self.color}, and it`s {self.yom}")

my_object = Car("Ford", "Mustang", "Red", "1978")
my_object.display()
my_object = Car("Toyota", "TX", "Grey", "1987")
my_object.display()
my_object = Car("Mercede", "Actross", "Yellow", "1967")
my_object.display()
my_object = Car("Volkswagen", "Volkswagen", "Purple", "1968")
my_object.display()
my_object = Car("Dodge", "Hellcat", "White", "1976")
my_object.display()