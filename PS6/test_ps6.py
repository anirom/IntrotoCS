# -*- coding:utf-8 -*-
# MIT OpenCourseWare
# Test for Wordgames

from ps6 import *
import time

#
# Test code
#

# ----------------------------------------- Test Get Words To Points -----------------------------------------

def testGetWordsToPoints(pointsdict, total):
    """
    Unit test for getWordsToPoints
    """
    #
    # Este test es para probar que se genera un diccionario con los puntos formados de cada palabra en el wordlist.
    #

    failure = False

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
        print("FAILURE (Test 3): testGetWordsToPoints()")
        print("\tSe esperaba un valor de 27 puntos para la palabra WIZZES, y se obtuvo", pointsdict['wizzes'])

    if failure:
        print("SUCCESS: testGetWordsToPoints(). Tiempo de repuesta: {:.2f} segundos.".format(total))

# ----------------------------------------- Test Is Valid Word -----------------------------------------
def testIsValidWord(pointsdict):
    """
    Unit test for pickBestWord
    """
    #
    # Este test probará que sea una palabra valida y que la palabra tenga las letras de la partida
    #

    failure = False
    hand = {'s': 1, 'c': 2, 'h': 1, 'o': 2, 'a': 1, 'd':1, 'l':1}

    # Test 1
    word = "power"
    valid = isValidWord(word, hand, pointsdict)
    if not valid:
        failure = True
    else:
        print("FAILURE (Test 1): testIsValidWord()")
        print("\tSe esperaba un valor false y se obtuvo un valor", valid)

    # Test 2
    word = "school"
    valid = isValidWord(word, hand, pointsdict)
    if valid:
        failure = True
    else:
        print("FAILURE (Test 2): testIsValidWord()")
        print("\tSe esperaba un valor true y se obtuvo un valor", valid)

    # Test 3
    word = "dals"
    valid = isValidWord(word, hand, pointsdict)
    if valid:
        failure = True
    else:
        print("FAILURE (Test 3): testIsValidWord()")
        print("\tSe esperaba un valor true y se obtuvo un valor", valid)

    if failure:
        print("SUCCESS: testIsValidWord()")

# ----------------------------------------- Test Pick Best Word -----------------------------------------

def testPickBestWord(pointsdict):
    """
    Unit test for pickBestWord
    """
    #
    # Este test probará que para distinto juego de letras, regresará la palabra con el score más alto.
    #

    # Test 1
    hand = {'g': 1, 'o': 2, 'l': 3, 'b': 1, 'a': 1, 'y':1}
    pointsdict = {'boogy': 11, 'globally': 14, 'global': 9, 'log': 3}
    bestword, bestvalue = pickBestWord(hand, pointsdict)

    if bestword == 'globally' and bestvalue == 14:
        failure = True
    else:
        print("FAILURE (Test 1): testPickBestWord()")
        print("\tSe esperaba la palabra 'globally' con un valor de 14 puntos, y se obtuvo", bestword, "con un valor de", bestvalue,"puntos.")

    # Test 2
    hand = {'e': 3, 'f': 2, 'z': 1, 'd': 1, 's': 1}
    pointsdict = {'fees': 7, 'zee': 12, 'fez': 15, 'feezes': 18, 'feezed': 19}
    bestword, bestvalue = pickBestWord(hand, pointsdict)
    if bestword == 'feezed' and bestvalue == 19:
        failure = True
    else:
        print("FAILURE (Test 2): testPickBestWord()")
        print("\tSe esperaba la palabra 'feezed' con un valor de 19 puntos, y se obtuvo", bestword, "con un valor de", bestvalue,"puntos.")

    # Test 3
    hand = {'z': 2, 'y': 1}
    bestword = pickBestWord(hand, pointsdict)
    if bestword == '.':
        failure = True
    else:
        print("FAILURE (Test 3): testGetWordsToPoints()")
        print("\tNo se espera ninguna palabra y se obtuvo", bestword)

    if failure:
        print("SUCCESS: testGetWordsToPoints()")

# ----------------------------------------- Running Test -----------------------------------------

wordlist = loadWords()
n = 7
start = time.time()
pointsdict = getWordsToPoints(wordlist, n)
end = time.time()
total = end - start

testGetWordsToPoints(pointsdict, total)
testIsValidWord(pointsdict)
testPickBestWord(pointsdict)