inicio = int(input(''))
fim = int(input(''))
contador = 0
for c in range(inicio, fim+1):
    if c % 4 ==0 and c % 100 != 0 or c % 400 == 0:
        contador = contador + 1
        print(c)
print(f'bissextos: {contador}')