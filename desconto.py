valor = float(input('Valor do item: '))
qtda = int(input('Quantidade: ' ))
total = valor * qtda
desconto = total*0.10
print(f'Total com desconto: {total-desconto:.2f}')
