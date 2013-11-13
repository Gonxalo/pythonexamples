#problem 3 true si es vocal

def EsVocal(vocal):
	if vocal == "a" or vocal == "e" or vocal == "i" or vocal == "o" or vocal == "u":
		return True
	else:
		return False
	
if EsVocal("a"):
	print("Vocal")
else:
	print("Consonante")