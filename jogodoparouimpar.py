num = int(input(''))
conta = num % 2
if conta == 0:
    print(f'{num-1} {num+2}')
else:
    print(f'{num-2} {num+1}')