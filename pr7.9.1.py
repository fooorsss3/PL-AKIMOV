n = int(input("число: "))
def kollvoshagov(n):
    shag = 0
    while n !=0:
        sumcifr = 0
        for cifri in str(n):
            sumcifr = sumcifr + int(cifri)
        n = n - sumcifr
        shag = shag+1
    return shag
print(kollvoshagov(n))


