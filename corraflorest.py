corra = int(input(''))
soma = 0
contadora = 0

while corra > 0:
    soma = soma + corra
    contadora = contadora + 1
    corra = int(input(''))

media = soma/contadora

print(f'soma: {soma}')
print(f'contadora: {contadora}')
print(f'MEDIA: {media:.2f}')




