i = 1 #inicio do intervalo
n = 100 #final do intervalo
p = 1 #Produtório dos fatores primos menos 1, (pi - 1)
m = 1 #Produtório dos fatores primos

for num in range(i, n + 1):
   if num > 1:
       for j in range(2, num):
           if (num % j) == 0:
               break
       else:
           p *= (num-1)
           m *= num

P = (n/m) * p #Fórmula final: P(n) = (n/m)*(p1 - 1)*(p2 - 1)...(pk - 1)

print(P)