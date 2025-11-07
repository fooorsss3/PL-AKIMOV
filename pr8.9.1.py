n=3
a=[]
for i in range(n):
    b=[]
    for j in range(n):
        print('введите [',i,',',j,'] элемент')
        b.append(int(input()))
    a.append(b)
print('исходная матрица')
for i in range(n):
    for j in range(n):
        print(a[i][j],end=' ')
    print()
k = 3
kratk = []
maxel = []
for i in range(n):
    for j in range(n):
        if a[i][j] % k == 0:
            kratk.append(a[i][j])
        if kratk:
            maxel = max(kratk)
l = len(kratk)
print(l,maxel)








