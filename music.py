
from math import dist
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans


#Lendo ds de músicas do spotify
ds = pd.read_csv('genres_V2.csv',sep=',')
print(ds.head(30))
print(ds.info())
ds.drop(columns='Unnamed: 0', axis=1, inplace=True)
ds.drop(columns='title', axis=1, inplace=True)
#Normalizando o ds para aplicar PCA
ds_normalized = ds.select_dtypes('number')
print(len(ds_normalized.columns))
ds_normalized = (ds_normalized - ds_normalized.mean())/ds_normalized.std()



#Visualizar/nalisar os resultados a aplicação do PCA
#pca = PCA(n_components=5)
#pca.fit(ds_normalized)
#print(pca.explained_variance_ratio_)
#percent = 0
#for component in pca.explained_variance_raio_:
#percent += component

#print("Total de cobertura dos dados na nossa base: {:.2f}%".format(percent*100)

#Aplicar o PCA depois da análise realizada
pca = PCA(n_components=8).fit_transform(ds_normalized)

#Roda o algoritimo l-means em cima da ase de dados com o PCA
kmeans = KMeans(n_clusters=4)
kmeans.fit(pca)
print(kmeans.labels_)

#Pegar os valores dos labels e colocar como uma nova coluna dentro do ds original
ds['cluster'] = kmeans.labels_
print(ds.head())

#Visualizar clusters distintos

print(len(ds[ds['cluster']==0]))
print(pd.value_counts(ds['cluster']))