a,b,c = input().split(' ')
a = int(a)
b = int(b)
c = int(c)
conta = (a+b+abs(a-b))/2
if conta > c:
    print(f'{conta:.0f} eh o maior')
elif conta < c:
    print(f'{c:.0f} eh o maior')

