# -*- coding:utf-8 -*-
# MIT OpenCourseWare
# Planning for the future

# Este programa calcula el saldo al fondo del retiro por cada año y lo guarda en una lista.

def nestEggFixed(salary, save, growthrate, years):

    retirementfund = []
    # Verifica que los porcentajes estén dentro del rango
    if 0 <= save <= 100 and 0 <= growthrate <= 100:
        for i in range(1,years+1):
            # Hace el calculo para el primer año y lo agrega a la lista
            if i == 1:
                retirement = salary*save*0.01
                retirementfund.insert(i-1, retirement)
            else:
                # Hace el calculo para el resto de los años y los agrega a la lista
                retirement = retirementfund[i-2] *(1+0.01*growthrate) + retirementfund[0]
                retirementfund.insert(i-1,retirement)

        return retirementfund

    else:
        return "Check the ranges of percentages"

def nestEggVariable(salary, save, growthrates):
    retirementfund = []
    for i in range(1,len(growthrates)+1):
        # Hace el calculo para el primer año y lo agrega a la lista
        if i == 1:
            retirement = salary*save*0.01
            retirementfund.insert(i-1, retirement)
        else:
            # Hace el calculo para los siguientes años y lo agrega a la lista
            retirement = retirementfund[i-2] *(1+0.01*growthrates[i-1]) + retirementfund[0]
            retirementfund.insert(i-1,retirement)

    return retirementfund

def postRetirement(savings, growthrates, expenses):
    retirementfund = []
    for i in range(1,len(growthrates)+1):
        if i == 1:
            # Hace el calculo para el primer año y lo agrega a la lista
            retirement = savings*(1+0.01*growthrates[i-1]) - expenses
            retirementfund.insert(i-1, retirement)
        else:
            # Hace el calculo de los siguientes años y lo agrega a la lista
            retirement = retirementfund[i-2] *(1+0.01*growthrates[i-1]) - expenses
            retirementfund.insert(i-1,retirement)

    return retirementfund

def findMaxExpenses(salary, save, preretiregrowthrates, postretiregrowthrates, epsilon):

    # Determina el valor al principio del retiro
    savings = nestEggVariable(salary, save, preretiregrowthrates)
    low = 0
    high = max(savings)
    # Empieza a calcular los gastos a partir del valor maximo y minimo que se podría gastar
    guess = (low + high)/2
    ctr = 1
    # Determina el valor al final del retiro
    expenses = postRetirement(savings[-1], postretiregrowthrates, guess)[-1]

    # Va a realizar el ciclo, hasta que haya un valor menor a epsilon en la cuenta de retiro
    while abs(expenses) > epsilon and ctr <= 100:
        # Si el valor de los gastos es negativo (esto quiere decir que para el ultimo año de retiro ya se está en deuda)
        # va a poner el valor maximo como la operación 'guess', si no, aumenta el valor de low para reducir la diferencia.
        if expenses < 0:
            high = guess
        else:
            low = guess
        ctr += 1
        guess = (low + high)/2
        expenses = postRetirement(savings[-1], postretiregrowthrates, guess)[-1]

    assert ctr <= 100, 'Iteration count exceeded'
    return guess

def testNestEggFixed():

    print("Retirement fund while you work per year.")
    print(nestEggFixed(10000,10,15,5))
    print(nestEggFixed(5000,5,3,2))
    print(nestEggFixed(4000,0,200,7))

def testNestEggVariable():

    print("\n Retirement fund while you work per year.")
    print(nestEggVariable(10000,10,[3,4,5,0,3]))
    print(nestEggVariable(5000,5,[5,7,6]))
    print(nestEggVariable(4000,3,[3,6,9,12]))

def testPostRetirement():

    print("\n Expenses from retirement fund after retirement.")
    print(postRetirement(100000,[10,5,0,5,1],30000))
    print(postRetirement(70000,[3,5,3],10000))
    print(postRetirement(96700,[2,1,3,8],27500))

def testFindMaxExpenses():

    print("\n Calculates maximum amount of expenses that allows retirement fund")
    print(findMaxExpenses(10000,10,[3,4,5,0,3],[10,5,0,5,1],0.01))
    print(findMaxExpenses(70000,5,[5,7,6],[3,5,3],0.01))
    print(findMaxExpenses(4000,3,[3,6,9,12],[2,1,3,8],0.01))

testNestEggFixed()
testNestEggVariable()
testPostRetirement()
testFindMaxExpenses()


