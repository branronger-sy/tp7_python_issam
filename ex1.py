import pandas as pd
df=pd.read_csv('covid.csv')
print("les premier lignes: ")
print(df.head())
print("Les derniere: ")
print(df.tail())
print("Les types de donnes: ")
print(df.dtypes)
#2
df['date_commande']=pd.to_datetime(df['date_commande'])
print(df.dtypes)
#3
agg_par_jour = covid.drop(['dep', 'sexe'], axis=1).groupby('jour').sum()
print(agg_par_jour.tail())
#4
agg_par_jour.plot(title="Evolution_des_hospitalisations_par_jour" )
#5
covid_sexe=covid[covid['sexe']=='M'].drop(['dep', 'sexe'], axis=1).groupby('jour').sum()
covid_sexe.plot(title="Evolution des hospitalisations par jour (pour un Masc)",logy=True)
plt.show()
#6
agg_diff=agg_par_jour.diff()
agg_diff.plot(title="Séries différenciées des hospitalisations",logy=True)
plt.show()
#7
agg_smooth=agg_par_jour.rolling(window=7).mean()
agg_smooth.plot(title="Séries lissées sur 7 jours des hospitalisations", logy=True)
plt.show()