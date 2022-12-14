# -*- coding: utf-8 -*-
"""Group_26_Assignment_3__Smart_Cities.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/12oihGiBuv0u2AZ3dU3N5V6yzZdeXmk-3

## Install libraires
"""

!pip install markupsafe==2.0.1
!pip install pycaret[full]

!pip uninstall Jinja2 --yes
!pip install Jinja2

"""## Importing the libraries"""

# Commented out IPython magic to ensure Python compatibility.
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.manifold import TSNE
from IPython.core.pylabtools import figsize
from pycaret.utils import enable_colab
enable_colab()
from pycaret.anomaly import *
from sklearn.cluster import DBSCAN
from tqdm import tqdm
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
# %matplotlib inline

"""## Importng the *dataset*"""

anomaly_detection = pd.read_csv('Dataset_to_be_used_in_anomaly_detection.csv')
anomaly_detection.head()

anomaly_detection.columns

anomaly_detection.drop('Unnamed: 0' ,axis =1, inplace=True)
anomaly_detection.head()

"""## Modeling"""

s = setup(anomaly_detection, session_id = 123)

models()

def models(model):
  ml_model = create_model(model,fraction=0.05)
  ml_model_results = assign_model(ml_model)
  anomalies = ml_model_results[ml_model_results['Anomaly'] == 1]
  results = ml_model_results.iloc[:,:-2]
  c = 1
  figsize(10,7)
  for column in results.columns:
    plt.subplot(2,2,c)
    plt.plot(ml_model_results[column])
    plt.scatter(anomalies.index,anomalies[column],c = 'r', marker ='o', s = 50)
    plt.title(" ".join(column.split('_')))
    c = c+1
  
  return anomalies, ml_model_results

"""1. SVM"""

anomalies_svm, svm_model_results = models('svm')

"""2. KNN"""

anomalies_KNN, knn_model_results = models('knn')

"""3. PCA"""

anomalies_PCA, pca_model_results = models('pca')

"""4. DBSCAN"""

model = DBSCAN(eps=0.5, min_samples=7)
predLabels = model.fit_predict(anomaly_detection)
predLabels

# replace -1 to 1 
Dbscan=np.where(predLabels==-1,1,predLabels)
Dbscan

"""##TSNE plot"""

def tsne(x,y):
    Tsne = TSNE(n_components = 2)
    tsne_results = Tsne.fit_transform(x)
    df = pd.DataFrame()
    df['feature 1'] = tsne_results[:,0]
    df['feature 2'] = tsne_results[:,1]
    df['y'] = y
    sns.scatterplot(x = 'feature 1', y = 'feature 2', hue = df.y.tolist(), data = df)

tsne(svm_model_results.iloc[:,:-2],svm_model_results.iloc[:,-2])

tsne(knn_model_results.iloc[:,:-2], knn_model_results.iloc[:,-2])

tsne(pca_model_results.iloc[:,:-2],pca_model_results.iloc[:,-2])

tsne(pca_model_results.iloc[:,:-2],Dbscan)

"""## Evaluation """

preformance = pd.read_csv('/content/Dataset_to_be_used_in_performance_comparison.csv')
preformance.head()

true_label = preformance.iloc[:,-1]
svm_label = svm_model_results.iloc[:,-2]
knn_label = knn_model_results.iloc[:,-2]
pca_label = pca_model_results.iloc[:,-2]

cr_svm = classification_report(true_label,svm_label)
print(cr_svm)

cr_knn = classification_report(true_label,knn_label)
print(cr_knn)

cr_pca = classification_report(true_label,pca_label)
print(cr_pca)

cr_DB= classification_report(true_label,Dbscan)
print(cr_DB)