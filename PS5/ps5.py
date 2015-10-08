# -*- coding:utf-8 -*-
# MIT OpenCourseWare
# Wordgames

# Juego de palabras parecido al Scrabble

import string
import random

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Regresa todas las palabras válidas que se usarán para la partida,
    todas conformadas por letras minúsculas.

    El archivo words.txt es el que contiene las palabras validas.
    """

    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    return wordlist

def getFrequencyDict(sequence):
    """
    Regresa un diccionario donde las claves son letras de la partida
    y los valores son los recuentos, el numero de veces que un elemento
    es repetido en la partida.

    sequence: string or list
    return: dictionary
    """

    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq

#
# Problem #1: Scoring a word
#

def getWordScore(word, n):
    """
    Regresa el score para cada palabra, asumiendo que la palabra es valida.

    El score para cada palabra es la suma de los puntos de cada letra
    en la palabra, más 50 puntos si todas las letras son utilizadas.

    Los valores de cada letras son como en el Scrabble y están almacenadas
    en el diccionario SCRABBLE_LETTER_VALUES.

    word: string (lowercase letters)
    returns: int >= 0
    """

    total = 0

    # Hace la comparación del string recibido con el diccionario de valores para obtener el total.
    for key in word:
        if key in SCRABBLE_LETTER_VALUES:
            value = SCRABBLE_LETTER_VALUES[key]

        total = total + value

    if len(word) == n:
        total += 50
    return total

def displayHand(hand):
    """
    Muestra las letras disponibles en la jugada.

    Por ejemplo:
       displayHand({'a':1, 'x':2, 'l':3, 'e':1})
    Debería imprimir algo como:
       a x x l l l e
    El orden de las palabras no es importante.

    hand: dictionary (string -> int)
    """

    finalhand = ""

    for letter in hand.keys():
        for j in range(hand[letter]):
            finalhand = finalhand + letter + " " # Almacena letra por letra para mostrarlo de forma horizontal

    return finalhand

def dealHand(n):
    """
    Regresa, de forma random, la 'n' cantidad de letras, en minúsculas.
    Al menos n/3 letras deben ser vocales.

    Las jugadas son representadas como diccionarios. Donde las keys
    son las letras y los valores son los numeros de veces que se repite
    esa letra en esa jugada.

    n: int >= 0
    returns: dictionary (string -> int)
    """

    hand = {}
    num_vowels = n // 3

    # Genera una selección random de vocales
    for i in range(num_vowels):
        x = VOWELS[random.randrange(0,len(VOWELS))]
        hand[x] = hand.get(x, 0) + 1

    # Genera una selección random de consonantes
    for i in range(num_vowels, n):
        x = CONSONANTS[random.randrange(0,len(CONSONANTS))]
        hand[x] = hand.get(x, 0) + 1
    return hand

#
# Problem #2: Update a hand by removing letters
#
def updateHand(hand, word):
    """
    Asumimos que la jugada tiene todas las letras que conforman la palabra.

    Actualiza la jugada: Utiliza las letras de la palabra dada y regresa
    las letras restantes de esa jugada.

    No hay efectos secundarios: así que no cambian las letras.

    word: string
    hand: dictionary (string -> int)
    returns: dictionary (string -> int)
    """

    # Busca cada letra de la palabra en el diccionario y le va restando una unidad a la cantidad de veces que
    # aparece la letra
    for letter in word:
        if letter in hand:
            hand[letter] = hand[letter] - 1
            if hand[letter] == 0:
                del hand[letter]

    return hand

#
# Problem #3: Test word validity
#
def isValidWord(word, hand, wordlist):
    """
    Regresa verdadero si la palabra está en la lista y está
    compuesta por las letras que se tienen en la jugada.
    De otro modo, regresa falso.
    No hay que cambiar ni la jugada o la lista de palabras.

    word: string
    hand: dictionary (string -> int)
    word_list: list of lowercase strings
    """

    valid = False
    found = False
    low = 0
    high = len(wordlist)-1

    # Primero se verifica que la palabra esté compuesta por las letras dadas en la jugada
    for letter in word:
        if letter in hand and hand[letter] >= 1:
            valid = True
        else:
            return False

    # Una vez verificada que la palabra esté conformada con las letras de la jugada,
    # se hará la busqueda de la palabra dada en la ista de las palabras validas
    # mediante una busqueda binaria
    if valid == True:
        while low <= high and not found:
            middle = (low + high)//2
            if wordlist[middle] < word:
                low = middle + 1
                # print(wordlist[middle])
            elif wordlist[middle] > word:
                high = middle - 1
                # print(wordlist[middle])
            else:
                found = True

    if not found:
        return found
    else:
        return found

#
# Problem #4: Playing a hand
#
def playHand(hand, wordlist):
    """
    Permite al usuario jugar la mano dada, como sigue:

    * Se muestra la jugada.

    * El usuario puede introducir una palabra.

    * Una palabra invalida es rechazada y un mensaje aparece pidiéndole al
      usuario otra palabra.

    * Cuando se introduce una palabra valida, se usan las letras de la jugada.

    * Después de cada palabra valida: el score de la palabra y el score total se
      muestran, las letras restantes se muestran en la jugada y al usuario se le pide
      otra palabra.

    * La suma del score de la palabra se muestra cuando termina la jugada.

    * La jugada termina cuando no haya mas letras sin usar.
      El usuario puede terminar la partida ingresando el caracter '.'
      en lugar de una palabra.

    * Se muestra el marcador final.

      hand: dictionary (string -> int)
      word_list: list of lowercase strings
    """
    total = 0

    # Se le muestra al usuario las letras de la jugada
    print("Partida actual:", displayHand(hand))
    word = input("Introduzca una palabra o un punto (.) si desea finalizar la partida: ").lower()
    while word != '.': # Se ejecutará siempre y cuando no se introduzca un punto
        while not word.isalpha(): # Para validar que siempre introduza letras
            word = input("Introduzca una palabra o un punto (.) si desea finalizar la partida: ").lower()
        valid = isValidWord(word, hand, wordlist)
        while not valid: # Si la palabra no es valida, volverá a pedirla
            word = input("Lo siento, la palabra que ingresaste no es valida. Prueba con otra palabra: ").lower()
            valid = isValidWord(word, hand, wordlist)
        points = getWordScore(word,HAND_SIZE) # LLeva el conteo por palabra
        total = points + total # Lleva el conteo total
        print("Puntos por palabra:", points,"puntos. Total:", total," puntos.")
        hand = updateHand(hand,word) # Actualiza la partida con las letras que ya se utilizaron
        print("Partida actual:",displayHand(hand))
        word = input("Introduzca una palabra o un punto (.) si desea finalizar la partida: ").lower()
    print("Score final:", total)

#
# Problem #5: Playing a game
#
def play_game(word_list):
    """
    Permite al usuario jugar una n cantidad de

    * Pregunta al usuario ingresar, 'n' ó 'r' ó 'e'.

    * Si el usuario ingresa 'n', se le permite empezar una nueva jugada.
      Cuando termine la jugada, se le vuelve a preguntar por cualquiera de las 3 opciones.

    * Si el usuario elige 'r', deja al usuario que juegue la última mano de nuevo.

    * Si el usuario elige 'e', sale del juego.

    * Si el usuario elige cualquier otra opcion, debe volver a pregunta.
    """
    # TO DO ...
    print("play_game not implemented.")         # delete this once you've completed Problem #4
    play_hand(deal_hand(HAND_SIZE), word_list)  # delete this once you've completed Problem #4

    ## uncomment the following block of code once you've completed Problem #4
#    hand = deal_hand(HAND_SIZE) # random init
#    while True:
#        cmd = raw_input('Enter n to deal a new hand, r to replay the last hand, or e to end game: ')
#        if cmd == 'n':
#            hand = deal_hand(HAND_SIZE)
#            play_hand(hand.copy(), word_list)
#            print
#        elif cmd == 'r':
#            play_hand(hand.copy(), word_list)
#            print
#        elif cmd == 'e':
#            break
#        else:
#            print "Invalid command."

#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    word_list = loadWords()
    play_game(word_list)
