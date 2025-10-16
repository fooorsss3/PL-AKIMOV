s =[]
n = int(input("количество элементов массива: "))
for i in range(n):
    k = int(input(f"элемент: {i+1}: "))
    s.append(k)
print(min(s))
print(s[::-1])


