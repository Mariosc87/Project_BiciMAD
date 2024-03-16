import argparse
import pandas as pd


parser = argparse.ArgumentParser(description='Bici Mad mas cercano a cada Centro Deportivo')

# definir argumentos de entrada, que luego voy a escribir en la terminal
parser.add_argument('-c', '--centros', type=str, help='Centros deportivos de Madrid. Si escribes centros te aparecen todos los centros de madrid')
#parser.add_argument('-i', '--info', type=str, help='si escribes "centros" aparece el listado de centros deportivos de Madrid. ')


# inicio el parser
parse_args = parser.parse_args()

centros = parse_args.centros

df = pd.read_csv('data/centroxbicimad.csv')

df2 = df[df['titulo']==centros]
    
if centros.lower() == 'centros':
    print(df)

else:
    for indice, row in df2.iterrows():
        print(f'Hola, el centro deportivo {row['titulo']}, tiene como estacion bicimad mas cercana {row['name']} {row['address']} y esta a {row['metros_distancia']} metros')


