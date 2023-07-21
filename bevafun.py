import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_squared_error, accuracy_score
import seaborn as sns
from sklearn import preprocessing
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans

def pca_prep_plot(mat_day):
    '''
    INPUT:
     
     mat_day - the matrix of the dataset imported from the CSV
     
     This function will take a matrix with labels and will perform PCA and display the variance it will also return the dataframe'''
    mat_X= mat_day[:,:-1]
    mat_Y=mat_day[:,-1]
    min_max_scaler = preprocessing.StandardScaler()
    day1np_norm = min_max_scaler.fit_transform(mat_day)
    day1_df= pd.DataFrame(day1np_norm)

   

    
    #Using PCA reduce to 2-3 important features 
    pca = PCA(n_components=3)
    day1_pca = pca.fit_transform(day1_df)

    
    pc_df = pd.DataFrame(data = day1_pca , 
    columns = ['PC1', 'PC2','PC3'])
    pc_df['Cluster'] = mat_Y
    pc_df.head()
  
    day1_PC1=day1_pca[:,0]
    day1_PC2=day1_pca[:,1]
    day1_PC3=day1_pca[:,2]
    
    pca.explained_variance_
    df_var = pd.DataFrame({'% Variance':pca.explained_variance_,
             'Principal Components':['PC1','PC2','PC3']})
    ax = sns.barplot(x='Principal Components',y="% Variance", 
                     data=df_var, color="c");
    
    return pc_df