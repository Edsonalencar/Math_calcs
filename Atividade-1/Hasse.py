R = []
x = {2, 3, 4, 5, 8, 12, 24, 25}
for m in x:
    for n in x:
        if (m != n) and (m % n == 0):
            R += [(n, m)]

print(R)
