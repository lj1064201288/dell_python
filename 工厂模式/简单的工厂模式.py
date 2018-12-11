class Shape():
    def draw(self):
        pass

    def remove(self):
        pass

class Circle(Shape):

    def draw(self):
        print("Circle is created")

    def remove(self):
        print("Circle is removed")

class Rectangle(Shape):

    def draw(self):
        print("Rectangle is created")

    def remove(self):
        print("Rectangle is removed")

class Triangle(Shape):

    def draw(self):
        print("Triangle is created")

    def remove(self):
        print("Triangle is removed")

class Factory():

    def __init__(self):
        self.graph = input("Please input a graph a want:")

    def get_factory(self):
        if self.graph == "Cirle":
            return Circle()

        if self.graph == "Rectangle":
            return Rectangle()

        if self.graph == "Triangle":
            return  Triangle()

        else:
            return TypeError

if __name__ == '__main__':

    graph = Factory().get_factory()
    graph.draw()
    graph.remove()