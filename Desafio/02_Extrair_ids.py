
# EXTRAIR LISTA DE IDS
import pandas as pd 

df = pd.read_csv('ids_funcionarios.csv')
func_ids = df['ID'].tolist()
print(func_ids)
