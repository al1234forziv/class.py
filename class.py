class Shape():
    def draw(self):
        return 'shape'

class Circle(Shape):
    def draw(self):
        return 'circle'

class Polygon(Shape):
    def draw(self):
        return 'polygon'

circle =  Circle()
polygon = Polygon()

print(circle.draw())
print(polygon.draw())

