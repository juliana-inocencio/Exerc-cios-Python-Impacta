n1 = int(input(''))
n2 = int(input(''))
contador = 0
for i in range(n1, n2 + 1):
    if i > 1:
        for j in range(2, i):
            if (i % j == 0):
                break
        else:
            print(i)
            contador += 1
print(f'primos: {contador}')