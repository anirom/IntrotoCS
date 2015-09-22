# -*- coding:utf-8 -*-
# MIT OpenCourseWare
# Matching strings: a biological perspective

# Programa que separa la key principal en dos tuple y averigua si hay elementos sustituibles

from ps3c import subStringMatchOneSub
from ps3b import subStringMatchExact

def subStringMatchExactlyOneSub(target,key):

    onesubstitution = ()
    perfectmatch = subStringMatchExact(target,key)
    #print(perfectmatch)
    possiblesubstitution = subStringMatchOneSub(target,key)
    #print(possiblesubstitution)


    for onesub in possiblesubstitution:
        if onesub in perfectmatch:
            pass
        else:
            onesubstitution = onesubstitution + (onesub,)

    return onesubstitution

print('Las sustitucion(es) se dara(n) a partir de: ', subStringMatchExactlyOneSub('ATGACATGCACAAGTATGAAGCAT','ATG'))


