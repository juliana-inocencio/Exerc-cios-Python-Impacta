p = int(input('p: '))
q = int(input('q: '))
contador = 0
while p >= q:
    p = p - q
    contador = contador + 1
print(f'o quociente da divisão é {contador}')