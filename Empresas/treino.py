import pandas as pd
timestamp_atual = pd.Timestamp.now()
mes = timestamp_atual.strftime('%m-%Y')


data = [mes]

calcas = [1,2,3,4]
df = pd.DataFrame({'Dia' : [1, 2],
                    'Mes/ano': [data , data],
                   }






)

print("DataFrame original:")
print(df)

