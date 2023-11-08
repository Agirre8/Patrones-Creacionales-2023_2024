import pandas as pd

URL = "https://datos.madrid.es/egob/catalogo/212504-0-emergencias-activaciones.csv"

# Leer CSV desde la URL
data = pd.read_csv(URL, sep=';', encoding='ISO-8859-1')

print(data.info()) 
print(data.describe())  
print(data.head()) 

#elimino los valores nulos para que no me de error al procesar lso datos
data = data.dropna()

#compruebo que no hay valores nulos en el dataset
nulos = data.isna().sum()
print(nulos)
