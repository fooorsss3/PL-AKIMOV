n=3
a=[]
t = [0, 0]
for i in range(n):
    b=[]
    for j in range(n):
        print('введите [', i, ',', j, '] элемент')
        b.append(int(input()))
    a.append(b)
print('исходная матрица')
for i in range(n):
    for j in range(n):
        print(a[i][j],end=' ')
    print()
max_chislo = a[0][0]
for i in range(n):
    for j in range(n):
        if abs(a[i][j]) > abs(max_chislo):
            max_chislo = a[i][j]
            t = [i, j]
print(max_chislo)
a.pop(t[0])
for i in a:
    i.pop(t[1])
for i in a:
    print(i)

