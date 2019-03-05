from lxml import etree
arbol = etree.parse('liga.xml')
cont = 0
# Pedir número de jornada y año

	# Abrir documento dependiendo de jornada y año
#eventos=arbol.xpath("//evento")
#print(eventos)
#for datos in eventos:
#	print(datos.xpath("./fecha/text()")[cont])
#	print(datos.xpath("./equipolocal/text()")[cont])
#	print(datos.xpath("./equipovisitante/text()")[cont])
#	print(datos.xpath("./tv/text()")[cont])
#	cont = cont + 1
#	print(cont)
	# Mostrar partidos, hora y canal de tv
def partidos(arbol):
	fecha=arbol.xpath("//evento/fecha/text()")
	local=arbol.xpath("//evento/equipolocal/text()")
	visitante=arbol.xpath("//evento/equipovisitante/text()")
	canal=arbol.xpath("//evento/tv/text()")
	return zip(fecha,local,visitante,canal)

for a,e,i,o in partidos(arbol):
    print ("Fecha y Hora:",a,e,"-",i,"   Canales:",o)

# Pedir número de jornada y año
	# Abrir documento de esa jornada y año
	# Contar goles de esa jornada

# Pedir jornada, año y canal de TV
	# Abrir documento de jornada y año
	# Mostrar partidos de esa jornada en ese canal

# Pedir temporada y arbitro
	# Abrir documentos de temporada
	# Mostrar partidos arbitrados por ese arbitro

# Pedir una jornada
	# Abrir documento de jornada
	# Id mostrando partidos de esa jornada y al final mostrar si
	# si se ha acertado con la quiniela	