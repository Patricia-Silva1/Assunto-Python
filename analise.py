import matplotlib.pyplot as plt
import numpy as np

import pandas as pd
from pandas.core.frame import DataFrame
import seaborn as sns
from scipy import stats

from pandas.core.algorithms import unique
from pandas.io.formats.format import return_docstring

#def categorize(price):
#    if price >= 500000.0:
#        return 'expensive'
#    elif price >= 220000.0:
#        return 'fair'
#    else:
#        return 'cheap'

dataset = pd.read_csv('kc_house_data.csv', sep=',', encoding='latin1')

#print(type(dataset))

#dataset['cat_price'] = dataset['price'].apply(categorize)
#print(dataset.info())
#print(dataset.head(10))
#print(dataset[dataset['price'] == 7700000.0])
#print(pd.value_counts(dataset['cat_price']))
#print("Qtd de quartos: ",dataset['bedrooms'].unique())
#print(dataset[dataset['bedrooms'] == 33])

bedrooms = dataset['bedrooms']
bedrooms.dropna(inplace=True)
values = np.array(bedrooms)
print(values.tolist())
sum = 0
#Verificar qd de campos nulos no dataset
print(dataset.isnull().sum())
for value in values:
    if value != 33.0:
        sum += value
media = sum/(len(values)-1)
print(media)

#Substituir campos nulos de quartos para a média de quaros do dataset
dataset['bedrooms'].fillna(media, inplace=True)
dataset.dropna(inplace=True)
print(dataset.isnull().sum())

# Aplicação do ZScore para eliminação outliers
# verificar a existênca de outliers
#sns.boxplot(x=dataset['bedrooms'])
#plt.show()

#Utilizar o Zsccore
bedrooms = pd.DataFrame(values)
bedrooms.columns = ['bedrooms']
z = np.abs(stats.zscore(bedrooms))
z_bedrooms = bedrooms[z<3.(axis=1)]
#sns.boxplot(x=z_bedrooms['bedrooms'])
#plt.show()

#Aplicar IQR
Q1 = bedrooms.quantile(0.25)
Q3 = bedrooms.quantile(0.75)
IQR = Q3 - Q1
q_highest_bedrooms = Q3 + 1.5 * IQR
q_lowest_bedrooms = Q1 - 1.5 * IQR
print('Maior: ', q_highest_bedrooms)
print('Menor: ', q_lowest_bedrooms)

IQR_bedrooms = bedrooms[~((bedrooms>q_highest_bedrooms)|(bedrooms<q_lowest_bedrooms)).any(axis = 1)]
sns.boxenplot(x = IQR_bedrooms['bedrooms'])
plt.show()