from lxml import etree
arbol = etree.parse('liga.xml')
	
#def partidos(arbol):
#	fecha=arbol.xpath("//evento/fecha/text()")[0]
#	local=arbol.xpath("//evento/equipolocal/text()")[0]
#	return fecha,local

#fech,loc = partidos(arbol)
#print("Fecha: %s"%fech)
#print("Equipo Local: %s"%loc)

print(arbol)