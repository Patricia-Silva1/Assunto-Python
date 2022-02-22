from os import sep
import pandas as pd
import numpy as np
# from numpy.random.mtrand import permutation, random
import math
from sklearn.neighbors import KNeighborsRegressor

ds = pd.read_csv('nba_2013.csv', sep = ',')
# print(ds.columns.values)
#print(ds.head())
#print(ds.info())
#print(ds.isnull().sum())
ds['x3p.'].fillna(0, inplace=True)
ds['ft.'].fillna(0, inplace=True)
ds['x2p.'].fillna(0, inplace=True)
ds['efg.'].fillna(0, inplace=True)
ds['fg.'].fillna(0, inplace=True)
ds.drop(['season_end'],axis=1,inplace=True)
#print(ds.isnull().sum())

ds_normalized = ds.select_dtypes('number')
ds_normalized = ds_normalized - ds_normalized.mean()/ds_normalized.std()
# print(ds_normalized.head())


#Separar base de teste x treino

#Embaralhar índices para não pegar dados de sequências
random_index = np.random.permutation(ds_normalized.index)
#Calcular qtd de dados de teste
q_test = math.floor(len(ds_normalized) / 4)

#Separar a base de teste
test = ds_normalized.loc[random_index[1:q_test]]

#Separar base de treino
train = ds_normalized.loc[random_index[q_test]]

#Separar o dado da predição

#Separar colunas que irão ajudar a definir o target
# definir x
ds_temp = ds_normalized.drop(columns=['pts'],axis=1)
x_columns = ds_temp.columns
print(x_columns)

# definir y
y_column = ['pts']

knn = KNeighborsRegressor(n_neighbors=3)

knn.fit(train[x_columns], train[y_column])

predictions = knn.predict(test[x_columns])

#TODO
#Calcular erro médio das predições





