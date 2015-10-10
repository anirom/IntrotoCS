# -*- coding:utf-8 -*-
# MIT OpenCourseWare
# Test for Wordgames: Ghost

from ps5_ghost import *

#
# Test code
#

# ----------------------------------------- Test Load Words -----------------------------------------

def testLoadWords(wordlist):
    """
    Unit test for loadWords
    """
    #
    # Verificando que cargue correctamente la lista de palabras validas.
    #
    if type(wordlist) is list:
        print("Loading words...")
        print(" ", len(wordlist), "words loaded.")
    else:
        print("Failed Loading List")

# ----------------------------------------- Test Is Valid Word -----------------------------------------

def testIsValidWord(wordlist):
    """
    Unit test for isValidWord
    """
    #
    # Test para probar la busqueda de la palabra, ingresando letra por letra.
    #

    failure = False

    # Test 1
    finalword = []
    word = "killer"
    for letter in word:
        finalword.append(letter)
        fw = ''.join(finalword)
        valid = isValidWord(fw, wordlist)

    if valid:
        failure = True
    else:
        print("FAILURE (Test 1): testIsValidWord()")
        print("\tSe esperaba un valor True, y se obtuvo", valid)

    # Test 2
    finalword = []
    word = "seda"
    for letter in word:
        finalword.append(letter)
        fw = ''.join(finalword)
        valid = isValidWord(fw, wordlist)

    if not valid:
        failure = True
    else:
        print("FAILURE (Test 2): testIsValidWord()")
        print("\tSe esperaba un valor False, y se obtuvo", valid)

    if failure: print("SUCCESS: testIsValidWord()")

# ----------------------------------------- Test Counter Ghost -----------------------------------------

def testCounterGhost():
    """
    Unit test for counterGhost
    """
    #
    # Test para ir almacenando la palabra 'ghost' cuando un jugador pierde alguna partida
    #

    player = ''

    while player != 'ghost':
        player = counterGhost(player)

    if player == 'ghost' and type(player) == str:
        print("SUCCESS: testCounterGhost()")
    else:
        print("FAILURE: testCounterGhost()")
        print("\tSe esperaba el string 'ghost', y se obtuvo un", type(player),"con valor", player)

# ----------------------------------------- Test Play Hand -----------------------------------------

def testPlayHand(wordlist):
    """
    Unit test for playHand
    """
    #
    # Test para jugar una partida, es decir, completar una palabra
    #

    failure = False

    # Test 1
    # Test para la palabra KILL, en este caso debería perder el jugador 2
    lost, player = playHand(wordlist)
    if lost == True and player == 2:
        failure = True
    else:
        print("FAILURE (Test 1): testPlayHand()")
        print("\tSe esperaba que el jugador 2 haya perdido y se obtuvo que el jugador", player, "fue el que perdió")

    # Test 2
    # Test para la palabra PEAFA, en este caso debería perder el jugador 2
    lost, player = playHand(wordlist)
    if lost == True and player == 1:
        failure = True
    else:
        print("FAILURE (Test 2): testPlayHand()")
        print("\tSe esperaba que el jugador 1 haya perdido y se obtuvo que el jugador", player, "fue el que perdió")

    # Test 3
    # Test para la palabra PEAFOWL, en este caso debería perder el jugador 2
    lost, player = playHand(wordlist)
    if lost == True and player == 1:
        failure = True
    else:
        print("FAILURE (Test 3): testPlayHand()")
        print("\tSe esperaba que el jugador 1 haya perdido y se obtuvo que el jugador", player, "fue el que perdió")

    # Test 4
    # Test para la palabra PYTHON, en este caso debería perder el jugador 2
    lost, player = playHand(wordlist)
    if lost == True and player == 2:
        failure = True
    else:
        print("FAILURE (Test 4): testPlayHand()")
        print("\tSe esperaba que el jugador 2 haya perdido y se obtuvo que el jugador", player, "fue el que perdió")

    if failure: print("SUCCESS: testIsValidWord()")

# ----------------------------------------- Running Test -----------------------------------------

wordlist = loadWords()

testLoadWords(wordlist)
testIsValidWord(wordlist)
testCounterGhost()
testPlayHand(wordlist)
