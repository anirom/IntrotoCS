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

# ----------------------------------------- Test Player -----------------------------------------

def testPlayer():
    """
    Unit test for testPlayer Class
    """

    print("\n ---------- Test Player ---------")

    failure = False
    hand = {'c':1, 'a':1, 'b':1 ,'d':1, 'o':1, 'e':1}

    p1 = Player(1, Hand(6, hand))
    p2 = Player(2, Hand(6, hand))

    if not p1.getHand() == hand and p2.getHand() == hand:
        failure = True
        print("FAILURE: Se esperaría la mano que se ingresó:", hand,"y se está regresando:", p1.getHand())

    if not p1.getIdNum() == '1' and p2.getIdNum() == '2':
        failure = True
        print("FAILURE: Se espera que p1 sea el jugador 1 y p2 sea el jugador 2, y se está obteniendo:", p1.getIdNum(),
              p2.getIdNum())

    print("Jugador 1")
    print("\t", p1.addPoints(5))
    print("\t", p1.addPoints(12))
    if not p1.getScore() == 17:
        failure = True
        print("FAILURE: Se esperan 17 puntos, y se están obteniendo:", p1.getScore())
    print(p1)

    print("Jugador 2")
    print("\t", p2.addPoints(3))
    print("\t", p2.addPoints(10))
    if not p2.getScore() == 13:
        failure = True
        print("FAILURE: Se esperan 13 puntos, y se están obteniendo:", p1.getScore())
    print(p2)

    if not (p1 > p2) == 1:
        failure = True
        print("FAILURE: Se esperaba un 1, indicando que el puntaje del P1 es mayor al del P2. Se está regresando:",
              p1 > p2)
    if not (p1 < p2) == -1:
        failure = True
        print("FAILURE: Se esperaba un -1, indicando que el puntaje del P2 es menor al del P1. Se está regresando:",
              p2 < p1)
    if (p1 == p2):
        failure = True
        print("FAILURE: Se esperaba un valor falso y se está obteniendo:",
              p2 < p1)

    if not failure:
        print("SUCCES: testPlayer()")
    else:
        print("FAILURE: testPlayer()")

# ----------------------------------------- Running Test -----------------------------------------

wordlist = loadWords()
testLoadWords(wordlist)
testHand()
testPlayer()

