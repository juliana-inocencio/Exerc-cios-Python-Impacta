soma = 0
qtd = 0
n = int(input('Número: '))
while n != -1:
    soma = soma + n
    qtd = qtd + 1
    n = int(input('Número: '))
print(f'Média {soma/qtd}')