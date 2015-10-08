# -*- coding:utf-8 -*-
# MIT OpenCourseWare
# Test for Wordgames

from ps5 import *


#
# Test code
#

# ----------------------------------------- Test Load Words -----------------------------------------

def testLoadWords():
    """
    Unit test for loadWords
    """
    #
    # Verificando que cargue correctamente la lista de palabras validas.
    #
    wordlist = loadWords()
    if type(wordlist) is list:
        print("Loading words...")
        print(" ", len(wordlist), "words loaded.")
    else:
        print("Failed Loading List")


# ----------------------------------------- Test Get Word Score -----------------------------------------

def testGetWordScore():
    """
    Unit test for getWordScore
    """
    #
    # Test para probar que se tienen los scores correctos  por cada palabra.
    #
    failure = False
    # Diccionario con las palabras y scores respectivos.
    words = {("", 7): 0, ("it", 7): 2, ("was", 7): 6, ("love", 7): 7, ("scored", 7): 9, ("waybill", 7): 65,
             ("outgnaw", 7): 61, ("outgnawn", 8): 62}
    for (word, n) in words.keys():
        score = getWordScore(word, n)
        if score != words[(word, n)]:
            print("FAILURE: testGetWordScore()")
            print("\tSe esperaban", words[(word, n)],
                  "puntos, pero se obtuvo '" + str(score) + "' para la palabra '" + word + "', n=" + str(n))
            failure = True

    if not failure: print("SUCCESS: testGetWordScore()")


# ----------------------------------------- Test Get Frequency -----------------------------------------

def testGetFrequencyDict():
    """
    Unit test for getFrequencyDict
    """
    #
    # Test para verificar que devuelve un diccionario con las letras y el numero de repeticiones de estas.
    #
    words = ["lovers", "hello", "luffing"]
    failure = False

    # Test 1
    lovers = {'l': 1, 'o': 1, 'v': 1, 'e': 1, 'r': 1, 's': 1}
    frequency = getFrequencyDict(words[0])
    if lovers == frequency:
        failure = True
    else:
        print("FAILURE (Test 1): testgetFrequencyDict()")
        print("\tSe esperaba", lovers, "y se obtuvo", frequency)

    # Test 2

    hello = {'h': 1, 'e': 1, 'l': 2, 'o': 1}
    frequency = getFrequencyDict(words[1])
    if hello == frequency:
        failure = True
    else:
        print("FAILURE (Test 2): testgetFrequencyDict()")
        print("\tSe esperaba", lovers, "y se obtuvo", frequency)

    # Test 3

    luffing = {'l': 1, 'u': 1, 'f': 2, 'i': 1, 'n': 1, 'g': 1}
    frequency = getFrequencyDict(words[2])
    if luffing == frequency:
        failure = True
    else:
        print("FAILURE (Test 3): testgetFrequencyDict()")
        print("\tSe esperaba", lovers, "y se obtuvo", frequency)

    if failure: print("SUCCESS: testGetFrequencyDict")

# ----------------------------------------- Test Display Hand -----------------------------------------

def testDisplayHand():
    """
    Unit test for displayHand
    """
    #
    # Test para verificar que diplayHand regresa un string de letras
    #
    sequences = ["hpptuab", "olthern", "ncrxesi"]
    failure = False

    for i in range(len(sequences)):
        hand = getFrequencyDict(sequences[i])
        finalhand = displayHand(hand)
        if type(finalhand) == str:
            failure = True
        else:
            failure = False

    if failure:
        print("SUCCESS: testDisplayHand()")
    else:
        print("FAILURE: testDisplayHand()")
        print("\tNo se está obteniendo una lista de regreso")


# ----------------------------------------- Test Deal Hand -----------------------------------------

def testDealHand():
    """
    Unit test for dealHand
    """
    #
    # Test para verificar la aleatoriedad de las letras recibidas
    #
    HAND_SIZE = 7
    repeats = 0

    hand1 = dealHand(HAND_SIZE)
    for i in range(20):  # Hará pruebas para 20 veces
        hand2 = dealHand(HAND_SIZE)
        if hand1 == hand2:  # Si son iguales los diccionarios aleatorios, se irán sumando a repeats
            repeats += 1
        hand1 = hand2

    if repeats > 10:
        # En este caso, si se han repetido más de 10 veces los diccionarios, no está funcionando correctamente
        # la función de aleatoriedad
        print("FAILURE: testDealHand()")
        print("\tHubo una repetición de", repeats, ",para una jugada de", HAND_SIZE, "letras.")
    else:
        print("SUCCESS: testDealHand()")


