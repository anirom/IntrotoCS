# -*- coding:utf-8 -*-
# MIT OpenCourseWare
# Wordgames

# Juego de palabras parecido al Scrabble

import random
import time
from itertools import permutations

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

WORDLIST_FILENAME = "words.txt"

pointsdict = {}
possibleword = {}
timelimit = 0

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

def isValidWord(word, hand, pointsdict):
    """
    Regresa verdadero si la palabra está en la lista y está
    compuesta por las letras que se tienen en la jugada.
    De otro modo, regresa falso.
    No hay que cambiar ni la jugada o la lista de palabras.

    word: string
    pointsdict: dictionary of words
    """

    valid = False
    modhand = hand.copy()

    # Como se recibe un diccionario se utilza para buscar la palabra.
    for letter in word:
        if letter in hand and modhand[letter] >= 1:
            value = modhand[letter] - 1
            modhand[letter] = value
            valid = True
        else:
            return False

    if valid:
        worddict = pointsdict.get(word, None)
        if worddict is None:
            return False
        else:
            return True

def getWordsToPoints(wordlist, n):
    """
    Regresa un diccionario que contiene todas las palabras con sus respectivos puntajes
    """

    # Toma cada palabra en la lista y forma un diccionario con la palabra y sus puntos equivalentes

    for word in wordlist:
        score = getWordScore(word, n)
        pointsdict.update({word:score})

    return pointsdict

def getTimeLimit(pointsdict, k, HAND_SIZE):
    """
    Regresa el tiempo limite para el jugador como una función de k multiplicado.
    """

    starttime = time.time()
    # Hace algunos calculos. El proposito es calcular cuanto tiempo le llevó a la computadora realizar la tarea.
    for word in pointsdict:
        getFrequencyDict(word)
        getWordScore(word, HAND_SIZE)
    endtime = time.time()
    return (endtime - starttime) * k

def getPossibleWord(hand):
    """
    Esta función toma el hand de letras y regresa una lista de palabras posibles.
    """

    finalhand = ''
    pw = {}

    for letter in hand.keys():
        for j in range(hand[letter]):
            finalhand = finalhand + letter

    for L in range(2, len(finalhand)+1):
        for subset in permutations(finalhand, L):
            word = ''.join(subset)
            # print(word)
            pw.update({word: word})

    return pw

def pickBestWordFaster(hand, possibleword):
   """
   Recibe dos diccionarios y revisa cuales palabras son posibles y regresa el valor mas alto que se puede obtener con la mano dada

   hand: dictionary
   possibleword: dictionary
   """
    bestword = ''
    bestwordvalue = 0

    words = possibleword.values()
    for word in words:
        if word in pointsdict:
            wordvalue = pointsdict[word]
            if wordvalue > bestwordvalue:
                # print(word)
                bestwordvalue = pointsdict[word]
                bestword = word

    if bestwordvalue > 0:
        # print(bestword, bestwordvalue)
        return bestword, bestwordvalue

    return '.'

def pickBestWord(hand, pointsdict):
    """
    Regresa la palabra con el valor más alto que se puede obtener con las letras dadas.

    Regresa '.' si no se puede formar una palabra con la mano dada.

    hand: dictionary (string -> int)
    pointsdict: dictionary (string -> int)

    La complejidad de este algoritmo es de O(n) (lineal)
    """

    bestwordvalue = 0

    # Va a revisar para
    for word in pointsdict:
        valid = isValidWord(word, hand, pointsdict)
        if valid:
            wordvalue = pointsdict[word]
            if wordvalue > bestwordvalue:
                bestwordvalue = pointsdict[word]
                bestword = word
                # print(bestword, bestwordvalue)

    if bestwordvalue > 0:
        # print(bestword, bestwordvalue)
        return bestword, bestwordvalue

    return '.'

