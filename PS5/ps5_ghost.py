# -*- coding:utf-8 -*-
# MIT OpenCourseWare
# Wordgames: Ghost

import random
import string

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

def isValidWord(word, wordlist):
    """
    Regresa True si se tiene una palabra valida, y False si no lo es.
    """

    found = False
    low = 0
    high = len(wordlist)-1

    # Mediante busqueda binaria trata de acercarse a la palabra que se está buscando

    while low <= high and not found:
        middle = (low + high)//2
        if wordlist[middle] < word:
            possibleword = wordlist[middle]
            low = middle + 1
            # Si es mayor a 3, verificará que la palabra sea la misma, si no,
            # que simplemente se encuentre esa letra en las palabras con las que hace match.

            if len(word) > 3:
                if possibleword == word:
                    # print("Está la palabra",word)
                    found = True
            else:
                if possibleword.find(word) != -1:
                    # print("Está la palabra",word)
                    found = True
                    break

        else:   # wordlist[middle] > word
            possibleword = wordlist[middle]
            high = middle - 1
            # Si es mayor a 3, verificará que la palabra sea la misma, si no,
            # que simplemente se encuentre esa letra en las palabras con las que hace match.

            if len(word) > 3:
                if possibleword == word:
                    # print("Está la palabra",word)
                    found = True
            else:
                if possibleword.find(word) != -1:
                    # print("Está la palabra",word)
                    found = True
                    break

    if not found:
        return found
    else:
        return found

def counterGhost(ghostword):
    """
    Va devolviendo los caracteres de la palabra 'ghost' cada vez que alguien pierde una partida.
    """

    ghostword = [ghostword]

    if ghostword == ['']:
        ghostword.append('g')
        gw = ''.join(ghostword)
    elif ghostword == ['g']:
        ghostword.append('h')
        gw = ''.join(ghostword)
    elif ghostword == ['gh']:
        ghostword.append('o')
        gw = ''.join(ghostword)
    elif ghostword == ['gho']:
        ghostword.append('s')
        gw = ''.join(ghostword)
    elif ghostword == ['ghos']:
        ghostword.append('t')
        gw = ''.join(ghostword)

    return gw

if __name__ == '__main__':
    wordlist = loadWords()
    print("\n\t****************** Ghost Game ******************")
    #playGame(wordlist)
