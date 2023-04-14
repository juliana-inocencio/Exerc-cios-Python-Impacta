a = float(input())
b = int(input())
c = a * b
d = (c*0.1) + ((0.01*c)*b)
print(f'{c:.2f}')
print(f'{c-d:.2f}')
