# -*- coding:utf-8 -*-
# MIT OpenCourseWare
# Human Advisor with Dynamic Programming

import time

SUBJECT_FILENAME = "smallsub.txt"

#
# Problem 1: Building A Subject Dictionary
#

def loadSubjects(filename):
    """
    Esta función va a cargar una lista de asignaturas de un archivo. Cada linea del archivo contiene un string de la
    forma "name, value, work", donde 'name' es un string, 'value' es un entero indicando cuánto un estudiante aprenderá
    tomando la asignatura, y 'work' es un entero indicando el número de horas que un estudiante debería dedicarle para
    pasar la asignatura.

    loadSubject() regresa un diccionario mapeando el nombre de la asignatura a un tuple: (value, work) donde 'name' es un
    string y donde 'value' y 'work' son enteros.

    returns: {name:(value, work), ...}
    """

    # Lee cada una de las líneas del archivo especificado y las imprime
    inputFile = open(filename)

    subjects_dict = {}

    # Generando el diccionario
    for line in inputFile:
        tolist = line.strip('\n').split(',')
        key = tolist[0]
        value = (int(tolist[1]), int(tolist[2]))
        subjects_dict.update({key:value})

    return subjects_dict

#
# Problem 2: Subject Selection By Greedy Optimization
#

def greedyAdvisor(subjects, maxWork, comparator):
    """
    Esta función va a formular una lista de asignaturas que satisfaga las restricciones de cada estudiante, es decir,
    las horas que esta dispuesto a trabajar. El algoritmo debe escoger la primera mejor asignatura, donde la noción de
    mejor está definida por los comparadores.

    El comparador toma dos argumentos de tipo (value, work) y regresa un valor booleano verdadero indicando que cualquiera
    que sea el primer argumento, ese cumple la condición con respecto al segundo.

    Regresa un diccionario mapeando las asignaturas de la forma name:(value,work) donde incluye las asignaturas seleccionadas
    por el algoritmo, de tal manera que el total del trabajo de las asignaturas en el diccionario, no sea mayor a
    maxWork. Las asignaturas son seleccionadas usando el greedy algorithm. Las asignaturas en el diccionario no deben
    cambiar.

    subjects: dictionary mapping subject name:(value, work)
    maxWork: int >= 0
    comparator: function taking two tuples and returning a bool
    returns: dictionary mapping subject name:(value, work)
    """

    bestSubjects = {}
    totalWork = 0
    maxSubject = 0

    keys = list(subjects.keys())

    while True:
        for pair in keys:
            if maxSubject == 0:
                maxSubject = pair
            elif comparator(subjects[pair], subjects[maxSubject]):
                maxSubject = pair

        totalWork = totalWork + subjects[maxSubject][1]

        if totalWork <= maxWork:
            bestSubjects.update({maxSubject:subjects[maxSubject]})
            keys.remove(maxSubject)
            maxSubject = 0
        else:
            return bestSubjects











