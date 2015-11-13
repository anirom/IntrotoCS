# -*- coding:utf-8 -*-
# MIT OpenCourseWare
# Test for Human Advisor with Dynamic Programming

from ps8 import *

#
# Test code
#

# ----------------------------------------- Test Load Subjects -----------------------------------------

def testLoadSubjects(filename):
    subjects = loadSubjects(filename)
    printSubjects(subjects)

    if type(subjects) == dict:
        print("SUCCESS: testLoadSubjects()")
    else:
        print("FAILURE testLoadSubjects()")
        print("\tLa función no regresó un diccionario")

def printSubjects(subjects):
    """
    Imprime un string que contiene los campos name, value y work para cada asignatura en el diccionario y el total del
    trabajo y valor de todas las asignaturas
    """
    totalVal, totalWork = 0,0
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

# ----------------------------------------- Running Test -----------------------------------------

SUBJECT_FILENAME = "subjects.txt"
VALUE, WORK = 0, 1

testLoadSubjects(SUBJECT_FILENAME)
