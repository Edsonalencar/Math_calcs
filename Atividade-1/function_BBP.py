def casasPi(num):
    pi = 0
    for k in range(int(num)):
        pi += 1/pow(16, k) * (4/(8*k+1) - 2/(8*k+4) - 1/(8*k+5) - 1/(8*k+6))
    return pi


print(casasPi(1000))
