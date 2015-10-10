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
    realword = ''

    # Mediante busqueda binaria trata de acercarse a la palabra que se está buscando

    while low <= high and not found:
        middle = (low + high)//2
        if wordlist[middle] < word:
            possibleword = wordlist[middle]
            low = middle + 1
            # Si es mayor a 3, verificará que la palabra sea la misma, si no,
            # que simplemente se encuentre esa letra en las palabras con las que hace match.

            if len(word) > 3:
                if possibleword.find(word) != -1:
                    realword = possibleword
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
                if possibleword.find(word) != -1:
                    realword = possibleword
                    if possibleword == word:
                        # print("Está la palabra",word)
                        found = True
            else:
                if possibleword.find(word) != -1:
                    # print("Está la palabra",word)
                    found = True
                    break

    if not found:
        return found, realword
    else:
        return found, realword

def counterGhost(ghostword):
    """
    Va devolviendo los caracteres de la palabra 'ghost' cada vez que alguien pierde una partida.
    """

    # Convierte el string recibido en una lista
    ghostword = [ghostword]

    # Va a buscar el string para ir formando la palabra 'ghost'
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

def playHand(wordlist):
    """
    Esta función permite jugar una partida y regresa un valor verdadero cuando se ha perdido
    """
    finalword = []
    fw = ''
    possibleword = ''
    lost = False
    valid = True
    player1 = False

    # Lo va a realizar hasta que algún jugador pierda
    while True:
        if valid and len(fw) <= 3: # Va a validar que siempre que sea verdadero y menor a 3 siga preguntando por letras
            if not player1: # Para ir pasando entre el jugador 1 y 2
                player = 1
                print("Turno del Jugador \033[1;32m{}.\033[1;m".format(player))
                print("\033[1;34mPalabra actual ->\033[1;m", fw.upper())
                word = input("Ingrese una letra: ").lower() # De esta manera lo convierte a minuscula
                while not word.isalpha() or len(word) >= 2: # Verifica que solo sean letras y que no se introduzca más de una letra
                        word = input("Ingrese una letra: ").lower()
                finalword.append(word)
                fw = ''.join(finalword)
                valid, possibleword = isValidWord(fw, wordlist)
                player1 = True
            else:
                player = 2
                print("Turno del Jugador \033[1;32m{}.\033[1;m".format(player))
                print("\033[1;34mPalabra actual:\033[1;m", fw.upper())
                word = input("Ingrese una letra: ").lower()
                while not word.isalpha() or len(word) >= 2:
                        word = input("Ingrese una letra: ").lower()
                finalword.append(word)
                fw = ''.join(finalword)
                valid, possibleword = isValidWord(fw, wordlist)
                player1 = False

        elif valid and len(fw) > 3: # Una vez que es valido y es mayor a 3 se ha perdido el juego
            print("\033[1;31mEl jugador \033[1;32m{}\033[1;m \033[1;31mha perdido con la palabra \033[1;34m{}\033[1;m\033[1;m".format(player, fw.upper()))
            lost = True
            break

        elif not valid: # Si se tiene una palabra no valida
            if possibleword.find(fw) != -1: # Verifica si el fragmento de palabra está en una palabra del diccionario
                if not player1:
                    player = 1
                    print("Turno del Jugador \033[1;32m{}.\033[1;m".format(player))
                    print("\033[1;34mPalabra actual:\033[1;m", fw.upper())
                    word = input("Ingrese una letra: ").lower()
                    while not word.isalpha() or len(word) >= 2:
                        word = input("Ingrese una letra: ").lower()
                    finalword.append(word)
                    fw = ''.join(finalword)
                    valid, possibleword = isValidWord(fw, wordlist)
                    player1 = True
                else:
                    player = 2
                    print("Turno del Jugador \033[1;32m{}.\033[1;m".format(player))
                    print("\033[1;34mPalabra actual:\033[1;m", fw.upper())
                    word = input("Ingrese una letra: ").lower()
                    while not word.isalpha() or len(word) >= 2:
                        word = input("Ingrese una letra: ").lower()
                    finalword.append(word)
                    fw = ''.join(finalword)
                    valid, possibleword = isValidWord(fw, wordlist)
                    player1 = False
            else: # Si no está la palabra, entonces ha perdido el juego
                print("\033[1;31mEl jugador \033[1;32m{}\033[1;m \033[1;31mha perdido con la palabra \033[1;34m{}.\033[1;m\033[1;m".format(player, fw.upper()))
                lost = True
                break

    return lost, player

def playGame(wordlist):
    """
    Esta función es la que inicializa el juego
    """

    while True:
        cmd = input("Ingresa 'n' para jugar una nueva partida o 'e' para salir: ").lower()
        if cmd == 'n':
            player1 = ''
            player2 = ''
            while player1 != 'ghost' and player2 != 'ghost': # Va a realizar el ciclo hasta que alguno de los jugadores
                                                             # conforme la palabra 'ghost'
                lost, player = playHand(wordlist)
                if lost and player == 1:
                    player1 = counterGhost(player1)
                if lost and player == 2:
                    player2 = counterGhost(player2)

            if player1 == 'ghost': # Verifica si el jugador 1 o 2 es el que completo la palabra 'ghost'
                print("EL JUGADOR\033[1;32m 2 \033[1;mHA GANADO EL JUEGO.")
            else:
                print("EL JUGADOR\033[1;32m 1 \033[1;mHA GANADO EL JUEGO.")

        elif cmd == 'e':
            break
        else:
            print("Comando invalido.")


if __name__ == '__main__':
    wordlist = loadWords()
    print("\n\t****************** Ghost Game ******************")
    playGame(wordlist)
