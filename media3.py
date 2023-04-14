a,b,c,d = input().split(' ')
a = float(a)
b = float(b)
c = float(c)
d = float(d)
media = (a+b+c+d)/4
print(f'Media: {media:.1f}')
if media <5:
    print('Aluno reprovado.')
elif media >5 and 6.9:
    print('Aluno em exame.')
else:
    print('Aluno reprovado.')
