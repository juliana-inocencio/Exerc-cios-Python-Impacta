soma = 0
doacao = float(input(''))
while doacao != -1:
    soma = soma + doacao
    doacao = float(input(''))
print(f'VC$ {soma:.2f}')
print(f'R$ {soma*2.50:.2f}')
