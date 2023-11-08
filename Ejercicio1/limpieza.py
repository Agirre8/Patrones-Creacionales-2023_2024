import pandas as pd

data = pd.read_csv('Ejercicio1/activaciones_samur_2022.csv', delimiter = ";")

print(data.info()) 
print(data.describe())  
print(data.head()) 

#elimino los valores nulos para que no me de error al procesar lso datos
data = data.dropna()

#compruebo que no hay valores nulos en el dataset
nulos = data.isna().sum()
print(nulos)
print(data.columns)
meses_a_numeros = {
    'ENERO': 1,
    'FEBRERO': 2,
    'MARZO': 3,
    'ABRIL': 4,
    'MAYO': 5,
    'JUNIO': 6,
    'JULIO': 7,
    'AGOSTO': 8,
    'SEPTIEMBRE': 9,
    'OCTUBRE': 10,
    'NOVIEMBRE': 11,
    'DICIEMBRE': 12
}

data['Mes'] = data['Mes'].map(meses_a_numeros)

data['Hora Solicitud'] = pd.to_datetime(data['Hora Solicitud'], format='%H:%M:%S')
data['Hora Solicitud'] = (data['Hora Solicitud'].dt.hour * 60 + data['Hora Solicitud'].dt.minute + data['Hora Solicitud'].dt.second / 60).round().astype('int64')

data['Hora Intervención'] = pd.to_datetime(data['Hora Intervención'], format='%H:%M:%S')
data['Hora Intervención'] = (data['Hora Intervención'].dt.hour * 60 + data['Hora Intervención'].dt.minute + data['Hora Intervención'].dt.second / 60).round().astype('int64')

data.drop('Año', axis=1, inplace=True)

data_limpio = data.copy()

tipos_de_datos = data.dtypes
print(tipos_de_datos)
data_limpio.to_csv('Ejercicio1/dataset_limpio.csv', index=False)
