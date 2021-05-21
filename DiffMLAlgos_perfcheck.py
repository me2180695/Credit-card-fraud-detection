import numpy as np
import xlrd
from sklearn.ensemble import BaggingClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC

def printRes(clf,Xtest,Ytest):
    TP =0
    FP =0
    TN =0
    FN =0
    for i in range(0,2500):
        r = clf.predict([Xtest[i]])
        if (Ytest[i] == 1.0):
            if(r ==1.0):
                TP +=1
            else:
                FN+=1
        else:
            if(r == 1.0):
                FP += 1
            else:
               TN += 1
    print("Rates- TP:%f,TN:%f,FP:%f,FN:%f"%(TP/(TP+FN),TN/(TN+FP),FP/(FP+TN),FN/(FN+TP)))
    R = TP/(TP+FN)
    S = TN/(FP+TN)
    MFS = (2*R*S)/(R+S)
    print("Recall: %f,Specifictiy:%f"%(R,S))
    print("modified f1 score: %f \n"%(MFS))


Xtrain = []
Ytrain = []
Xtest = []
Ytest = []

workbook = xlrd.open_workbook("2018ME20695_6_1.xlsx")
worksheet = workbook.sheet_by_index(0)
for i in range(1,7501):
    Xvalue = []
    Xvalue.append(worksheet.cell_value(i,1))
    Xvalue.append(worksheet.cell_value(i,2))
    Xtrain.append(Xvalue)
    Ytrain.append(worksheet.cell_value(i,0))

for i in range(7501,10001):
    Xvalue = []
    Xvalue.append(worksheet.cell_value(i,1))
    Xvalue.append(worksheet.cell_value(i,2))
    Xtest.append(Xvalue)
    Ytest.append(worksheet.cell_value(i,0))

print("Ensemble bagged trees Results: ")
baggingclf = BaggingClassifier(random_state=123).fit(Xtrain,Ytrain)
printRes(baggingclf,Xtest,Ytest)
print("Gradient booster algorithm Results:")
GradientBoostingclf = GradientBoostingClassifier(random_state=123).fit(Xtrain,Ytrain)
printRes(GradientBoostingclf,Xtest,Ytest)
print("Logistic Regression Results:")
LogisticRegressionclf = LogisticRegression(random_state=123).fit(Xtrain,Ytrain)
printRes(LogisticRegressionclf,Xtest,Ytest)
print("cubic SVM Results:")
SVMclf = SVC(kernel='poly',degree=3,random_state=123).fit(Xtrain,Ytrain)
printRes(SVMclf,Xtest,Ytest)

print("As per my analysis, Ensembled Bagged trees is having the highes modified f1 score . So, we")
print("should choose Ensemble bagged trees algorithm")


