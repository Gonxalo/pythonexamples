import math
def distancia(x1,x2,y1,y2):
	cateto1 = (x2-x1)**2
	cateto2 = (y2-y1)**2
	raiz = math.sqrt(cateto1 + cateto2)
	return raiz

print "x2: "
x1 = int(raw_input())
print "x1"
x2 = int(raw_input())
print "y2: "
y1 = int(raw_input())
print "y1"
y2 = int(raw_input())

print distancia(x1,x2,y1,y2)