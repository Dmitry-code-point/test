def sravnenie(a):
    b = []
    for i in a:
        if i > 10:
            b.append(float(i) / 10)
        else:
            b.append(i)
    return b
a = [56, 9, 11, 2]
n = (sorted(sravnenie(a), reverse=True))
print(n)