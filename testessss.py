a = int(input())
b = int(input())
if a > b:
    print('Nenhuma tabuada no intervalo!')
for c in range(a,b+1):
    for d in range(1,10+1):
        print(f'{c} x {d} = {c * d}')
    print('----------')
