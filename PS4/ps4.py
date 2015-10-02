# -*- coding:utf-8 -*-
# MIT OpenCourseWare
# Plannig for the future

# Este programa calcula el saldo al fondo del retiro por cada año y lo guarda en una lista.

def nestEggFixed(salary, save, growthrate, years):

    retirementfund = []
    if 0 <= save <= 100 and 0 <= growthrate <= 100:
        for i in range(1,years+1):
            if i == 1:
                retirement = salary*save*0.01
                retirementfund.insert(i-1, retirement)
            else:
                retirement = retirementfund[i-2] *(1+0.01*growthrate) + retirementfund[0]
                retirementfund.insert(i-1,retirement)

        return retirementfund

    else:
        return "Verifica los rangos de los porcentajes"


def testNestEggFixed():

    print(nestEggFixed(10000,10,15,5))
    print(nestEggFixed(5000,5,3,2))
    print(nestEggFixed(4000,0,200,7))

testNestEggFixed()
