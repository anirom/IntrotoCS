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

#
# Problem 4: Subject Selection By Dynamic Programming
#

def dpAdvisorTree(subjects, maxWork):
    """
    Regresa un diccionario, mapeando las asignaturas de forma name: (value, work) que contiene un set de asignaturas
    que tiene el máximo valor sin exceder el valor de maxWork.

    subjects: dictionary mapping subject name to (value, work)
    maxWork: int >= 0
    returns: dictionary mapping subject name to (value, work)
    """
    memo = {}

    keys = list(subjects.keys())
    valueList = []
    workList = []
    result = {}

    for each in subjects:
        valueList.append(subjects[each][VALUE])
        workList.append(subjects[each][WORK])

    value, answerList = dpTreeAdvisor(workList, valueList, len(workList) - 1, maxWork, memo)

    for i in answerList:
        result.update({keys[i]: subjects[keys[i]]})

    return result

def dpAdvisorTable(subjects, maxWork):
    """
    Regresa un diccionario, mapeando las asignaturas de forma name: (value, work) que contiene un set de asignaturas
    que tiene el máximo valor sin exceder el valor de maxWork.

    subjects: dictionary mapping subject name to (value, work)
    maxWork: int >= 0
    returns: dictionary mapping subject name to (value, work)
    """

    tupSubjects = []
    result = {}

    for each in subjects:
        name = each
        work = subjects[each][WORK]
        value = subjects[each][VALUE]
        tempSubject = (name, value, work)
        tupSubjects.append(tempSubject)

    answerList = dpTableAdvisor(tupSubjects, maxWork)
    for item in answerList:
        result.update({item[0]: (item[1], item[2])})

    return result

def dpTreeAdvisor(work, value, index, maxWork, memo):
    """"
    CodeHelp from MIT
    """
    # Ejemplificando el diccionario  {'15.01': (9, 6), '6.00': (16, 8), '1.00': (7, 7), '6.01': (5, 3)}, con un trabajo
    # máximo de 15 horas. La función dinámica toma un tuple que contiene el indice de donde se posiciona, el trabajo
    # restante y el valor generado.

    #                                                   (index, work, value)
    #                                                    3,      15,      0
    #                                              /                            \
    #                                        2,  15,  0                      2,  8,  7
    #                                       /           \                   /          \
    #                            1,  15,  0               1,  12,  5        1,  8,  7   1,  4, 12
    #                          /           \             /           \      /       \
    #                   0,15,0         0,7,16       0,12,5        0,4,21   0,8,7     0,0,23
    #                      /  \           / \           / \           / \     / \
    #               -,15,0  -,9,9   -,7,16 -,2,25  -,12,5 -,3,11  0,4,21 - -8,7  -,1,13
    #
    # El mejor caso sería -,2,25, donde se toman las asignaturas 15.01 y 6.00.

    try:
        return memo[(index, maxWork)]
    except KeyError:
        if index == 0:
            if work[index] < maxWork:
                memo[(index, maxWork)] = value[index], [index]
                return value[index], [index]
            else:
                memo[(index, maxWork)] = 0, []
                return 0, []
    withoutIndex, courseList = dpTreeAdvisor(work, value, index - 1, maxWork, memo)
    if work[index] > maxWork:
        memo[(index, maxWork)] = withoutIndex, courseList
        return withoutIndex, courseList
    else:
        withIndex, courseListTemp = dpTreeAdvisor(work, value, index - 1, maxWork - work[index], memo)
        withIndex += value[index]
    if withIndex > withoutIndex:
        indexValue = withIndex
        courseList = [index] + courseListTemp
    else:
        indexValue = withoutIndex

    memo[(index, maxWork)] = indexValue, courseList
    return indexValue, courseList


def dpTableAdvisor(tupSubjects, maxWork):
    """"
    CodeHelp from rosettacode.org [http://rosettacode.org/wiki/Knapsack_problem/0-1#Dynamic_programming_solution]
    """

    # Ejemplificando el diccionario  {'15.01': (9, 6), '6.00': (16, 8), '1.00': (7, 7), '6.01': (5, 3)}, con un trabajo
    # máximo de 15 horas. La función dinámica toma un tuple que contiene el indice de donde se posiciona, el trabajo
    # restante y el valor generado.

    #         0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15
    # (9,6)   0 | 0 | 0 | 0 | 0 | 0 | 9 | 9 | 9 | 9 | 9  | 9  | 9  | 9  | 9  | 9
    # (16,8)  0 | 0 | 0 | 0 | 0 | 0 | 9 | 9 |16 |16 | 16 | 16 | 16 | 16 | 25 | 25
    # (7,7)   0 | 0 | 0 | 0 | 0 | 0 | 9 | 9 |16 |16 | 16 | 16 | 16 | 16 | 25 | 25
    # (5,3)   0 | 0 | 0 | 5 | 5 | 5 | 9 | 9 |16 |16 | 16 | 21 | 21 | 21 | 25 | 25
    #
    # El mejor caso sería (16,8), (9,6) con un valor de 25 donde se toman las asignaturas 15.01 y 6.00.

    table = [[0 for w in range(maxWork + 1)] for j in range(len(tupSubjects) + 1)]

    for j in range(1, len(tupSubjects) + 1):
        name, value, work = tupSubjects[j-1]
        for w in range(1, maxWork + 1):
            if work > w:
                table[j][w] = table[j-1][w]
            else:
                table[j][w] = max(table[j-1][w], table[j-1][w-work] + value)

    result = []
    w = maxWork
    for j in range(len(tupSubjects), 0, -1):
        wasAdded = table[j][w] != table[j-1][w]

        if wasAdded:
            name, value, work = tupSubjects[j-1]
            result.append(tupSubjects[j-1])
            w -= work

    return result