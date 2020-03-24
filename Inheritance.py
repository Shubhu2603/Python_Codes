#Implementation of Inheritance using Python
class Fruit:
    def __init__(self,color,flavour):
        self.color=color
        self.flavour=flavour
    def display(self):
        print(self.color,self.flavour)

class Apple(Fruit):
    pass

class Grape(Fruit):
    pass

A=Apple("red","sweet")
G=Grape("green","sour")
A.display()
G.display()