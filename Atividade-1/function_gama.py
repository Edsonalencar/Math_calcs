import math

# Caclcula factorial
def fatorial(x): 
  factorial = 1

  if x < 0:
    return None
  elif x == 0:
    return 1
  else:
    for i in range(1, x + 1):
      factorial = factorial*i
    return factorial

# Calcula o valor de gama
def calcGama(x):
  if int(x) == float(x):
    return fatorial(x-1)
  else:
    return math.gamma(x)


# Chama a função
print(calcGama(1/2))
