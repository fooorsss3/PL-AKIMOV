s = []
for i in range(10):
    f = int(input(f"число {i + 1}: "))
    s.append(f)
a = sum(s)
k = a/10
print(k)
for i in range(len(s)):
    if s[i]> k:
        s[i] = 1
print(s)

