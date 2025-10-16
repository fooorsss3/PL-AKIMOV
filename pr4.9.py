N = int(input("колличество чисел из ряда Фибонначи: "))
R = 0
R2 = 1
summm_fibonnachi = 0
for i in range(N):
    summm_fibonnachi += R
    R = R2
    R2 = R+R2
    print(summm_fibonnachi)