# ----------------------------------------- Test Update Hand -----------------------------------------

def testUpdateHand():
    """
    Unit test for updateHand
    """
    #
    # Test para verificar que devuelva un diccionario con las palabras restantes
    #
    failure = False

    # Test 1
    hand = {'a': 1, 'q': 1, 'l': 2, 'm': 1, 'u': 1, 'i': 1}
    word = "quail"
    expectedhand = {'l': 1, 'm': 1}

    handupdated = updateHand(hand, word)
    if expectedhand != handupdated:
        print("FAILURE (Test 1): testUpdateHand()")
        print("\tSe esperaba", expectedhand, "y se obtuvo", handupdated)
    else:
        failure = True

    # Test 2
    hand = {'e': 1, 'v': 2, 'n': 1, 'i': 1, 'l': 2}
    word = "evil"
    expectedhand = {'v': 1, 'n': 1, 'l': 1}

    handupdated = updateHand(hand, word)
    if expectedhand != handupdated:
        print("FAILURE (Test 2): testUpdateHand()")
        print("\tSe esperaba", expectedhand, "y se obtuvo", handupdated)
    else:
        failure = True

    # Test 3
    hand = {'h': 1, 'e': 1, 'l': 2, 'o': 1}
    word = "hello"
    expectedhand = {}

    handupdated = updateHand(hand, word)
    if expectedhand != handupdated:
        print("FAILURE (Test 3): testUpdateHand()")
        print("\tSe esperaba", expectedhand, "y se obtuvo", handupdated)
    else:
        failure = True

    if failure: print("SUCCESS: testUpdateHand()")


# ----------------------------------------- Test Is Valid Word -----------------------------------------

def testIsValidWord(wordlist):
    """
    Unit test for isValidWord
    """
    #
    # Test para verificar si la palabra ingresada se conforma de las letras dadas en la partida y que
    # sea una palabra que pertenezca a la lista de palabras validas
    #
    failure = False

    # Test 1

    hand = {'r': 1, 'a': 3, 'p': 2, 'e': 1, 't': 1, 'u': 1}
    word = "rpture"
    valid = isValidWord(word, hand, wordlist)

    if not valid:
        failure = True
    else:
        print("FAILURE (Test 1): testIsValidWord()")
        print("\tSe esperaba un valor False y regresó un valor", valid)

    # Test 2

    hand = {'n': 1, 'h': 1, 'o': 1, 'y': 1, 'd': 1, 'w': 1, 'e': 2}
    word = "honey"
    valid = isValidWord(word, hand, wordlist)

    if valid:
        failure = True
    else:
        print("FAILURE (Test 2): testIsValidWord()")
        print("\tSe esperaba un valor True y regresó un valor", valid)

    # Test 3

    hand = {'e': 1, 'v': 2, 'n': 1, 'i': 1, 'l': 0}
    word = "evil"
    valid = isValidWord(word, hand, wordlist)

    if not valid:
        failure = True
    else:
        print("FAILURE (Test 3): testIsValidWord()")
        print("\tSe esperaba un valor False y regresó un valor", valid)

    # Test 4

    word = "paint"
    valid = isValidWord(word, hand, wordlist)

    if not valid:
        failure = True
    else:
        print("FAILURE (Test 3): testIsValidWord()")
        print("\tSe esperaba un valor False y regresó un valor", valid)

    if failure == True:
        print("SUCCESS: isValidWord()")

# ----------------------------------------- Test Play Hand -----------------------------------------

def testPlayHand(wordlist):
    print("\n\t****************** Word Games ******************")
    hand = dealHand(12)
    playHand(hand, wordlist)

# ----------------------------------------- Running Test -----------------------------------------

wordlist = loadWords()

testLoadWords()
testGetWordScore()
testGetFrequencyDict()
testDisplayHand()
testDealHand()
testUpdateHand()
testIsValidWord(wordlist)
testPlayHand(wordlist)
