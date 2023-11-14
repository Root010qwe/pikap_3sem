from bub_oo.figure import Figure
from bub_oo.color import Color
import math
class Circle(Figure):
    type = "Круг"
    def __init__(self, radius, color):
        self.radius = radius
        self.c_color = Color(color)
    def area(self):
       return math.pi * (self.radius ** 2)

    def __repr__(self):
        return '{} {} цвета радиусом {} площадью {}.'.format(
            self.type,
            self.c_color._color,
            self.radius,
            self.area()
        )