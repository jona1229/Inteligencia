import json
with open('labase.json') as file:
	data = json.load(file)
ruta=[]

def primeroProfundidad(Carpeta,Archivo):
	
	if Carpeta == Archivo:
		return Archivo
		
	for d in data:
		if d[0] == Carpeta:
			ruta.append(Carpeta)
			arch=primeroProfundidad(d[1],Archivo)
			if arch:
				return arch
	if ruta:
		ruta.pop()


arch=primeroProfundidad("C:","abc.jpg")
rt = ""
if arch:
	for r in ruta:
		rt=rt+r+"/"
	rt=rt+arch
	print(rt)
else:
	print("No Existe")

