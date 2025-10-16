a = [5,3,7,9,1]
max = a.index(max(a))
min = a.index(min(a))
a[max],a[min] = a[min],a[max]
print(a)