# -*- coding:utf-8 -*-
# MIT OpenCourseWare
# Test for Wordgames

from ps5 import *

#
# Test code
#

def testLoadWords():
    """
    Unit test for loadWords
    """

    # Verificando que cargue correctamente la lista de palabras validas.

    wordlist = loadWords()
    if type(wordlist) is list:
        print("Loading words...")
        print("   SUCCESS:", len(wordlist), "words loaded.")
    else:
        print("FAILURE LOADING LIST")

def testGetWordScore():
    """
    Unit test for getWordScore
    """

    # Test para probar que se tienen los scores correctos  por cada palabra.

    failure = False
    # Diccionario con las palabras y scores respectivos.
    words = {("", 7):0, ("it", 7):2, ("was", 7):6, ("love",7):7,("scored", 7):9, ("waybill", 7):65, ("outgnaw", 7):61, ("outgnawn", 8):62}
    for (word, n) in words.keys():
        score = getWordScore(word, n)
        if score != words[(word, n)]:
            print("FAILURE: testGetWordScore()")
            print("\tSe esperaban", words[(word, n)], "puntos, pero se obtuvo '" + str(score) + "' para la palabra '" + word + "', n=" + str(n))
            failure = True
    if not failure:
        print("SUCCESS: testGetWordScore()")

def testGetFrequencyDict():
    """
    Unit test for getFrequencyDict
    """

    # Test para verificar que devuelve un diccionario con las letras y el numero de repeticiones de estas.

    sequences = ["lovers", "hello", "luffing"]
    lovers = {'l':1,'o':1,'v':1,'e':1,'r':1,'s':1}
    hello = {'h':1,'e':1,'l':2,'o':1}
    luffing = {'l':1,'u':1,'f':2,'i':1,'n':1,'g':1}
    failure = False

    for i in range(len(sequences)):
        frequency = getFrequencyDict(sequences[i])
        if frequency == lovers or hello or luffing:
            failure = True
        else:
            failure = False

    if failure == True:
        print("SUCCESS: testGetFrequencyDict()")
    else:
        print("FAILURE: testGeFrequencyDict()")

def testDisplayHand():
    """
    Unit test for displayHand
    """

    # Test para verificar que imprime de forma vertical una cadena random de caracteres

    sequences = ["hpptuab", "olthern", "ncrxesi"]
    failure = False

    for i in range(len(sequences)):
        hand = getFrequencyDict(sequences[i])
        finalhand = displayHand(hand)
        if finalhand == sequences[0] or sequences[1] or sequences[2]:
            # print(finalhand)
            failure = True
        else:
            failure = False

    if failure == True:
        print("SUCCESS: testDisplayHand()")
    else:
        print("FAILURE: testDisplayHand()")

def testDealHand():
    """
    Unit test for dealHand
    """

    # Test para verificar la aleatoriedad de las letras recibidas

    HAND_SIZE = 7
    repeats = 0

    hand1 = dealHand(HAND_SIZE)
    for i in range(20): # Hará pruebas para 20 veces
        hand2 = dealHand(HAND_SIZE)
        if hand1 == hand2: # Si son iguales los diccionarios aleatorios, se irán sumando a repeats
            repeats += 1
        hand1 = hand2

    if repeats > 10:
        # En este caso, si se han repetido más de 10 veces los diccionarios, no está funcionando correctamente
        # la función de aleatoriedad
        print("FAILURE: testDealHand()")

    print("SUCCESS: testDealHand()")

# ----------------------------------------- Running Test -----------------------------------------

testLoadWords()
testGetWordScore()
testGetFrequencyDict()
testDisplayHand()
testDealHand()
