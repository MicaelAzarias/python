T = float(input("insira o valor da tensão: "))
C = float(input("insira o valor da corrente: "))

P = T * C

print(P)
pip install pandas 
import pandas as pd
dados={
    'tipos de carro': ['sedan', 'suv', 'hatchback', 'caminhonete', 'coupe'],
    'tipo de direção': ['hidraulica', 'eletrica', 'mecanica', 'eletrica', 'hidraulica'],
    'tipo de pneu': ['radial', 'diagonal', 'radial', 'diagonal', 'radial'],
    'faixa de preço': ['alto', 'media', 'baixo', 'alto', 'medio'],
    'potencia': [120,130,100,180,200],
    'velocidade de cruzeiro': [True, False, True, True, False]
}

df_carros = pd.DataFrame(dados)
df_carros
df_carros.head(5)
print('o valor minimo é:', df_carros['potencia'].min())
def filtro_por_valor(df_carros, coluna, valor): # primeiro vem o parametro, depois a coluna e depois o valor.
    return df_carros[df_carros[coluna] == valor]

filtro_por_valor(df_carros, 'tipos de carro', 'sedan')


carros_desejado = ['alice', 'david']

for nome in carros_desejado:
    dados = df_carros.loc[df_carros['tipos de carro'] == nome]
    print(f"dados para {nome}:\n{dados}\n")
