todos = []
linha1 = []
linha2 = []
linha3 = []

for i in range(0, 3):
    numero = int(input(f'Digite um valor para {0,i} : '))
    linha1.append(numero)
    if len(linha1[:]) == 3:
        for x in range(0,3):
            numero = int(input(f'Digite um valor para {1,x} : '))
            linha2.append(numero)
            if len(linha2[:]) == 3:
                for z in range(0,3):
                    numero = int(input(f'Digite um valor para {2,z} : '))
                    linha3.append(numero)
                    if len(linha3) == 3:
                        todos.append(linha1)
                        todos.append(linha2)
                        todos.append(linha3)
                        print('=-=' * 30)
                        for j in range(0,3):

                            print(f'[{todos[j][0]}]', end = '')

                            print(f'[{todos[j][1]}]',end = '')

                            print(f'[{todos[j][2]}]')





