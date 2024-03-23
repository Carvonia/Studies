import pandas as pd

notas_df = pd.read_csv("D:\\Programming\\Studies\\Python\\Uni\\Pandas\\notas.csv", delimiter=';')
nr = pd.DataFrame({'matricula':'blank', 'nomecompleto':'blank', 'codigocurso':'blank', 'curso':'blank','aoub':'blank', 'n1':'blank', 'n2':'blank', 'n3':'blank', 'n4':'blank', 'n5':'blank', 'n6':'blank', 'n7':'blank', 'n8':'blank', 'n9':'blank'}, index=[0])
notas_df = pd.concat([nr,notas_df.loc[:]]).reset_index(drop=True)
notas_df.columns = ['matricula', 'nomecompleto', 'codigocurso', 'curso', 'aoub', 'n1', 'n2', 'n3', 'n4', 'n5', 'n6', 'n7', 'n8', 'n9']

print(notas_df)

# Check if '201' is in the cleaned column names (case-insensitive)
if 'matricula' not in notas_df.columns:
    raise ValueError("The column '201' is not present in the DataFrame.")

# Check if 'codigocurso' is in the cleaned column names (case-insensitive)
if 'codigocurso' not in notas_df.columns:
    raise ValueError("The column 'CodigoCurso' is not present in the DataFrame.")

if 'DS' not in notas_df.columns:
    raise ValueError("The column 'DS' is not present in the DataFrame.")

pesos_df = pd.read_csv("D:\\Programming\\Studies\\Python\\Uni\\Pandas\\pesos.csv", delimiter=';')
pesos_df.set_index('CodigoCurso', inplace=True)

def calcular_nota_final_ponderada(row):
    # Check if 'codigocurso' is in the row index
    if 'codigocurso' not in row.index:
        raise ValueError("The column 'CodigoCurso' is not present in the DataFrame.")
    
    notas_cursadas = row.replace('N', pd.NA).astype(float)
    
    # Check if 'codigocurso' exists in pesos_df before accessing it
    codigo_curso = row['codigocurso']
    if codigo_curso not in pesos_df.index:
        raise ValueError(f"Course '{codigo_curso}' not found in 'pesos_df'.")
    
    pesos_cursadas = pesos_df.loc[codigo_curso].astype(float)

    nota_final = (notas_cursadas * pesos_cursadas).sum() / pesos_cursadas.sum()
    pontuacao = pesos_cursadas.sum()

    return pd.Series({'NotaFinal': round(nota_final, 3), 'Pontuacao': pontuacao})

resultados_df = notas_df.apply(calcular_nota_final_ponderada, axis=1)
notas_df.columns = notas_df.columns.str.strip().str.lower()
notas_df[['notafinal', 'pontuacao']] = resultados_df

for curso in notas_df['codigocurso'].unique():
    curso_df = notas_df[notas_df['codigocurso'] == curso]
    curso_df.sort_values(by='nomecompleto', inplace=True)
    resultado_df = curso_df[['nomecompleto', 'matricula', 'notafinal', 'pontuacao']]
    resultado_df.to_csv(f'{curso}_resultado.csv', sep=';', index=False)

print(notas_df)
