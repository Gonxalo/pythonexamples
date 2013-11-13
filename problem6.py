#problema 6, lista comunes
def comun(lista1, lista2):
	lista=[]
	for i in lista1:
		for j in lista2:
			if i == j:
				lista.append(i)
				break
	return lista

lista1 = [1,2,5,8,9,21]
lista2=[15,4,20,34,60]
lista = comun(lista1, lista2) 
if len(lista) > 0:
	print(lista)
else:
	print("No hay comunes")