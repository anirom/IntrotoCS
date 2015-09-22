# -*- coding:utf-8 -*-
# MIT OpenCourseWare
# Matching strings: a biological perspective

# Esta funcion toma dos valores, target y key, y regresa un tuple con los valores de los puntos iniciales donde
# el key y target tienen coincidencias

def subStringMatchExact(target,key):

    match = ()
    if key == '':
        return tuple()
    else:
    # Inicia el ciclo para obtener los indices
        for i in range(len(target)):
            # Regresa el indice donde está el match
            start = str.find(target, key)
            targetvalue = len(target[:(start)])
            if start == -1:
                break
            else:
                # Va cortando el rango de busqueda del string target
                target = target[(start + len(key)):]
            if i > 0:
                # El valor de start lo modifica para obtener la posicion real, lo guarda en el tuple
                # y aumenta el valor del contador que actua como el indice
                start = counter + targetvalue
                match = match + (start,)
                counter = start + len(key)
            else:
                counter = targetvalue + len(key)
                match = match + (start,)

    return match
