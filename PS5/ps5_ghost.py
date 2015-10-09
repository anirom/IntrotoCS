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