def playHand(hand, HAND_SIZE, pointsdict):
    """
    Permite al usuario jugar en modo computadora
    """
    total = 0
    k = 1

    playertime = getTimeLimit(pointsdict, k, HAND_SIZE)

    print("Tiempo limite para dar una respuesta:", playertime)
    print("Partida actual:", displayHand(hand))

    possibleword = getPossibleWord(hand)
    strtime = time.time()
    word = pickBestWordFaster(hand, possibleword) # Determina la mejor palabra con las letras dadas
    endtime = time.time()
    totaltime = endtime - strtime
    playertotaltime = playertime - totaltime
    points = pointsdict[word[0]]

    total = points + total  # Lleva el conteo total
    print("La mejor palabra es:", word[0])
    print("Puntos por palabra:", points, "puntos. Total:", total, "puntos.")
    print("Tiempo de respuesta: {:.2f} segundos. Te quedan: {:.2f} segundos.".format(totaltime, playertotaltime))

    hand = updateHand(hand,word[0]) # Actualiza la partida con las letras que ya se utilizaron

    while word[0] != '.': # Se ejecutará siempre y cuando no se introduzca un punto
        print("Partida actual:", displayHand(hand))
        possibleword = getPossibleWord(hand)
        strtime = time.time()
        word = pickBestWordFaster(hand, possibleword)  # Determina la mejor palabra con las letras dadas
        endtime = time.time()
        totaltime = endtime - strtime
        playertotaltime = playertotaltime - totaltime
        if word[0] != '.' and playertotaltime < playertime:
            print("La mejor palabra es:", word[0])
            print("Puntos por palabra:", points, "puntos. Total:", total, "puntos.")
            print("Tiempo de respuesta: {:.2f} segundos. Te quedan: {:.2f} segundos.".format(totaltime, playertotaltime))
            hand = updateHand(hand, word[0])  # Actualiza la partida con las letras que ya se utilizaron
        else:
            print("Ya no hay más palabras.")
            break

    print("Score final:", total, "puntos. Tiempo que te quedó:",playertotaltime, "segundos.")

def playGame(wordlist):
    """
    Permite al usuario jugar una n cantidad de

    * Pregunta al usuario ingresar, 'n' ó 'r' ó 'e'.

    * Si el usuario ingresa 'n', se le permite empezar una nueva jugada.
      Cuando termine la jugada, se le vuelve a preguntar por cualquiera de las 3 opciones.

    * Si el usuario elige 'r', deja al usuario que juegue la última mano de nuevo.

    * Si el usuario elige 'e', sale del juego.

    * Si el usuario elige cualquier otra opcion, debe volver a pregunta.
    """

    HAND_SIZE = input("Elige cuantas letras quieres para la partida: ")
    while not HAND_SIZE.isdigit(): # Para verificar que sea siempre numeros
        HAND_SIZE = input("Sólo se aceptan números enteros. Elige cuantas letras quieres para la partida: ")
    HAND_SIZE = int(HAND_SIZE) # Para pasar de string a entero
    pointsdict = getWordsToPoints(wordlist, HAND_SIZE)
    handOrg = None


   # Mientras se cumpla alguna de las siguientes
    while True:
        cmd = input("Ingresa 'n' para jugar una nueva partida, 'r' para repetir la partida anterior y 'e' para salir: ").lower()
        if cmd == 'n' :
            hand = dealHand(HAND_SIZE)
            handOrg = hand.copy() # De esta manera se almacena la partida creada en este juego
            playHand(hand, HAND_SIZE, pointsdict)
            print()
        elif cmd == 'r':
            if handOrg == None:
                print("No se han iniciado partidas.")
            else:
                playHand(handOrg, HAND_SIZE, pointsdict)
                print()
        elif cmd == 'e':
            break
        else:
            print("Comando invalido.")

if __name__ == '__main__':
    wordlist = loadWords()
    print("\n\t****************** Words Game ******************")
    playGame(wordlist)

