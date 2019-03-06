from lxml import etree

# Función para pedir número de jornada
def jornada():
	jornada=int(input("Dígame la jornada(1-38): "))
	while jornada > 38 or jornada < 1:
		print("Número incorrecto de jornada.")
		jornada=int(input("Dígame la jornada(1-38): "))
		return jornada

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

def pedir_canal():
	while True:
		print("Dime el canal por el que quiere preguntar:")
		print("1.beIN")
		print("2.GOL")
		print("3.GolT")
		print("4.C+L")
		print("5.C+ Liga")
		print("6.Teledeporte")
		print()
		canal=int(input("Elige opción: "))
		print()

		if opcion == 1:
			canal="beIN"
			return canal
		elif opcion == 2:
			canal="GOL"
			return canal
		elif opcion == 3:
			canal="GolT"
			return canal
		elif opcion == 4:
			canal="C+L"
			return canal
		elif opcion == 5:
			canal="C+ Liga"
			return canal
		elif opcion == 6:
			canal="Teledeporte"
			return canal
		else:
			print()
			print("Error de opción")
			print()

def canal(arbol):
	local=arbol.xpath('//evento[tv="%s"]/../equipolocal/text()'%tv_)
	visi=arbol.xpath('//evento[tv="%s"]/../equipovisitante/text()'%tv_)
	fecha=arbol.xpath('//evento[tv="%s"]/../fecha/text()'%tv_)
	return zip(fecha,local,visi)

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
		jorna=jornada()
		arbol = etree.parse('https://www.marca.com/marcador/futbol/iphone/1/2017_18/fase0/jornada_%s/marcador.xml' % jorna)
		for fecha,local,visi,tv in partidos(arbol):
		    print ("Fecha y hora:",fecha)
		    print("Local: %s -- Visitante: %s" % (local,visi))
		    print("Canal/es de TV: %s" % tv)
		    print("="*40)
		print()

	elif opcion == 2:
		glocal,gvisitante = goles(arbol)
		print(sum(glocal))

	elif opcion == 3:
		tv_=pedir_canal()
		print(tv_)
		for fecha,local,visi in canal(arbol):
		    print ("Fecha y hora:",fecha)
		    print("Local: %s -- Visitante: %s" % (local,visi))
		    print("Canal/es de TV: %s" % tv)
		    print("="*40)
		    print("Hola")
		print()

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