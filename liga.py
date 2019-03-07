from lxml import etree

# Función para pedir número de jornada
def jornada():
	jornada=int(input("Dígame la jornada(1-38): "))
	while jornada > 38 or jornada < 1:
		print("ERROR: Número de jornada incorrecta")
		jornada=int(input("Dígame la jornada(1-38): "))
	return jornada

# Funcion para mostrar partidos, hora y canal de tv.
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
		print("2.Gol")
		print("3.Partidazo")
		print("4.C+L")
		print("5.C+ Liga")
		print("6.Teledeporte")
		print()
		opcion=int(input("Elige opción: "))
		print()

		if opcion == 1:
			emision="beIN"
			return emision
		elif opcion == 2:
			emision="Gol"
			return emision
		elif opcion == 3:
			emision="Partidazo"
			return emision
		elif opcion == 4:
			emision="C+L"
			return emision
		elif opcion == 5:
			emision="C+ Liga"
			return emision
		elif opcion == 6:
			emision="Teledeporte"
			return emision
		else:
			print()
			print("Error de opción")
			print()

def canal(arbol,tv_):
	local=arbol.xpath('//evento[tv="%s"]/equipolocal/text()'%tv_)
	visi=arbol.xpath('//evento[tv="%s"]/equipovisitante/text()'%tv_)
	fecha=arbol.xpath('//evento[tv="%s"]/fecha/text()'%tv_)
	return zip(fecha,local,visi)

def pedir_equipo():
	while True:
		print("Dime el equipo:")
		print("1.R. Madrid")
		print("2.Barcelona")
		print("3.Eibar")
		print("4.Leganés")
		print("5.Levante")
		print("6.Valencia")
		print("7.R. Sociedad")
		print("8.Atlético")
		print("9.Girona")
		print("10.Espanyol")
		print("11.Sevilla")
		print("12.Athletic")
		print("13.Getafe")
		print("14.Celta")
		print("15.Alavés")
		print("16.Las Palmas")
		print("17.Málaga")
		print("18.Villarreal")
		print("19.Betis")
		print("20.Deportivo")
		print()
		opcion=int(input("Elige opción: "))
		print()

		if opcion == 1:
			equipo="R. Madrid"
			return equipo
		elif opcion == 2:
			equipo="Barcelona"
			return equipo
		elif opcion == 3:
			equipo="Eibar"
			return equipo
		elif opcion == 4:
			equipo="Leganés"
			return equipo
		elif opcion == 5:
			equipo="Levante"
			return equipo
		elif opcion == 6:
			equipo="Valencia"
			return equipo
		elif opcion == 7:
			equipo="R. Sociedad"
			return equipo
		elif opcion == 8:
			equipo="Atlético"
			return equipo
		elif opcion == 9:
			equipo="Girona"
			return equipo
		elif opcion == 10:
			equipo="Espanyol"
			return equipo
		elif opcion == 11:
			equipo="Sevilla"
			return equipo
		elif opcion == 12:
			equipo="Athletic"
			return equipo
		elif opcion == 13:
			equipo="Getafe"
			return equipo
		elif opcion == 14:
			equipo="Celta"
			return equipo
		elif opcion == 15:
			equipo="Alavés"
			return equipo
		elif opcion == 16:
			equipo="Las Palmas"
			return equipo
		elif opcion == 17:
			equipo="Málaga"
			return equipo
		elif opcion == 18:
			equipo="Villarreal"
			return equipo
		elif opcion == 19:
			equipo="Betis"
			return equipo
		elif opcion == 20:
			equipo="Deportivo"
			return equipo
		else:
			print()
			print("Error de opción")
			print()

def maximo_goles(arbol,equipo):
	glocal=arbol.xpath('//evento[equipolocal="%s"]/resultadolocal/text()'%equipo)
	gvisitante=arbol.xpath('//evento[equipovisitante="%s"]/resultadovisitante/text()'%equipo)
	return glocal,gvisitante

while True:
	print()
	print("1.Pedir jornada y mostrar partidos, hora y canal de TV")
	print("2.Te cuenta el número de goles que se han marcado en una determinada jornada")
	print("3.Pedir una jornada y canal de TV, y te dice qué partidos y a qué hora se emitirán en ese canal")
	print("4.Pedir equipo y decir en que partido de la temporada ha metido más goles")
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
		arbol = etree.parse('jornada%i.xml' % jorna)
		for fecha,local,visi,tv in partidos(arbol):
		    print ("Fecha y hora:",fecha)
		    print("Local: %s -- Visitante: %s" % (local,visi))
		    print("Canal/es de TV: %s" % tv)
		    print("="*40)
		print()

	elif opcion == 2:
		jorna=jornada()
		arbol = etree.parse('jornada%i.xml' % jorna)
		glocal,gvisitante = goles(arbol)
		local = list(glocal)
		local = map(int,local)
		visitante = list(gvisitante)
		visitante = map(int,visitante)
		print()
		print("En la jornada",jorna,"se han marcado un total de",sum(local)+sum(visitante),"goles")
		print()

	elif opcion == 3:
		jorna=jornada()
		tv_=pedir_canal()
		arbol = etree.parse('jornada%i.xml' % jorna)
		for fecha,local,visi in canal(arbol,tv_):
		    print("Fecha y hora:",fecha)
		    print("Local: %s -- Visitante: %s" % (local,visi))
		    print("="*40)
		print()

	elif opcion == 4:
		equipo=pedir_equipo()
		print(equipo)
		jornadas = 38
		max_jornada = 0
		for i in range(1,jornadas+1):
			arbol = etree.parse('jornada%i.xml' % i)
			glocal,gvisitante = maximo_goles(arbol,equipo)
			if len(glocal)>0:
				if glocal[0] == "0":
					print("En la jornada",i,"el",equipo,"no marcó goles")
				else:
					print("En la jornada",i,"el",equipo,"marcó",glocal[0],"goles")
			else:
				if gvisitante[0] == "0":
					print("En la jornada",i,"el",equipo,"no marcó goles")
				else:
					print("En la jornada",i,"el",equipo,"marcó",gvisitante[0],"goles")

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