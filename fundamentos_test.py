def principal ():
	a = input('\nQuieres hacer un test sobre la clase 1? ')

	if a == 'y':
		print('\nEscribe las respuestas correctas')
		print('\n1. Que es un sistema de informacion')
		input('\n\t: ')
		print('''\n\t
			Es un tipo especializado de sistema. Conjunto de elementos que interactuan entre 
			si con el fin de apoyar las actividades de una empresa o negocio.''')
		print('\n2. Cuales son los componentes de un sistema de informacion')
		input('\n\t: ')
		print('''\n\t
		* Entrada: 
		* Procesamiento: 
		* Salida: 
		* Retroalimentacion: 

		Datos -> Sistema -> Informacion
			''')

		print('\n3. Elementos de un sistema de informacion')
		input('\n\t: ')
		print('''
		* Equipo computacional
		* El recurso humano
		* Los datos o informacion
		* Los programas
		* Los programas
		* Las telecomunicaciones
		* Procedimientos
			''')

		print('\n4. Describe los procedimientos')
		input('\n\t: ')
		print('''	
			Que incluyen las politicas y reglas de operacion, tanto en lo funcional, como 
			en los mecanismos para hacer trabajar una app''')

		print('\n5. Cuales son las actividades basicas de un SI')
		input('\n\t: ')
		print('''
			* Entrada de datos
			* Almacenamiento de datos
			* Procesamientos
			* Salida de informacion
			''')

		print('\n6. Describe la entrada de datos')
		input('\n\t: ')
		input('\t: ')
		print('\n7. Describe el almacenamiento de datos')
		input('\n\t: ')
		input('\t: ')
		print('\n8. Describe el procesamiento de datos')
		input('\n\t: ')
		input('\t: ')
		print('\n9. Describe la salida de informacion')
		input('\n\t: ')
		input('\t: ')
		res = input('\n\tQuieres volver al inicio? ')
		if res == 'y':
			principal()
	elif a == 'n':
		print('1. Volver al inicio')
		print('2. Salir del programa')
		r = input('Respuesta: ')
		if r == '1':
			principal()
		else:
			print('Fin del programa')

principal()



