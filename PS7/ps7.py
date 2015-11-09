# -*- coding:utf-8 -*-
# MIT OpenCourseWare
# Review Problems

def fact0(i):
    """
    ¿Cuál es la complejidad de fact0?
    """

    assert type(i) == int and i >= 0    # Al ser constante la verificación, la complejidad es O(1)
    if i == 0 or i == 1:                # O(1)
        return 1                        # O(1)
    return i*fact0(i-1)                 # Dependerá de la cantidad de veces que se ejecute la recursividad, 4 + (i-k)

    # Es una función recursiva con una complejidad lineal: O(n)

def fact1(i):
    """
    ¿Cuál es la complejidad de fact1?
    """

    assert type(i) == int and i >= 0    # O(1)
    res = 1                             # O(1)
    while i > 1:                        # Dependerá del tamaño de i, O(n)
        res *= 1                        # O(1)
        i -= 1                          # O(1)
    return res

    # La suma nos da 2+2n, resultando una complejidad de O(2n) que puede representarse como O(n), siendo una complejidad lineal.

def makeSet(s):
    """
    ¿Cuál es la complejidad de makeSet?
    """
    assert type(s) == str               # O(1)
    res = ''                            # O(1)
    for c in s:                         # Dependerá del tamaño de s, O(n)
        if not c in res:                # O(1)
            res = res + c               # O(1)
    return res

    # La suma nos da 2+2n, resultando una complejidad de O(2n) que puede representarse como O(n), siendo una complejidad lineal.

def intersect(s1, s2):
    """
    ¿Cuál es la complejidad de intersect?
    """

    assert type(s1) == str and type(s2) == str  # O(1)
    s1 = makeSet(s1)                            # Depende de makeSet que es de complejidad lineal, O(2n)
    s2 = makeSet(s2)                            # Depende de makeSet que es de complejidad lineal, O(2n)
    res = ''                                    # O(1)
    for e in s1:                                # Dependerá del tamaño de s1, O(n)
        if e in s2:                             # Sólo hace una verificación, O(1)
            res = res + e                       # O(1)
    return res

    # La suma nos da 1+2n+2n+2n, resultando una complejidad de O(6n) que puede representarse como O(n), siendo una complejidad lineal.

def swap0(s1, s2):
    """
    Hand simulation
    """

    assert type(s1) == list and type(s2) == list
    tmp = s1[:]
    s1 = s2[:]
    s2 = tmp
    return

s1 = [1]
s2 = [2]
swap0(s1, s2)
print(s1, s2)

# s1 = [1], s2 = [2]
# swap0([1],[2])
    # tmp = [1]
    # s1 = [2]
    # s2 = [1]
    # return NONE
# print: [1] [2]

# La función swap0 nunca devuelve el cambio que hace en la función, así que imprime los valores inciales.

def swap1(s1,s2):
    """
    Hand simulation
    """

    assert type(s1) == list and type(s2) == list
    return s2, s1

s1 = [1]
s2 = [2]
s1, s2 = swap1(s1, s2)
print(s1, s2)

# s1 = [1], s2 = [2]
# swap1([1],[2])
    # return [2][1]
# print: [2] [1]

# La función swap1 devuelve los valores recibidos al revés y es lo que se imprime

def rev(s):
    """
    Hand simulation
    """

    assert type(s) == list
    for i in range(len(s)):
        tmp = s[i]
        s[i] = s[-(i+1)]
        s[-(i+1)] = tmp

s = [1,2,3]
rev(s)
print(s)

# s = [1,2,3]
# rev([1,2,3])
    # for i = 0
        # tmp = 1
        # s[0] = 3
        # s[-1] = 1
        # s = [3,2,1]
    # for i = 1
        # tmp = 2
        # s[1] = 2
        # s[-2] = 2
        # s = [3,2,1]
    # for i = 2
        # tmp = 1
        # s[2] = 3
        # s[-3] = 1
        # s = [1,2,3]

# print: [1,2,3]

# La función rev, pone al revés la lista, pero al tener la longitud de la lista lo regresa a su estado original, si se
# declara al iteración hasta len(s)/2 genera un error pues deben ser numeros enteros.