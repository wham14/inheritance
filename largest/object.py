class Student:
    #constructor method
    def __init__(self,name,age,score):
        self.name=name
        self.age=age
        self.score=score


        #member function
    def display(self):
        print(f"Student name is : {self.name}, Age is : {self.age}, Score is : {self.score}")

        #instance of the class(object)
myobj=Student("James",22,"A")
myobj.display()
myobj2=Student("Ruth",52,"A-")
myobj2.display()
myobj3=Student("Peace",16,"B")
myobj3.display()
myobj4=Student("lisa",24,"B-")














