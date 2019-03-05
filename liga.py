from lxml import etree
arbol = etree.parse('liga.xml')
cont = 0
# Pedir número de jornada y año
	# Abrir documento dependiendo de jornada y año

	# Mostrar partidos, hora y canal de tv
def partidos(arbol):
	fecha=arbol.xpath("//evento/fecha/text()")
	local=arbol.xpath("//evento/equipolocal/text()")
	visitante=arbol.xpath("//evento/equipovisitante/text()")
	canal=arbol.xpath("//evento/tv/text()")
	return zip(fecha,local,visitante,canal)

while True:
	print("1.Pedir jornada y año y mostrar partidos, hora y canal de TV")
	print("2.Te cuenta el número de goles que se han marcado en una determinada jornada")
	print("3.Pedir una jornada y canal de TV,y te dice qué partidos y a qué hora se emitirán en ese canal")
	print("4.Pedir árbitro y temporada y decir cuantos partidos ha arbitrado")
	print("5.Quiniela de jornada seleccionada")
	print("0.Salir")
	opcion=int(input("Elige opción: "))

	if opcion == 0:
		print()
		print("Adiós!")
		print()
		break;

	elif opcion == 1:
		for fecha,local,visi,tv in partidos(arbol):
		    print ("Fecha y hora:",fecha)
		    print("Local: %s -- Visitante: %s" % (local,visi))
		    print("Canal/es de TV: %s" % tv)
		    print("="*40)

	else:
		print()
		print("Error de opción")
		print()

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