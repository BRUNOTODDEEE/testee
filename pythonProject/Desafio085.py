todos = []
imp = []
par = []

for i in range(0,7):
    numero = int(input('Digite seus 7 numeros : '))
    if numero %2 == 0:
        par.append(numero)
    else:
        imp.append(numero)


todos.append(par)
todos.append(imp)

if todos[0][1] %2 == 0:
    print(f'Os numero pares foram {sorted(todos[0])}')
    print(f'Os numeros impares foram{sorted(todos[1])}')





