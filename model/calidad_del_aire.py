# -*- coding: utf-8 -*-


import json

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import requests
import seaborn as sb
import sklearn.metrics as metrics
from sklearn import linear_model, model_selection
from sklearn.metrics import accuracy_score, classification_report, f1_score
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import StandardScaler

""" url = "http://ha.jdrkairquality.com:1880/endpoint/getenviroments"
r = requests.get(url)
data = r
for d in data:
    print(d)
    print("-----------------------------------------------------------") """

"""Importación de archivos de Drive"""

"""Variable que contiene en string la ruta de la carpeta que contiene la data"""

BASE_FOLDER = "model/"

"""Importación en un dataframe la data y mostrar primeras filas del dataframe"""

dataframe = pd.read_excel(BASE_FOLDER + "dataset_air_quality.xlsx")
# dataframe = pd.read_json(data.text)
dataframe.head()

dataframe.dtypes

y = dataframe['Estado']
X = dataframe[['A', 'B', 'C', 'D', 'E']]
dataframe = dataframe.replace(np.nan, "0")
X.dtypes

"""Separación de train y test por medio de sklearn - Escalado de variables"""


X_train, X_test, y_train, y_test = train_test_split(X, y)
scaler = StandardScaler()
scaler.fit(X_train)
X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)
"""Entrenar el modelo y muestra de valores segun su clasificación"""
mlp = MLPClassifier(hidden_layer_sizes=(6, 6, 6, 6),
                    solver='lbfgs', max_iter=6000)
mlp.fit(X_train, y_train)
predictions = mlp.predict(X_test)
print(classification_report(y_test, predictions))

def prediction_asd(data):
    # x_new = pd.DataFrame(  {'A':[9.5], 'B':[0.101], 'C':[0.076],'D':[100], 'E':[35.5]} )
    #x_new = pd.DataFrame({'A': [1.773], 'B': [0.02617], 'C': [0.00342], 'D': [109.9], 'E': [25.626]})
    print(data)
    resultado = mlp.predict(data)
    print(resultado[0])


