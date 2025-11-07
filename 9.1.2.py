def recursive(a, b):
    if a < b:
        return a
    else:
        return recursive(a-b, b)
a = int(input("число a: "))
b = int(input("число b: "))
if b <= 0:
    print("b должно быть натуральным числом (больше 0).")
else:
    res = recursive(a, b)
    print(res)
