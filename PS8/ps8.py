# -*- coding:utf-8 -*-
# MIT OpenCourseWare
# Human Advisor with Dynamic Programming

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
            bestSubjects.update({maxSubject: subjects[maxSubject]})
            keys.remove(maxSubject)
            maxSubject = 0
        else:
            return bestSubjects

#
# Problem 3: Subject Selection By Brute Force
#

def bruteForceAdvisor(subjects, maxWork):
    """
    Regresa un diccionario mapeado las asignaturas de forma name: (value, work), donde representa la selección global
    optima de las asignaturas usando un algoritmo de fuerza bruta.

    subjects: dictionary mapping subject name to (value, work)
    maxWork: int >= 0
    returns: dictionary mapping subject name to (value, work)
    """
    nameList = list(subjects.keys())
    tupleList = list(subjects.values())
    bestSubset, bestSubsetValue = \
            bruteForceAdvisorHelper(tupleList, maxWork, 0, None, None, [], 0, 0)
    outputSubjects = {}
    for i in bestSubset:
        outputSubjects[nameList[i]] = tupleList[i]
    return outputSubjects

def bruteForceAdvisorHelper(subjects, maxWork, i, bestSubset, bestSubsetValue,
                            subset, subsetValue, subsetWork):
    # Hit the end of the list.
    if i >= len(subjects):
        if bestSubset == None or subsetValue > bestSubsetValue:
            # Found a new best.
            return subset[:], subsetValue
        else:
            # Keep the current best.
            return bestSubset, bestSubsetValue
    else:
        s = subjects[i]
        # Try including subjects[i] in the current working subset.
        if subsetWork + s[WORK] <= maxWork:
            subset.append(i)
            bestSubset, bestSubsetValue = bruteForceAdvisorHelper(subjects,
                    maxWork, i+1, bestSubset, bestSubsetValue, subset,
                    subsetValue + s[VALUE], subsetWork + s[WORK])
            subset.pop()
        bestSubset, bestSubsetValue = bruteForceAdvisorHelper(subjects,
                maxWork, i+1, bestSubset, bestSubsetValue, subset,
                subsetValue, subsetWork)
        return bestSubset, bestSubsetValue
