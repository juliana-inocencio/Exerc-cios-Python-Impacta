def pede_idade (mensagem):
    idade = int(input(mensagem))
    return idade

idade = pede_idade('Digite sua idade: ')
if idade > 18:
    print('você tem mais de 18 anos')
else:
    print('você tem menos de 18 anos')
print('fim')