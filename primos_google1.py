n = int(input("Digite o número inicial: "))
m = int(input("Digite o número final: "))
count = 0
for i in range(n,m+1):
    if i > 1:
        for j in range(2,i):
            if(i % j == 0):
                break
            else:
                print(i)
count = count + 1
print(f'primos: {count}')
