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

# ----------------------------------------- Running Test -----------------------------------------

wordlist = loadWords()

testLoadWords(wordlist)
testIsValidWord(wordlist)
testCounterGhost()

