# -*- coding:utf-8 -*-
# MIT OpenCourseWare
# Test for Human Advisor with Dynamic Programming

import time
from ps8 import *

#
# Test code
#

# ----------------------------------------- Test Load Subjects -----------------------------------------

def testLoadSubjects(subjects):
    printSubjects(subjects)

    if type(subjects) == dict:
        print("SUCCESS: testLoadSubjects()")
    else:
        print("FAILURE testLoadSubjects()")
        print("\tLa función no regresó un diccionario")

def printSubjects(subjects):
    """
    Imprime un string que contiene los campos name, value y work para cada asignatura en el diccionario y el trabajo
    total y el valor de todas las asignaturas
    """
    totalVal, totalWork = 0, 0
    if len(subjects) == 0:
        return 'Empty SubjectList'
    res = 'Course\tValue\tWork\n======\t====\t=====\n'
    subNames = list(subjects.keys())
    subNames.sort()
    for s in subNames:
        val = subjects[s][VALUE]
        work = subjects[s][WORK]
        res = res + s + '\t' + str(val) + '\t\t' + str(work) + '\n'
        totalVal += val
        totalWork += work
    res = res + '\nTotal Value: ' + str(totalVal) +'\n'
    res = res + 'Total Work:\t' + str(totalWork) + '\n'
    print(res)

# ----------------------------------------- Test Greedy Advisor -----------------------------------------

# Las funciones cmpValue, cmpWork y cmpRatio son los comparadores que ingresan en la función greedyAdvisor.

def cmpValue(subInfo1, subInfo2):
    """
    Regresa Verdadero si el valor del tuple (value, work) de subInfo1 es MAYOR que el valor del tuple (value, work)
    de subInfo2
    """
    val1 = subInfo1[VALUE]
    val2 = subInfo2[VALUE]
    return val1 > val2

def cmpWork(subInfo1, subInfo2):
    """
    Regresa verdadero si el trabajo del tuple (value, work) de subInfo1 es MENOR que el trabajo del tuple (value, work)
    de subInfo2
    """
    work1 = subInfo1[WORK]
    work2 = subInfo2[WORK]
    return work1 < work2

def cmpRatio(subInfo1, subInfo2):
    """
    Regresa verdadero si value/work del tuple (value, work) de subInfo1 es MAYOR que value/work del tuple (value, work)
    de subInfo2
    """
    val1 = subInfo1[VALUE]
    val2 = subInfo2[VALUE]
    work1 = subInfo1[WORK]
    work2 = subInfo2[WORK]
    return float(val1) / work1 > float(val2) / work2

def testGreedyAdvisor(subjects):

    failure = True
    maxWork = 15
    subjects = {'15.01': (9, 6), '6.00': (16, 8), '1.00': (7, 7), '6.01': (5, 3)}

    # Test 1

    result = greedyAdvisor(subjects, maxWork, cmpValue)

    if result == {'15.01': (9, 6), '6.00': (16, 8)}:
        failure = False
    else:
        print("Test 1: FAILURE testGreedyAdvisor()")
        print("\tSe esperaba un diccionario con {'15.01': (9, 6), '6.00': (16, 8)} y se devolvió un diccionario:", result)

    # Test 2

    result = greedyAdvisor(subjects, maxWork, cmpWork)
    if result == {'6.01': (5, 3), '15.01': (9, 6)}:
        failure = False
    else:
        print("Test 2: FAILURE testGreedyAdvisor()")
        print("\tSe esperaba un diccionario con {'6.01': (5, 3), '15.01': (9, 6)} y se devolvió un diccionario:", result)

    # Test 3

    result = greedyAdvisor(subjects, maxWork, cmpRatio)
    if result == {'6.00': (16, 8), '6.01': (5, 3)}:
        failure = False
    else:
        print("Test 3: FAILURE testGreedyAdvisor()")
        print("\tSe esperaba un diccionario con {'6.00': (16, 8), '6.01': (5, 3)} y se devolvió un diccionario:", result)

    if not failure:
         print("SUCCESS: testGreedyAdvisor()")

# ----------------------------------------- Test Brute Force -----------------------------------------

def testBruteForceTime(subjects):
    """ Esta función corre un test para la función bruteForceAdvisor y mide el tiempo para recobir una respuesta para
    distintas horas de trabajo """

    for i in range(1, 10):
        start_time = time.time()
        bruteForceAdvisor(subjects, i)
        end_time = time.time()
        counter = end_time - start_time
        if counter > 3:
            print('TIMEOUT: testBruteForceTime()')
            break

    # Observations
        # El tiempo razonable de computo se limitó a 3 segundos, nos regresa para hasta 7 horas de trabajo. Hace una
        # búsqueda muy lenta y ya para un computo de 15 horas como en la función greedyAdvisor su tiempo es exagerado.

# ----------------------------------------- Test Dinnamyc Programming Advisor -----------------------------------------

def testDPAdvisor(subjects):

    maxWork = 15
    # subjects = {'15.01': (9, 6), '6.00': (16, 8), '1.00': (7, 7), '6.01': (5, 3)}

    print("\n<--- Dynamic Programming with Tree Method ---> \n")
    printSubjects(dpAdvisorTree(subjects, maxWork))
    print("<--- Dynamic Programming with Table Method ---> \n")
    printSubjects(dpAdvisorTable(subjects, maxWork))

# ----------------------------------------- Test Dinnamyc Programming -----------------------------------------

def testDp(subjects):

    maxWork = 7

    # Time Brute Force
    start_time = time.time()
    bruteForceAdvisor(subjects, maxWork)
    end_time = time.time()
    counterBruteForce = end_time - start_time
    print("Tiempo de respuesta:", counterBruteForce)

    # Time DP Tree

    start_time = time.time()
    dpAdvisorTree(subjects, maxWork)
    end_time = time.time()
    counterDPTree = end_time - start_time
    print("Tiempo de respuesta:", counterDPTree)

    # Time DP Table

    start_time = time.time()
    dpAdvisorTable(subjects, maxWork)
    end_time = time.time()
    counterDPTable = end_time - start_time
    print("Tiempo de respuesta:", counterDPTable)

    if counterBruteForce > counterDPTree and counterBruteForce > counterDPTree :
        print("SUCCESS: Las funciones dinámicas son más rápidas que la función de fuerza bruta.")
    else:
        print("FAILURE: Resultó más rápida la fuerza bruta.")

    # Observations
        # La memorización, además de hacer más estructurada la busqueda simplifica los cálculos, haciendo más
        # veloz la respuesta.
# ----------------------------------------- Running Test -----------------------------------------

SUBJECT_FILENAME = "subjects.txt"
VALUE, WORK = 0, 1

subjects = loadSubjects(SUBJECT_FILENAME)

testLoadSubjects(subjects)
testGreedyAdvisor(subjects)
testBruteForceTime(subjects)
testDPAdvisor(subjects)
testDp(subjects)