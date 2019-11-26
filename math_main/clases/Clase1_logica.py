# CLase 1 Logica

logica = '''
		La lógica es la ciencia formal y rama tanto de la filosofía como de las matemáticas que 
		estudia los principios de la demostración y la inferencia válida, las falacias, las 
		paradojas y la noción de verdad.

		La lógica matemática es la rama más matemática de la lógica, que estudia la inferencia 
		mediante sistemas formales como la lógica proposicional, la lógica de primer orden y la 
		lógica modal. La lógica computacional es la aplicación de la lógica matemática a las 
		ciencias de la computación. La lógica filosófica utiliza los métodos y resultados de la 
		lógica moderna para el estudio de problemas filosóficos.

		Los orígenes de la lógica se remontan a la Edad Antigua, con brotes independientes en 
		China, India y Grecia. Desde entonces, la lógica tradicionalmente se considera una rama 
		de la filosofía, pero en el siglo XX la lógica ha pasado a ser principalmente la lógica 
		matemática, y por lo tanto ahora también se considera parte de las matemáticas, e 
		incluso una ciencia formal independiente.
		'''

def about():
	print(logica)

def test1_():
	input('\n\tWhat is logic? \n\t:')
	input('\n\tWhat studies mathematical logic? \n\t:')
	input('\n\tWhat is computational logic? \n\t:')
	input('\n\tDescribe some history about logic \n\t:')

def logica_test():
	test1 = input('\n\tWelcome to the logic test, do you want to take it? ')
	if test1 == 'y':
		test1_()
	else:
		print('\n\tWell take care')



