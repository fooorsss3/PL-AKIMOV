s = input("текс: ")
f = s.split()
a = []
ya = []
for i in f:
    if i.find("а") == 0 :
        a.append(i)
    if i.rfind("я") == len(f) -1:
        ya.append(i)
print(a)
print(ya)

