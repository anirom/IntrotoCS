# -*- coding:utf-8 -*-
# MIT OpenCourseWare
# Wordgames: Ghost

import random

##
# En este juego participan dos jugadores, cada uno toma turno para escribir una letra de un fragmento de una
# palabra intentando no completarla. Al completar una palabra mayor a 3 caracteres, o escribir una letra
# que no pueda conformar una palabra se pierde la partida. Cuando se pierde una partida se va ganando una letra de
# la palabra 'GHOST'. El primero que complete esta palabra, pierde el juego.
##

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

def isValidWord(word, wordlist):
    """
    Regresa True si se tiene una palabra valida, y False si no lo es.
    """

    found = False
    low = 0
    high = len(wordlist)-1

    # Mediante busqueda binaria trata de acercarse a la palabra que se está buscando y con el método .find()
    # asegura que la palabra sea la misma

    while low <= high and not found:
        middle = (low + high)//2
        if wordlist[middle] < word:
            possibleword = wordlist[middle]
            low = middle + 1
            # print(wordlist[middle])
            if possibleword.find(word) != -1:    # De esta manera confirma que la palabra posible
                # print("Está la palabra",word)  # tenga al menos los caracteres del fragmento
                found = True
                break

        else:   # wordlist[middle] > word
            possibleword = wordlist[middle]
            high = middle - 1
            # print(wordlist[middle])
            if possibleword.find(word) != -1:
                # print("Está la palabra",word)
                found = True
                break

    if not found:
        return found
    else:
        return found

if __name__ == '__main__':
    wordlist = loadWords()
    print("\n\t****************** Ghost Game ******************")
    #playGame(wordlist)
