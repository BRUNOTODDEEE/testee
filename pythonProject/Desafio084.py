completo = []
pessoas = []
count = 0
elemento = 0

while True:
    nome = str(input('Digite o seu nome: '))
    pessoas.append(nome)
    peso = int (input('Digite o seu peso: '))
    pessoas.append(peso)
    completo.append(pessoas[:])
    pessoas.clear()




    continuar = str(input('Deseja continuar(S/N): ')).strip().upper()
    if continuar == 'N':
        break




for i in (completo[:]):
    for v in (completo[0][i]):


    print(i)



    












