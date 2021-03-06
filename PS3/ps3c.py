# -*- coding:utf-8 -*-
# MIT OpenCourseWare
# Matching strings: a biological perspective

# Programa que separa la key principal en dos tuple y averigua si hay elementos sustituibles y no sustituibles

from ps3b import subStringMatchExact

def constrainedMatchPair(tupkeyone, tupkeytwo, m):

    validmatch = ()

    for n in tupkeyone:
        for k in tupkeytwo:
            if n + m + 1 == k:
                validmatch += (n,)


    return validmatch

def subStringMatchOneSub(target, key):

    allmatches = ()

    for i in range(0,len(key)):
        keyone = key[:i]
        keytwo = key[i+1:]
        #print('\nRompiendo la key: ', key, 'en key1 = ', keyone, 'y key2 = ', keytwo)
        matchone = subStringMatchExact(target, keyone)
        matchtwo = subStringMatchExact(target, keytwo)
        #print('El primer match: ',matchone)
        #print('El segundo match: ',matchtwo)
        validmatch = constrainedMatchPair(matchone, matchtwo, len(keyone))
        allmatches = allmatches + validmatch
        #print('Posibles matches para sustituir', validmatch)

    return allmatches

#print('Las posibles sustituciones son en: ', subStringMatchOneSub('ATGACATGCACAAGTATGCAT','ATG'))