# -*- coding:utf-8 -*-
# MIT OpenCourseWare
# Matching strings: a biological perspective

# Una secuencia de ADN es comúnmente representada como una secuencia de 4 nucleotidos:
# Adeninda (A), Citosina (C), Guanina (G) y Timina (T) y por lo tanto una molecula de ADN está representado
# por una cadena compuesta de elementos alfabeticos de sólo 4 símbolos

# Este programa encuentra el numero de veces que aparece una key string en un string dado
import string

def iterativeFunction(s,fs):

    numberKey = 0
    start = 0
    end = len(s)
    for i in range(end):
        start = s.find(fs,start)
        if start == -1:
            break
        else:
            start += 1
            numberKey += 1

    return numberKey

def recursiveFunction(s,fs,start = 0, numKey = 0):
    start = s.find(fs,start)
    if start == -1:
        return numKey
    else:
        return recursiveFunction(s,fs,start+1, numKey+1)

print(iterativeFunction("attgcacgttgattgacttca","tt"))
print(iterativeFunction("attgcacgttgattgacttca","ttg"))
print(iterativeFunction("attgcacgttgattgacttca","ttga"))
print(recursiveFunction("attgcacgttgattgacttca","tt"))
print(recursiveFunction("attgcacgttgattgacttca","ttg"))
print(recursiveFunction("attgcacgttgattgacttca","ttga"))
