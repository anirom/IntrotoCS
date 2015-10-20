# -*- coding:utf-8 -*-
# MIT OpenCourseWare
# Test for Wordgames

from ps6 import *
import time

#
# Test code
#

# ----------------------------------------- Test Pick Best Word -----------------------------------------

def testPickBestWord():
    """
    Unit test for pickBestWord
    """
    #
    # Este test probará que para distinto juego de letras, regresará la palabra con el score más alto.
    #

# ----------------------------------------- Test Get Words To Points -----------------------------------------

def testGetWordsToPoints(wordlist):
    """
    Unit test for getWordsToPoints
    """
    failure = False

    #
    # Este test es para probar que se genera un diccionario con los puntos formados de cada palabra en el wordlist.
    #

    n = 7
    start = time.time()
    pointsdict = getWordsToPoints(wordlist, n)
    end = time.time()

    total = end - start

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

# ----------------------------------------- Running Test -----------------------------------------

wordlist = loadWords()

testGetWordsToPoints(wordlist)