n = 4
def f(n): return n < 1 or (-1)**n+n*f(n-1)


print(f(n))
