# -*- coding:utf-8 -*-
# MIT OpenCourseWare
# Word Game

from ps10 import *

#
# Test code
#

# ----------------------------------------- Test LoadWords -----------------------------------------

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

# ----------------------------------------- Test Hand -----------------------------------------
def testHand():
    """
    Unit test for testHand Class
    """

    failure = False
    print("\n ---------- Test Hand ---------")

    h = Hand(8, {'a':3, 'b':2, 'd':3})

    print("Mano actual:", h)
    h.update('bad')
    print("Palabra dada: bad")
    print("Mano actual:", h)

    if h.containsLetters('aabdd') and not h.isEmpty():
        failure = True
    else:
        failure = False
        print("FAILURE: Debería estar la letras 'aabdd' y además no estar vacío")

    h.update('dad')
    print("Palabra dada: dad")
    print("Mano actual:", h)
    if h.containsLetters('ab') and not h.isEmpty():
        failure = True
    else:
        failure = False
        print("FAILURE: Debería estar la letras 'aabdd' y además no estar vacío")

    h.update('ab')
    print("Palabra dada: ab")
    print("Mano actual:", h)

    if h.isEmpty():
        failure = True
    else:
        failure = False
        print("FAILURE: Debería estar vacío")

    print("Comparación de jugadas: ")
    print("h = Hand(8, {'a':3, 'b':2, 'd':3})")
    h = Hand(8, {'a':3, 'b':2, 'd':3})
    print("g = Hand(8, {'a':3, 'b':2, 'd':3})")
    g = Hand(8, {'a':3, 'b':2, 'd':3})
    print("j = Hand(8, {'a':3, 'b':2, 'd':3})")
    j = Hand(7, {'a':2, 't':2, 'p':3})
    print("¿h = g?", h == g)
    print("¿h,g = j?", h == j or g == j)

    if failure:
        print("SUCCES: testHand()")
    else:
        print("FAILURE: testHand()")

# ----------------------------------------- Running Test -----------------------------------------

wordlist = loadWords()
testLoadWords(wordlist)
testHand()

