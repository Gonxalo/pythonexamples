#problema 1 calcula numero mayor de una lista

def max(lista):
	a = lista[0]	
	if len(lista)>0:
		for i in lista:	
			#print("a:", a, "i:",i)
			if a < i:
				a = i
	print(a)

max([1,20,4,10,9,6])