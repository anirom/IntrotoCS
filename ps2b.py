#!/usr/bin/env python
# -*- coding: utf-8 -*-
# MIT OpenCourseWare EE&CS
# McNugget Problem

# Este programa determina para distintos paquetes, el numero maximo, menor a 200, que no se puede pedir

packages = (6,9,20)
# packages = (7, 15, 21)
# packages = (12,24,36)
# packages = (1,3,10) # Este permite todas las combinaciones posibles


a = 0
b = 0
c = 0
n = 0
numeromayor = 0
valido = True

for i in range(1, 150):
    for a in range(0, 5):
        # Si ya se ha cumplido la condición, se va rompiendo el ciclo para mantener en True su validez
        if n == i:
            break
        else:
            n = (packages[0] * a) + (packages[1] * b) + (packages[2] * c)
            if n == i:
                #print('same')
                valido = True
                break
            else:
                valido = False
        for b in range(0, 5):
            if n == i:
                break
            else:
                n = (packages[0] * a) + (packages[1] * b) + (packages[2] * c)
                if n == i:
                    #print('same')
                    valido = True
                    break
                else:
                    valido = False
                for c in range(0, 5):
                    n = (packages[0] * a) + (packages[1] * b) + (packages[2] * c)
                    if n == i:
                        #print('same')
                        valido = True
                        break
                    else:
                        valido = False

    if valido == False:
        #print(i)
        numeromayor = i

print("Dados los paquetes <{:d}>, <{:d}>, <{:d}>".format(*packages) + " el número más grande de McNuggets que no "
      "puede ser comprado en cantidad exacta es: {}".format(numeromayor))