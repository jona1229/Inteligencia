import json
with open('labase.json') as file:
	data = json.load(file)
revisados =[]
camino=[]
auxiliar = []
Nodsig=[]
#------------------------------------------------
def primeroAnchura(Carpeta,Archivo):

	if Carpeta == Archivo:
		return Archivo
	if Nodsig:
		contador = 0
		for X in Nodsig:
			 contador += 1
		if contador > 1:
			print("Nodo Priciopal: " + Nodsig[0])
			Nodsig.pop(0)
	if auxiliar:
		del auxiliar[:]
	for i in data:
		if i[0] == Carpeta:
			Nodsig.append(i[1])
			auxiliar.append(i[0])
			if i[1] == Archivo:
				nodo = primeroAnchura(i[1],Archivo)
				return nodo
	revisados.append(list(set(auxiliar)))
	if revisados:
		print("Nodos Recorridos")
		print(str(revisados))
		print(Nodsig[0])
		camino.append(Nodsig[0])
		return primeroAnchura(Nodsig[0],Archivo)

nodo = primeroAnchura("C:","Steam.exe")
print("Hijo Encontrado Del Nodo Principal: " +nodo)
cam = []
if nodo:
	for c in camino:
		if c not in cam:
			cam.append(c)
	print("Padres(Nodos Evaluados)")
	print(cam)
else:
	print("No Se Encontro")

