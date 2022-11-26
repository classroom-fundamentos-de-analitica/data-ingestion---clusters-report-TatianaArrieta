"""
Ingestión de datos - Reporte de clusteres
-----------------------------------------------------------------------------------------

Construya un dataframe de Pandas a partir del archivo 'clusters_report.txt', teniendo en
cuenta que los nombres de las columnas deben ser en minusculas, reemplazando los espacios
por guiones bajos; y que las palabras clave deben estar separadas por coma y con un solo 
espacio entre palabra y palabra.


"""
import pandas as pd
import re


def ingest_data():

    contador = 0
    dictionary = {}
    dataframe = pd.DataFrame()

    with open('clusters_report.txt') as clustersreport:
        rows = clustersreport.readlines()
    rows = rows[4:]
    clusters = []
    cluster = [0, 0, 0, '']
    lastCluster = 1
    lastPClave = 105
    lastPorcentaje = "15,9 %"
    for i, _ in df.iterrows():
        if df.iloc[i,0] != lastCluster and not pd.isna(df.iloc[i,0]):
            lastCluster = df.iloc[i,0]
            lastPClave = df.iloc[i,1]
            lastPorcentaje = df.iloc[i,2]
        else:
            df.iloc[i,0] = lastCluster
            df.iloc[i,1] = lastPClave
            df.iloc[i,2] = lastPorcentaje

        for line in clustersreport:
            line = re.sub(r"\s+", " ", line)
            if len(line)>1 and contador > 3:
                if line.split()[0].isnumeric() == True:
                    try: 
                        dictionary['principales_palabras_clave'] = ' '.join(dictionary['principales_palabras_clave'])
                        df = df.append(dictionary, ignore_index=True)
                    except: pass
                    dictionary = {'cluster': int(line.split()[0]),
                                'cantidad_de_palabras_clave': int(line.split()[1]),
                                'porcentaje_de_palabras_clave': float(line.split()[2].replace(',','.')),
                                'principales_palabras_clave': line.split()[4:]}
                else: 
                    dictionary['principales_palabras_clave'].append(' '.join(line.split()))
                    
            contador += 1
            
    dictionary['principales_palabras_clave'] = ' '.join(dictionary['principales_palabras_clave'])
    df = df.append(dictionary, ignore_index=True)
    df['principales_palabras_clave'] = df['principales_palabras_clave'].str.rstrip('\.')
    

    return df
