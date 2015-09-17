# MIT OpenCourseWare EE&CS
# Prime Numbers

# Este programa determinar los primero 1000 numero primos

# Inicializacion de variables
# Los numeros primos son a partir de n>1
n = 2
primeNumber = 0

while primeNumber < 1000:
    x = n
    contador = 0
    number = n%x
    if number == 0:
        contador += 1
        x -= 1
        for x in range(x,0,-1):
            number = n%x
            if number == 0:
                contador += 1
            else:
                x -= 1
    if contador == 2:
        print(n)
        primeNumber += 1
        n += 1
    else:
        n += 1
