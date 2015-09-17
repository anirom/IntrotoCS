# MIT OpenCourseWare EE&CS
# Prime Numbers

# Suma logaritmicamente n numeros primos

#Inicializacion de variables

import math
n = 2
primeNumber = 0
i = 0
resultado = 1

print("Suma de n numeros primos")
i = input("Ingresa el numero hasta el que deseas sumar: ")
while i.isdigit() == False:
    i = input("Ingresa el numero hasta el que deseas sumar: ")

i = int(i)

while i < 2:
    print("Debe ser un numero mayor a 1")
    i = input("Ingresa el numero hasta el que deseas sumar: ")
    i = int(i)

n = 2
primeNumber = 0
# No se detendra hasta que llegue a 1000 numeros primos
for n in range(2,i):
    x = n
    contador = 0
    number = n % x  # Verifica si es una division exacta
    if number == 0:
        contador += 1
        x -= 1
        for x in range(x, 0, -1):  # Disminuye el valor del divisor
            number = n % x
            if number == 0:
                contador += 1
            else:
                x -= 1
    if contador == 2:  # Verifica que solo tenga dos divisiones exactas, que seria entre 1 y su mismo numero
        #print(n)
        primeNumber += 1
        resultado = math.log(n)
        n += n
    else:
        n += 1

print("Suma logaritmica de los numeros primos: {0}".format(resultado))

#primeNumber = math.exp(i)
print("Numeros naturales: {0}".format(primeNumber))
ratio2 = 1/(math.log(resultado/i))
print(ratio2)

