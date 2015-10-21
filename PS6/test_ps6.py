# -*- coding:utf-8 -*-
# MIT OpenCourseWare
# Test for Wordgames

from ps6 import *
import time

#
# Test code
#

# ----------------------------------------- Test Get Words To Points -----------------------------------------

def testGetWordsToPoints(wordlist, pointsdict, total):
    """
    Unit test for getWordsToPoints
    """
    failure = False

    #
    # Este test es para probar que se genera un diccionario con los puntos formados de cada palabra en el wordlist.
    #

    # Test 1
    if pointsdict['abaka'] == 11:
        failure = True
    else:
        print("FAILURE (Test 1): testGetWordsToPoints()")
        print("\tSe esperaba un valor de 11 puntos para la palabra ABAKA, y se obtuvo", pointsdict['abaka'])

    # Test 2
    if pointsdict['kinetics'] == 14:
        failure = True
    else:
        print("FAILURE (Test 2): testGetWordsToPoints()")
        print("\tSe esperaba un valor de 14 puntos para la palabra KINETICS, y se obtuvo", pointsdict['kinetics'])

    # Test 3

    if pointsdict['wizzes'] == 27:
        failure = True
    else:
        print("FAILURE (Test 2): testGetWordsToPoints()")
        print("\tSe esperaba un valor de 27 puntos para la palabra WIZZES, y se obtuvo", pointsdict['wizzes'])

    if failure:
        print("SUCCESS: testGetWordsToPoints(). Tiempo de repuesta: {:.2f} segundos.".format(total))

# ----------------------------------------- Test Is Valid Word -----------------------------------------

def testIsValidWord(pointsdict):
    """
    Unit test for isValidWord
    """
    #
    # Este test es para probar el retorno de todas las posibles palabras generadas por una secuencia de letras.
    #

    failure = False
    hand = {'lboglaly'}

    # Test 1
    word = 'go'
    valid = isValidWord(word, hand, pointsdict)
    if valid:
        failure = True
    else:
        print("FAILURE (Test 1): testGetWordsToPoints()")
        print("\tSe esperaba un valor de verdadero, y se obtuvo", valid)

    # Test 2
    word = 'global'
    start = time.time()
    valid = isValidWord(word, hand, pointsdict)
    end = time.time()
    total = end - start
    if valid:
        failure = True
    else:
        print("FAILURE (Test 1): testGetWordsToPoints()")
        print("\tSe esperaba un valor de verdadero, y se obtuvo", valid)

    # Test 3
    word = 'globally'
    valid = isValidWord(word, hand, pointsdict)
    if valid:
        failure = True
    else:
        print("FAILURE (Test 1): testGetWordsToPoints()")
        print("\tSe esperaba un valor de verdadero, y se obtuvo", valid)


    if failure:
        print("SUCCESS: testIsValidWord(). Tiempo de repuesta: {:.2f} segundos.".format(total))


# ----------------------------------------- Running Test -----------------------------------------

wordlist = loadWords()

n = 7
start = time.time()
pointsdict = getWordsToPoints(wordlist, n)
end = time.time()
total = end - start

testGetWordsToPoints(wordlist, pointsdict, total)
testIsValidWord(pointsdict)