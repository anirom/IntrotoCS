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

# ----------------------------------------- Test Get Frequency -----------------------------------------

def testGetFrequencyDict():
    """
    Unit test for getFrequencyDict
    """
    #
    # Test para verificar que devuelve un diccionario con las letras y el numero de repeticiones de estas.
    #
    words = ["ghost", "skills", "trumpet"]
    failure = False

    # Test 1
    lovers = {'g': 1, 'h': 1, 'o': 1, 's': 1, 't': 1}
    frequency = getFrequencyDict(words[0])
    if lovers == frequency:
        failure = True
    else:
        print("FAILURE (Test 1): testgetFrequencyDict()")
        print("\tSe esperaba", lovers, "y se obtuvo", frequency)

    # Test 2

    hello = {'s': 2, 'k': 1, 'i': 1, 'l': 2}
    frequency = getFrequencyDict(words[1])
    if hello == frequency:
        failure = True
    else:
        print("FAILURE (Test 2): testgetFrequencyDict()")
        print("\tSe esperaba", lovers, "y se obtuvo", frequency)

    # Test 3

    luffing = {'t': 2, 'r': 1, 'u': 1, 'm': 1, 'p': 1, 'e': 1}
    frequency = getFrequencyDict(words[2])
    if luffing == frequency:
        failure = True
    else:
        print("FAILURE (Test 3): testgetFrequencyDict()")
        print("\tSe esperaba", lovers, "y se obtuvo", frequency)

    if failure: print("SUCCESS: testGetFrequencyDict()")

# ----------------------------------------- Test IS Valid Word -----------------------------------------

def testIsValidWord(wordlist):
    """
    Unit test for isValidWord
    """
    #
    # Test para probar la busqueda de la palabra, ingresando letra por letra.
    #

    finalword = []
    failure = False

    # Test 1
    word = "killer"
    for letter in word:
        finalword.append(letter)
        fw = ''.join(finalword)
        valid = isValidWord(fw, wordlist)

    if valid:
        failure = True
    else:
        print("FAILURE (Test 1): testgetIsValidWord()")
        print("\tSe esperaba un valor True, y se obtuvo", valid)

    # Test 2
    word = "jumbo"
    for letter in word:
        finalword.append(letter)
        fw = ''.join(finalword)
        valid = isValidWord(fw, wordlist)

    if not valid:
        failure = True
    else:
        print("FAILURE (Test 2): testgetIsValidWord()")
        print("\tSe esperaba un valor False, y se obtuvo", valid)

    if failure: print("SUCCESS: testIsValidWord()")

# ----------------------------------------- Running Test -----------------------------------------

wordlist = loadWords()

testLoadWords(wordlist)
testGetFrequencyDict()
testIsValidWord(wordlist)
