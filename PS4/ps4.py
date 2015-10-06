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
        return "Check the ranges of percentages"

def nestEggVariable(salary, save, growthrates):
    years = len(growthrates)
    retirementfund = []
    for i in range(1,years+1):
        if i == 1:
            retirement = salary*save*0.01
            retirementfund.insert(i-1, retirement)
        else:
            retirement = retirementfund[i-2] *(1+0.01*growthrates[i-1]) + retirementfund[0]
            retirementfund.insert(i-1,retirement)

    return retirementfund

def testNestEggFixed():

    print("Retirement fund with salary, save, growthrate, years as inputs")
    print(nestEggFixed(10000,10,15,5))
    print(nestEggFixed(5000,5,3,2))
    print(nestEggFixed(4000,0,200,7))

def testNestEggVariable():

    print("\n Retirement fund with salary, save and growthrate list as inputs ")
    print(nestEggVariable(10000,10,[3,4,5,0,3]))
    print(nestEggVariable(5000,5,[5,7,6]))
    print(nestEggVariable(4000,3,[3,6,9,12]))

testNestEggFixed()
testNestEggVariable()



