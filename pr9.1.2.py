def find_max():
    num = int(input())
    if num == 0:
        return 1
    else:
        maxvspis = find_max()
        return max(num, maxvspis)
max = find_max()
print(max)