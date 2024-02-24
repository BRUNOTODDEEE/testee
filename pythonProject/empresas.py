morenao = []
lcamisas = []
lcalcas = []



print('Morenao')
print('='*30)

while True:
    camisas = int(input('Camisas : '))
    lcamisas.append(camisas)

    continuar = str(input('Deseja continuar(S/N)?')).strip().upper()
    if continuar == 'N':
        break

print('*=*'*100)


while True:
    calcas = int(input('Calcas : '))
    lcalcas.append(calcas)

    continuar = str(input('Deseja Continuar(S/N)?:')).strip().upper()
    if continuar == 'N':
        break



morenao.append(lcamisas[:])
morenao.append(lcalcas[:])

print(f'Quantidade de camisas: {lcamisas}  Total de camisas : {sum(lcamisas)}')
print(f'Quantidade de calcas: {lcalcas}  Total de calcas : {sum(lcalcas)}')






#Santa*
'''Semilia = []
Sguaicurus = []
Smatriz = []
Suniao = []'''
#############
'''morenao = []
terere = []
raizen = []
semlimite = []
mediterranio = []
piblopes'''

