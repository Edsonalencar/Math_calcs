n=4
f=lambda  n: n<1 or(-1)**n+n*f(n-1)
print(f(n))