
from matplotlib.pyplot import axis
import pandas as pd
import numpy as np 
import seaborn as sns
from sklearn.model_selection import train_test_split,GridSearchCV
from sklearn.neighbors import KNeighborsClassifier


ds = pd.read_csv('gender.csv',sep=',')
# print(ds.info())
# print(ds.head(20))

# sns.boxplot(x=ds['forehead_height_cm'])
# plt.show()


X = ds.drop(columns='Male',axis=1)
y = ds['Male']


x_train,x_test,y_train,ytest = train_test_split(X,y,test_size=0.25,random_state=50)




knn = KNeighborsClassifier()

k_values = dict(n_neighbors = [1,2,3,4,5,6])

base = np.array([10,11,13,15,14,13,15,18,])

gritSearch = GridSearchCV(knn,k_values,scoring='accuracy') 

gs = gritSearch.fit(x_train,y_train)

bestk = gs.best_params_

print('Acuracia  resultado para o valor de {} foi {}'.format(gs.best_params_,gs.best_score_))


#Aplicar o PCA
pca = PCA(n_components=5)
pca.fit(ds_normalized)
print(pca.explained_variance_ratio_)
percent = 0
for component in pca.explained_variance_raio_:
    percent += component

print("Total de cobertura dos dados na nossa base: {:.2f}%".format(percent*100))




