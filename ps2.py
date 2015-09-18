#!/usr/bin/env python
# -*- coding: utf-8 -*-
# MIT OpenCourseWare EE&CS
# McNugget Problem

# La ecuación que representa este problema es 6a + 9b + 20c = n, donde a,b,c y n > 0
# El teorema que explica el porqué es continuo para estos valores dice que a partir de una secuencia larga de numeros
# continuos, entonces se puede contar cualquier numero posterior como la adición de la unidad.

a = 0
b = 0
c = 0
n = 0

for i in range(50,66):
    print("Las combinaciones para a,b y c de {} ".format(i) + "nuggets, son: ")
    #Toma todos los valores posibles y hace las combinaciones verificando que sea igual al valor deseado
    for a in range (0,5):
        n = 6*a + 9*b + 20*c
        if n == i:
            print(a,b,c)
        for b in range (0,5):
            n = 6*a + 9*b + 20*c
            if n == i:
                print(a,b,c)
            for c in range(0,5):
                n = 6*a + 9*b + 20*c
                if n == i:
                    print(a,b,c)





