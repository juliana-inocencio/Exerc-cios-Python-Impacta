a,b,c,d = input().split(' ')
a = int(a)
b = int(b)
c = int(c)
d = int(d)
conta = a % 2
conta2 = c+d
conta3 = a+b
if b > c and d > a and conta2 > conta3 and conta == 0:
    print('Valores aceitos')
else:
    print('Valores nao aceitos')