from lxml import etree
arbol = etree.parse('liga.xml')
	
# Pedir número de jornada y año

	# Abrir documento dependiendo de jornada y año
def partidos(arbol):
	fecha=arbol.xpath("//evento/fecha/text()")[0]
	local=arbol.xpath("//evento/equipolocal/text()")[0]
	visitante=arbol.xpath("//evento/equipovisitante/text()")[0]
	canal=arbol.xpath("//evento/tv/text()")[0]
	return fecha,local,visitante,canal

fech,loc,vis,tv = partidos(arbol)
print("Fecha: %s"%fech)
print("Equipo local: %s"%loc)
print("Equipo visitante: %s"%vis)
print("Canal de TV: %s"%tv)

	# Mostrar partidos, hora y canal de tv

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
doc = etree.parse('prueba.xml')

print(doc.xpath("//price/text()"))