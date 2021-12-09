class Rectangle():
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        self.sides
    def getArea(self):
        return(self.height * self.width)


class Circle():
    def __init__(self, radius=0):
        self.radius = radius
        self.sides = 0
    def getArea(self):
        return (self.radius * self.radius * 3.14)

shapes = [Rectangle(6, 10), Circle(7)]

print(str(shapes[0].sides))
print(str(shapes[0].getArea()))
