'''
Date: 2021-03-01 02:51:29
LastEditTime: 2021-03-01 04:17:41
Author: Ye-P
Descripttion: svm test
'''
from sklearn import svm
import numpy as np
import pandas as pd
from sklearn import datasets
from sklearn.model_selection import cross_val_score, train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import scale
import matplotlib.pyplot as plt
iris = datasets.load_iris()
# print(iris)
print(iris.data[0:10])
print(iris.target[0:10])
data = scale(iris.data)
target = iris.target
# data = iris.data
X_train, X_test, y_train, y_test = train_test_split(
    data, target, test_size=0.3, shuffle=True)

x = []
y = []
for k in range(1, 10, 1):
    clf = KNeighborsClassifier(n_neighbors=k)
    scores = cross_val_score(clf, data, target, cv=5, scoring='accuracy')
    print(scores.mean())
    x.append(str(k))
    y.append(scores.mean())
    # print(scores['test_score'].mean())
plt.bar(x, y, color='green')
plt.show()
