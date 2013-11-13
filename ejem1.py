#ejem 1 

import math
input("NUmero :" )
print("a=", end="")
a = int(input())
print("b=", end="")
b = int(input())
print("c=", end="")
c = int(input())
result = 0

raiz = (pow(b,2)) - (4*a*c)
if raiz < 0:
	raiz = raiz * (-1)	
raiz = ((-b) + math.sqrt(raiz) ) / 2*a

print("Resultado: ", raiz)
	


