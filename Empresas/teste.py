import pandas as pd


timestamp_atual = pd.Timestamp.now()
mes = timestamp_atual.strftime('%m-%Y')



posto = ['Semilia','Sguaicurus','Smatriz','Suniao','terere','morenao']



##Postos

semilia_calcas = []
semilia_camisas = []

guaicurus_camisa = []
guaicurus_calca = []

smatriz_calca = []
smatriz_camisa = []

suniao_calca = []
suniao_camisa = []


terere_calca = []
terere_camisa = []

morenao_calca = []
morenao_camisa = []

##################### dia
dia_emilia = []
data_emilia = []

dia_guaicurus = []
data_guaicurus = []

dia_smatriz = []
data_smatriz = []

dia_suniao = []
data_suniao = []

dia_terere = []
data_terere = []

dia_morenao = []
data_morenao = []


for i in range(0,6):
    print(f'Posto:{posto[i]}')
    if i != 6:
        while True:

###################### dia
            if i == 0:
                dia = int(input('Dia:'))
                dia_emilia.append(dia)
                data_emilia.append(mes)
            elif i == 1:
                dia = int(input('Dia:'))
                dia_guaicurus.append(dia)
                data_guaicurus.append(mes)
            elif i == 2:
                dia = int(input('Dia:'))
                dia_smatriz.append(dia)
                data_smatriz.append(mes)
            elif i == 3:
                dia = int(input('Dia:'))
                dia_suniao.append(dia)
                data_suniao.append(mes)
            elif i == 4:
                dia = int(input('Dia:'))
                dia_terere.append(dia)
                data_terere.append(mes)
            elif i == 5:
                dia = int(input('Dia:'))
                dia_morenao.append(dia)
                data_morenao.append(mes)




##################### Postos

            if i == 0:
                calca = int(input('Calcas: '))
                semilia_calcas.append(calca)
                camisa = int(input('Camisas: '))
                semilia_camisas.append(camisa)

            elif i == 1:
                calca = int(input('Calcas: '))
                guaicurus_calca.append(calca)

                camisa = int(input('Camisas: '))
                guaicurus_camisa.append(camisa)

            elif i == 2:
                calca = int(input('Calcas: '))
                smatriz_calca.append(calca)

                camisa = int(input('Camisas: '))
                smatriz_camisa.append(camisa)

            elif i == 3:
                calca = int(input('Calcas: '))
                suniao_calca.append(calca)

                camisa = int(input('Camisas: '))
                suniao_camisa.append(camisa)

            elif i == 4:
                calca = int(input('Calcas: '))
                terere_calca.append(calca)

                camisa = int(input('Camisas: '))
                terere_camisa.append(camisa)

            elif i == 5:
                calca = int(input('Calcas: '))
                morenao_calca.append(calca)

                camisa = int(input('Camisas: '))
                morenao_camisa.append(camisa)



            continuar = str(input('Continuar?(S/N) : ')).strip().upper()
            if continuar == 'N':

                break
    else:
        break



emilia = ({
                    'Dia': dia_emilia,
                    'Mes/ano': data_emilia,
                    'Calca': semilia_calcas,
                    'Camisa':semilia_camisas

                    }

)


guaicurus = ({
                    'Dia': dia_guaicurus,
                    'Mes/ano': data_guaicurus,
                    'Calca': guaicurus_calca,
                    'Camisa':guaicurus_camisa

                    }

)




smatriz = ({
                    'Dia': dia_smatriz,
                    'Mes/ano': data_smatriz,
                    'Calca': smatriz_calca,
                    'Camisa':smatriz_camisa

                    }

)

suniao  = ({
                    'Dia': dia_suniao,
                    'Mes/ano': data_suniao,
                    'Calca': suniao_calca,
                    'Camisa':suniao_camisa

                    }

)

terere  = ({
                    'Dia': dia_terere,
                    'Mes/ano': data_terere,
                    'Calca': terere_calca,
                    'Camisa':terere_camisa

                    }

)

morenao  = ({
                    'Dia': dia_morenao,
                    'Mes/ano': data_morenao,
                    'Calca': morenao_calca,
                    'Camisa':morenao_camisa

                    }

)




tabela1 = pd.DataFrame(emilia)
tabela2 = pd.DataFrame(guaicurus)
tabela3 = pd.DataFrame(smatriz)
tabela4 = pd.DataFrame(suniao)
tabela5 = pd.DataFrame(terere)
tabela6 = pd.DataFrame(morenao)


print(tabela1)
print('********'*30)
print(tabela2)
print('********'*30)
print(tabela3)
print('********'*30)
print(tabela4)
print('********'*30)
print(tabela5)
print('********'*30)
print(tabela6)





