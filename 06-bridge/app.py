"""
Exemplo do padrão Bridge.
fonte: adaptado de https://en.wikipedia.org/wiki/Bridge_pattern
"""
from abc import ABC, abstractmethod


NOT_IMPLEMENTED = "You should implement this."


# Interface define métodos que todas as APIs devem implementar
class DrawingAPI(ABC):
    @abstractmethod
    def draw_circle(self, x, y, radius):
        raise NotImplementedError(NOT_IMPLEMENTED)


class DrawingAPI1(DrawingAPI):
    def draw_circle(self, x, y, radius):
        return "API1.circle at {0}:{1} - radius: {2}".format(x, y, radius)


class DrawingAPI2(DrawingAPI):
    def draw_circle(self, x, y, radius):
        return "API2.circle at {0}:{1} - radius: {2}".format(x, y, radius)

class DrawingAPI3(DrawingAPI):
    def draw_circle(self, x, y, radius):
        return "API3.circle at {0}:{1} - radius: {2}".format(x, y, radius)

# Enviamos a interface Drawing API como ref no construtor
# Nossa bridge se configura na composição com drawing_api
class Shape(ABC):
    def __init__(self, api: DrawingAPI):
        self.drawing_api = api

    @abstractmethod
    def draw(self):
        raise NotImplementedError(NOT_IMPLEMENTED)

    @abstractmethod
    def resize_by_percentage(self, percent):
        raise NotImplementedError(NOT_IMPLEMENTED)


# Circle poderá ser combinado com qualquer Drawing API
class CircleShape(Shape):
    def __init__(self, x, y, radius, drawing_api):
        self.x = x
        self.y = y
        self.radius = radius
        super(CircleShape, self).__init__(drawing_api)


    def draw(self):
        return self.drawing_api.draw_circle(self.x, self.y, self.radius)

    def resize_by_percentage(self, percent):
        self.radius *= 1 + percent / 100


class Cliente(object):
    @staticmethod
    def test():
        # Criamos três combinações diferentes sem precisar criar uma classe especializada pra cada
        shapes = [
            CircleShape(1.0, 2.0, 3.0, DrawingAPI1()),
            CircleShape(5.0, 7.0, 11.0, DrawingAPI2()),
            CircleShape(5.0, 4.0, 12.0, DrawingAPI3()),
        ]

        # polimorfismo pela classe abstrata Shape
        for shape in shapes:
            shape.resize_by_percentage(2.5)
            print(shape.draw())


Cliente.test()
