# MIT OpenCourseWare EE&CS
# Prime Numbers

# Este programa determinar los primero 1000 numero primos

# Inicializacion de variables
# Los numeros primos son a partir de n>1
n = 2
primeNumber = 0

while primeNumber < 1000: # Seguirá corriendo hasta que llegue a 1000 numeros primos
    x = n
    contador = 0
    number = n%x # Verifica si es una division exacta
    if number == 0:
        contador += 1
        x -= 1
        for x in range(x,0,-1): # Va disminuyendo el valor del divisor
            number = n%x
            if number == 0: # Verifica si es exacta o no la division
                contador += 1
            else:
                x -= 1
    if contador == 2: # Se usa para verificar que sólo tenga dos divisiones exactas. Que fuera entre 1 y el mismo numero
        print(n)
        primeNumber += 1
        n += 1
    else:
        n += 1
