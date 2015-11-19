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
        return self.side**2

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
        return 3.14159*(self.radius**2)

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
        return (1/2)*(self.base*self.height)

    def __str__(self):
        return 'Triangulo con base ' + str(self.base) + ' y altura ' + str(self.height)

    def __eq__(self, other):
        """
        Dos círculos son iguales si tienen el mismo radio.
        other: objeto que revisa la igualdad
        """
        return type(other) == Triangle and self.base == other.base and self.height == self.height