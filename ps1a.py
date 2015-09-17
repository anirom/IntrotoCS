# MIT OpenCourseWare EE&CS
# Prime Numbers

# Este programa determinar los primero 1000 numero primos

# Inicializacion de variables
# Los numeros primos son a partir de n>1
n = 2
primeNumber = 0

# No se detendra hasta que llegue a 1000 numeros primos
while primeNumber < 1000:
    x = n
    contador = 0
    # Verifica si es una division exacta
    number = n%x
    if number == 0:
        contador += 1
        x -= 1
        # Disminuye el valor del divisor
        for x in range(x,0,-1):
            number = n%x
            if number == 0:
                contador += 1
            else:
                x -= 1
    # Verifica que solo tenga dos divisiones exactas, que seria entre 1 y su mismo numero
    if contador == 2:
        print(n)
        primeNumber += 1
        n += 1
    else:
        n += 1
