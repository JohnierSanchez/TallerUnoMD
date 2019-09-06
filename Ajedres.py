# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal.
"""
#Llamamos a la libreria "pandas", Esta es la librería más popular para análisis de datos y financieros.
import pandas as pd 
#Llamamos a la libreria "seaborn",la cual nos permite realizar visualizaciones graficas. 
import seaborn as sns
#Llamamos a la libreria "statistics", La cual agrupa un conjunto de funciones para el calculo estadítico. 
import statistics as stats
#Leemos el Dataset que contiene la informacion, la cual esta separada por comas.
df=pd.read_csv('games.csv')
#Realizamos una grafica de distribucion de probabilidades,ax hace referencia a los ejes,realizamos una grafica con ayuda de seaborn.
ax=sns.distplot(df['turns'])
#Llamamos e imprimimos la funcion mean(), la cual nos devuelve la media aritmética.  
print(stats.mean(df['turns']))
#Leemos el estado de la victoria, el cual sea igual a "Jaque mate" y sumamos el total de numero de turnos.
print(df.loc[df['victory_status']=='mate']['turns'].sum())
#print(df.loc[df['victory_status']=='mate'&(df['rated']=='TRUE')])
