def matrica(file):
    mat = []
    f = open(file, "r")
    for line in f:
        row = [int(x) for x in line.split()]
        mat.append(row)
    return mat
mat = matrica("vvod.txt")
zapisat = open("vivod.txt", "w")
for i in mat:
    i[i.index(max(i))], i[0] = i[0], i[i.index(max(i))]
    i[i.index(min(i))], i[-1] = i[-1], i[i.index(min(i))]
    zapisat.write(str(i) + "\n")
