# -*- coding:utf-8 -*-
# MIT OpenCourseWare
# Human Advisor with Dynamic Programming

import time

SUBJECT_FILENAME = "subjects.txt"
VALUE, WORK = 0, 1

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