# -*- coding:utf-8 -*-
# MIT OpenCourseWare
# Shapes

from string import *


class Shape(object):
    def area(self):
        raise AttributeException("Las subclases deberían 'override' este método.")


class Square(Shape):
    """
    Esta clase define las caracteristicas del cuadrado
    """

    def __init__(self, h):
        """
        h: longitud del lado del cuadrado
        """
        self.side = float(h)

    def area(self):
        """
        Regresa el area del cuadrado
        """
        return self.side ** 2

    def __str__(self):
        return 'Cuadrado con lado ' + str(self.side)

    def __eq__(self, other):
        """
        Dos cuadrados son iguales si ellos tienen la misma dimensión.
        other: objeto que revisa la igualdad
        """
        return type(other) == Square and self.side == other.side


class Circle(Shape):
    """
    Esta clase define las caracteristicas del círculo
    """

    def __init__(self, radius):
        """
        radius: radio del circulo
        """
        self.radius = float(radius)

    def area(self):
        """
        Regresa el area aproximada del circulo
        """
        return 3.14159 * (self.radius ** 2)

    def __str__(self):
        return 'Circulo con radio ' + str(self.radius)

    def __eq__(self, other):
        """
        Dos círculos son iguales si tienen el mismo radio.
        other: objeto que revisa la igualdad
        """
        return type(other) == Circle and self.radius == other.radius


#
# Problem 1: Create the Triangle class
#

class Triangle(Shape):
    """
    Esta clase define las características de un triángulo equilatero
    """

    def __init__(self, base, height):
        """
        base: longitud de la base del triángulo
        height: altura del triángulo
        """
        self.base = float(base)
        self.height = float(height)

    def area(self):
        """
        Regresa el area aproximada del triángulo equilatero
        """
        return (1 / 2) * (self.base * self.height)

    def __str__(self):
        return 'Triangulo con base ' + str(self.base) + ' y altura ' + str(self.height)

    def __eq__(self, other):
        """
        Dos círculos son iguales si tienen el mismo radio.
        other: objeto que revisa la igualdad
        """
        return type(other) == Triangle and self.base == other.base and self.height == self.height


#
# Problem 2: Create the ShapeSet class
#

class ShapeSet:
    """
    Esta clase contiene un set de figuras, ya sea triángulo, cuadrado o círculo
    """

    def __init__(self):
        """
        Inicializa cualquier variable que necesite
        """
        self.dataShapes = []
        self.index = 0

    def addShape(self, sh):
        """
        Agrega un shape sh al set, donde dos shapes no pueden ser identicos
        sh: shape to be added
        """

        if type(sh) == Square:
            if str(sh) in self.dataShapes:
                return print("\033[1;31mIN STOCK:\033[1;m", str(sh))
            else:
                self.dataShapes.append(str(sh))
                return print("\033[1;32mADDED:\033[1;m", str(sh))

        if type(sh) == Circle:
            if str(sh) in self.dataShapes:
                return print("\033[1;31mIN STOCK:\033[1;m", str(sh))
            else:
                self.dataShapes.append(str(sh))
                return print("\033[1;32mADDED:\033[1;m", str(sh))

        if type(sh) == Triangle:
            if str(sh) in self.dataShapes:
                return print("\033[1;31mIN STOCK:\033[1;m", str(sh))
            else:
                self.dataShapes.append(str(sh))
                return print("\033[1;32mADDED:\033[1;m", str(sh))

    def __iter__(self):
        """
        Esta función regresa un iterador que permite iterar sobre el set de shapes, un shape a la vez
        """
        return self

    def __next__(self):
        """
        Funcion necesaria para poder hacer la iteración
        """
        if self.index < len(self.dataShapes):
            self.index += 1
            return self.dataShapes[self.index - 1]
        else:
            raise StopIteration

    def __str__(self):
        """
        Regresa una representacion en string del set, que consiste en el string de cada shape, categorizado por tipo:
        primero circulos, luego cuadrados y después triángulos
        """

        return "\n".join(sorted(self.dataShapes))
