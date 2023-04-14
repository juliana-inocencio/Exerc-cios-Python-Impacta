a = int(input())
b = int(input())
if a > b:
    print('Nenhuma tabuada no intervalo!')
elif a < b:
    for c in range(1,10+1):
        print(f'{a} x {c} = {a * c}')
    print('----------')
    for c in range(1,10+1):
        print(f'{b} x {c} = {b * c}')
    print('----------')
elif a == b:
    for c in range(1,10+1):
        print(f'{a} x {c} = {a * c}')
    print('----------')

