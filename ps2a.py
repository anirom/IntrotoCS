#!/usr/bin/env python
# -*- coding: utf-8 -*-
# MIT OpenCourseWare EE&CS
# McNugget Problem

# Este programa encuentra el mayor numero de nuggets que NO se pueden comprar en cantidad exacta.
# Sabemos que a partir de 50 hay una secuencia continua, y que además el paquete mínimo es de 6.
# Así que el numero mayor debe estar en el rango de 6 a 49.

a = 0
b = 0
c = 0
n = 0
numeromayor = 0
valido = True

for i in range(6, 50):
    for a in range(0, 5):
        # Si ya se ha cumplido la condición, se va rompiendo el ciclo para mantener en True su validez 
        if n == i:
            break
        else:
            n = 6 * a + 9 * b + 20 * c
            if n == i:
                # print('same')
                valido = True
                break
            else:
                valido = False
        for b in range(0, 5):
            if n == i:
                break
            else:
                n = 6 * a + 9 * b + 20 * c
                if n == i:
                    # print('same')
                    valido = True
                    break
                else:
                    valido = False
                for c in range(0, 5):
                    n = 6 * a + 9 * b + 20 * c
                    if n == i:
                        # print('same')
                        valido = True
                        break
                    else:
                        valido = False

    if valido == False:
        # print(i)
        numeromayor = i

print("El numero más grande de nuggets que no se pueden comprar es: {}".format(numeromayor))