from lxml import etree
arbol = etree.parse('liga.xml')
# Pedir número de jornada y año
def temporada():
	while True:
		print("1.Temporada 2012-13")
		print("2.Temporada 2013-14")
		print("3.Temporada 2014-15")
		print("4.Temporada 2015-16")
		print("5.Temporada 2016-17")
		print("6.Temporada 2017-18")
		print("7.Temporada 2018-19")
		opcion=int(input("Elige opción: "))

		if opcion == 1:
			temporada="2012_13"
			return temporada
		elif opcion == 2:
			temporada="2013_14"
			return temporada
		elif opcion == 3:
			temporada="2014_15"
			return temporada
		elif opcion == 4:
			temporada="2015_16"
			return temporada
		elif opcion == 5:
			temporada="2016_17"
			return temporada
		elif opcion == 6:
			temporada="2017_18"
			return temporada
		elif opcion == 7:
			temporada="2018_19"
			return temporada
		else:
			print()
			print("Error de opción")
			print()


	# Abrir documento dependiendo de jornada y año


# Funcion para mostrar partidos, hora y canal de tv
def partidos(arbol):
	fecha=arbol.xpath("//evento/fecha/text()")
	local=arbol.xpath("//evento/equipolocal/text()")
	visitante=arbol.xpath("//evento/equipovisitante/text()")
	canal=arbol.xpath("//evento/tv/text()")
	return zip(fecha,local,visitante,canal)

def goles(arbol):
	glocal=arbol.xpath("//evento/resultadolocal/text()")
	gvisitante=arbol.xpath("//evento/resultadovisitante/text()")
	return glocal,gvisitante

while True:
	print("1.Pedir jornada y año y mostrar partidos, hora y canal de TV")
	print("2.Te cuenta el número de goles que se han marcado en una determinada jornada")
	print("3.Pedir una jornada y canal de TV,y te dice qué partidos y a qué hora se emitirán en ese canal")
	print("4.Pedir árbitro y temporada y decir cuantos partidos ha arbitrado")
	print("5.Quiniela de jornada seleccionada")
	print("0.Salir")
	opcion=int(input("Elige opción: "))
	print()

	if opcion == 0:
		print()
		print("Adiós!")
		print()
		break;

	elif opcion == 1:
		tempo=temporada()
		for fecha,local,visi,tv in partidos(arbol):
		    print ("Fecha y hora:",fecha)
		    print("Local: %s -- Visitante: %s" % (local,visi))
		    print("Canal/es de TV: %s" % tv)
		    print("="*40)
		print()

	elif opcion == 2:
		glocal,gvisitante = goles(arbol)

		
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