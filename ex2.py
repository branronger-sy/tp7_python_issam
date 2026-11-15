import pandas as pd
import numpy as np
df=pd.read_csv('temperature.csv')
print(df.describe())
df_filtre=df[
    (df['mois'].isin([3,6,9,12]))& 
    (df['region']!='East')
]
print(df_filtre.head())
data_np = df_filtre.to_numpy()
moyennes_mensuelles = df_filtre.groupby('mois')['temperature'].mean()
print("Moyennes par mois :\n", moyennes_mensuelles)
df_pivote = df_filtre.pivot(index='ville', columns='mois', values='temperature')
matrice_corr = df_pivote.corr()
print("\nMatrice de corrélation entre les 4 mois :\n", matrice_corr)