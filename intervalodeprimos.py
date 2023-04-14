n1 = int(input(''))
n2 = int(input(''))
divisor = 1
contador = 0

for x in range(n1,n2+1):
    if x % divisor == 0:
        break
    divisor = divisor + 1
    print(x)




