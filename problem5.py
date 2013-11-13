#problema 5, reverse

def reversa(cadena):
	inverso = ""
	max = len(cadena) -1	
	while max>=0:
		#print(cadena[max])		
		inverso += cadena[max]
		max-=1
	return inverso

palabra = "radar"	
palindromo = reversa(palabra)
if palabra == palindromo:
	print("Es palindromo")
else:
	print("No es palindromo")