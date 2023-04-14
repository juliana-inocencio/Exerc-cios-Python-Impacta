a,b = input().split(' ')
a = int(a)
b = int(b)
if a == 1:
    print(f'Total: R$ {b*4.00:.2f}')
elif a == 2:
    print(f'Total: R$ {b*4.50:.2f}')
elif a == 3:
    print(f'Total: R$ {b*5.00:.2f}')
elif a == 4:
    print(f'Total: R$ {b*2.00:.2f}')
elif a == 5:
    print(f'Total: R$ {b*1.50:.2f}')


