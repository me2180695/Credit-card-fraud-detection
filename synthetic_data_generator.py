import numpy as np
from numpy import random
import xlsxwriter

np.random.seed(123)

def markov(currSt):
    if(currSt == 'g'):
        i = np.random.rand()
        if(i<0.05):
            return('f')
        else:
            return('g')
    else:
        i = np.random.rand()
        if(i<0.025):
            return('f')
        else:
            return('g')
        
def genTrans(n):
    lambdaG = 1/12
    lambdaF = 1/4
    muG = 50
    muF = 80
    sigmaG = 6
    sigmaF = 12
    state = 'g'
    Y = []
    transAmt = []
    tBtwTrans = []

    for i in range(0,n):
        nextTrans= markov(state)
        if (nextTrans == 'g'):
            state = nextTrans
            Y.append(1)
            transAmt.append(max(0,np.random.normal(muG,sigmaG)))
            tBtwTrans.append(np.random.exponential(lambdaG))
        else:
            state = nextTrans
            Y.append(0)
            transAmt.append(max(0,np.random.normal(muF,sigmaF)))
            tBtwTrans.append(np.random.exponential(lambdaF))

    output = [Y,tBtwTrans,transAmt]

    workbook = xlsxwriter.Workbook("2018ME20695_6_1.xlsx")
    worksheet = workbook.add_worksheet()
    worksheet.write(0,0,"Y(Genuine-1,fraudulent-0)")
    worksheet.write(0,1,"Time between transactions")
    worksheet.write(0,2,"Amount of transaction")

    for row in range(1,n+1):
        for col in range(0,3):
            worksheet.write(row,col,output[col][row-1])

    workbook.close()

genTrans(10000)
