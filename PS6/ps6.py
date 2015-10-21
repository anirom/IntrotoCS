# -*- coding:utf-8 -*-
# MIT OpenCourseWare
# Wordgames

# Juego de palabras parecido al Scrabble

import random
import time

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

WORDLIST_FILENAME = "words.txt"

pointsdict = {}
probablewordlist = []

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
    hand: string
    pointsdict: dictionary of words
    """

    # Convierte el objeto set hand a un string para poder usar la función find.
    hand = ''.join(hand)

    if pointsdict[word] and hand.find(word):
        return True
    else:
        return False

def pickBestWord(hand, pointsdict):
    """
    Regresa el valor más alto de la palabra que se puede obtener con las letras dadas.

    Regresa '.' si no se puede formar una palabra con la mano dada.
    """

def getWordsToPoints(wordlist, n):
    """
    Regresa un diccionario que contiene todas las palabras con sus respectivos puntajes
    """

    # Busca cada palabra en la wordlist, obtiene su score y lo almacena en el diccionario pointsdict
    for word in wordlist:
        score = getWordScore(word, n)
        pointsdict.update({word:score})

    return pointsdict

def playHand(hand, wordlist, HAND_SIZE):
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
    playertotaltime = 0
    points = 0
    total = 0

    playertime = input("Ingrese el tiempo límite para los jugadores (en segundos): ")
    while not playertime.isdigit():
        playertime = input("Ingrese el tiempo límite para los jugadores (en segundos): ")
    playertime = int(playertime)

    # Se le muestra al usuario las letras de la jugada
    print("Partida actual:", displayHand(hand))
    strtime = time.time()
    word = input("Introduzca una palabra o un punto (.) si desea finalizar la partida: ").lower()
    endtime = time.time()
    totaltime = endtime - strtime
    playertotaltime = playertime - totaltime
    print("Tiempo de respuesta: {:.2f} segundos. Te quedan: {:.2f} segundos.".format(totaltime, playertotaltime))
    while word != '.': # Se ejecutará siempre y cuando no se introduzca un punto
        while not word.isalpha(): # Para validar que siempre introduza letras
            word = input("Introduzca una palabra o un punto (.) si desea finalizar la partida: ").lower()
        valid = isValidWord(word, hand, wordlist)
        while not valid: # Si la palabra no es valida, volverá a pedirla
            if playertotaltime <= 0:
                print("Tiempo de respuesta: {:.2f} segundos. Tu tiempo ha sobrepasado el tiempo limite.".format(totaltime))
            else:
                strtime = time.time()
                word = input("Lo siento, la palabra que ingresaste no es valida. Prueba con otra palabra: ").lower()
                endtime = time.time()
                totaltime = endtime - strtime
                playertotaltime = playertotaltime - totaltime
                if playertotaltime <= 0:
                    print("Tiempo de respuesta: {:.2f} segundos. Tu tiempo ha sobrepasado el tiempo limite.".format(totaltime))
                    break
                else:
                    print("Tiempo de respuesta: {:.2f} segundos. Te quedan: {:.2f} segundos.".format(totaltime, playertotaltime))

            if word == '.':
                break
            valid = isValidWord(word, hand, wordlist)
        if word == '.':
            break
        else:
            if playertotaltime <= 0:
                break
            else:
                points = getWordScore(word,HAND_SIZE) # LLeva el conteo por palabra
                total = points + total # Lleva el conteo total
                print("Puntos por palabra:", points,"puntos. Total:", total,"puntos.")
                hand = updateHand(hand,word) # Actualiza la partida con las letras que ya se utilizaron
                print("Partida actual:",displayHand(hand))
                strtime = time.time()
                word = input("Introduzca una palabra o un punto (.) si desea finalizar la partida: ").lower()
                endtime = time.time()
                totaltime = endtime - strtime
                playertotaltime = playertotaltime - totaltime
                if playertotaltime <= 0:
                    print("Tiempo de respuesta: {:.2f} segundos. Tu tiempo ha sobrepasado el tiempo limite.".format(totaltime))
                    break
                else:
                    print("Tiempo de respuesta: {:.2f} segundos. Te quedan: {:.2f} segundos.".format(totaltime, playertotaltime))
    print("Score final:", total, "puntos. Tiempo de respuesta mayor a", playertime, "segundos.")

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
            playHand(hand, wordlist, HAND_SIZE, pointsdict)
            print()
        elif cmd == 'r':
            if handOrg == None:
                print("No se han iniciado partidas.")
            else:
                playHand(handOrg, wordlist, HAND_SIZE)
                print()
        elif cmd == 'e':
            break
        else:
            print("Comando invalido.")

if __name__ == '__main__':
    wordlist = loadWords()
    print("\n\t****************** Words Game ******************")
    playGame(wordlist)

