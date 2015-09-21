# -*- coding:utf-8 -*-
# MIT OpenCourseWare
# Matching strings: a biological perspective

# Calcula el numero de veces que aparece una palabra clave en un string, sin uso de la función .find()

def countSubStringMatch(target, key):

    numKey = 0

    for i in range(0,len(target)):
        chTarget = target[i]
        if chTarget is key[0]:
            for j in range(0,len(key)-1):
                chTarget = target[i+1]
                chKey = key[j+1]
                if chTarget is chKey:
                    if j == len(key)-2:
                        numKey += 1
                    else:
                        i += 1
                else:
                    break

    return numKey

def countSubStringMatchRecursive(target, key):
    start = str.find(target,key)
    if start >= 0:
        target = target[(start+len(key)):]
        return 1 + countSubStringMatchRecursive(target, key)
    else:
        return 0