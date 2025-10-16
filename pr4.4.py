# N = int(input("количество чисел: "))
# summa = 0
# for i in range(N):
#     a = int(input("прибовляем каждое число к сумме: "))
#     summa = summa + a
# print(summa)
N = int(input("количество чисел: "))
summa = 0
for i in range(N):
    summa = summa + int(input("добовляем каждое число к сумме"))
print(summa)
