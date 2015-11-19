# -*- coding:utf-8 -*-
# MIT OpenCourseWare
# Shapes

from ps9 import *

#
# Test code
#

# ----------------------------------------- Test Shapes -----------------------------------------
def testShapes():

    print("\n ---------- Cuadrados ----------")
    # Cuadrado 1
    print("\n\tCuadrado 1")
    cuadrado1 = Square(4)
    print(cuadrado1)
    print("Area del cuadrado ", cuadrado1.area())

    # Cuadrado 2
    print("\n\tCuadrado 2")
    cuadrado2 = Square(2)
    print(cuadrado2)
    print("Area del cuadrado ", cuadrado2.area())

    print("\nIgualdad entre los cuadrados es", cuadrado1 == cuadrado2)

    print("\n ---------- Circulos ----------")
    # Círculo 1
    print("\n\tCirculo 1")
    circulo1 = Circle(4)
    print(circulo1)
    print("Area del circulo ", circulo1.area())

    # Círculo 2
    print("\n\tCirculo 2")
    circulo2 = Circle(4)
    print(circulo2)
    print("Area del circulo ", circulo2.area())

    print("\nIgualdad entre los circulos es", circulo1 == circulo2)

    print("\n ---------- Triangulos ----------")
    # Triangulo 1
    print("\n\tTriangulo 1")
    triangulo1 = Triangle(4,8)
    print(triangulo1)
    print("Area del triangulo ", triangulo1.area())

    # Triangulo 2
    print("\n\tTriangulo 2")
    triangulo2 = Triangle(2, 8)
    print(triangulo2)
    print("Area del triangulo ", triangulo2.area())

    print("\nIgualdad entre los triangulos es", triangulo1 == triangulo2)

# ----------------------------------------- Test ShapeSet -----------------------------------------

def testShapeSet():
    print("\n ---------- Set Shapes ----------")
    # Creación de las figuras

    triangulo2 = Triangle(2, 8)
    triangulo3 = Triangle(6, 7)
    cuadrado1 = Square(4)
    cuadrado2 = Square(8)
    circulo1 = Circle(7)
    triangulo1 = Triangle(2, 8)


    # Creación del set
    shapeSet = ShapeSet()
    shapeSet.addShape(triangulo2)
    shapeSet.addShape(triangulo3)
    shapeSet.addShape(cuadrado1)
    shapeSet.addShape(cuadrado2)
    shapeSet.addShape(circulo1)
    shapeSet.addShape(triangulo1)

    # Itera sobre las figuras que hay
    print("\n --- iterator --- ")
    for item in shapeSet:
        print(item)

    # Imprime las figuras existentes
    print("\n --- print --- ")
    print(shapeSet)

# ----------------------------------------- Running Test -----------------------------------------

testShapes()
testShapeSet()