a,b= input().split(' ')
a = int(a)
b = int(b)
conta = b % a
if a < b and conta == 0:
    print('Sao Multiplos')
else:
    print('Nao sao Multiplos')