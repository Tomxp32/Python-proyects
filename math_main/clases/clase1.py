clase_1 = '''
			
	Demostración en matemática

	En matemáticas, una demostración o bien una prueba es un argumento deductivo para asegurar la verdad 
	de una proposición matemática. En la argumentación se pueden usar otras afirmaciones previamente 
	establecidas, tales como teoremas o bien las afirmaciones iniciales o axiomas. En principio una 
	demostración se puede rastrear hasta afirmaciones generalmente aceptadas, conocidas como axiomas. 
	Las demostraciones son ejemplos de razonamiento deductivo y se distinguen de argumentos inductivos 
	o empíricos; una demostración debe demostrar que una afirmación es siempre verdadera (ocasionalmente 
	al listar todos los casos posibles y mostrar que es válida en cada uno), más que enumerar muchos 
	casos confirmatorios. Una afirmación no probada que se cree verdadera se conoce como conjetura.

	Las demostraciones emplean lógica pero normalmente incluyen una buena parte de lenguaje natural, el 
	cual usualmente admite alguna ambigüedad. De hecho, la gran mayoría de las demostraciones en las 
	matemáticas escritas puede ser considerada como aplicaciones de lógica informal rigurosa. Las 
	demostraciones puramente formales, escritas en lenguaje simbólico en lugar de lenguaje natural, se 
	consideran en teoría de la demostración. La distinción entre demostraciones formales e informales 
	ha llevado a examinar la lógica matemática histórica y actual, el cuasi-empirismo matemático y el 
	formalismo matemático. La filosofía de las matemáticas concierne al rol del lenguaje y la lógica en 
	las demostraciones, y en las matemáticas como lenguaje.

	El hecho de no conocer ninguna demostración de un teorema no implica su no veracidad; sólo la 
	demostración de la negación de este resultado implica que es falso.

	Matematicas discretas clase #5 (20-11-2019)

	Aporte proxima clase
		- Se puede traer el formulario
		- Este formulario solo se puede usar en este aporte, para el examen no.

	Hoy debimos tener el aporte pero al profesor se le olvido decirnos. 

	Clase: Cuantificadores logicos #2

		Usando cuantificadores: 

		El dominio de los enteros:

		* Usaando implicaciones: El cubo de todos loe enteros negativos es negativo.

		Ax (x < 0) -> (x^3 < 0)

		Ejercicios en clase:

			- Ax eR / x^2 > 0

			Para todo x existe un numero real que cumpla x^2 > 0

			- Demostrar que x + y = 0 si x = -y
			- ExeR|x^2 > 0

		Tema de hoy = 'Demostraciones' (capitulo metodo de demostracion)

		Es un tema complejo, no lo tomara en el aporte, en el examen quizas habra una pregunta sobre esto.

		¿Que son?

		- Ax eR / x^2 > 0 es falso, ¿por que?

		Como demostramos esto =  buscando un numero
		/ =  tal que
		Ex = 0 / x^2 no es mayor a si mismo, es igual

		Metodos de demostracion: 

			- Demostracion directa
			- Demostracion indirecta
			- Demostracion al absurdo
			- Demostracion por contraejemplo

		En el caso anterior estamos demostrando a traves de un contrajemplo que eso no es verdadero, 
		es falso. Este metodo se utiliza cuando algo se toma por verdadero. 

		En el segundo caso:  Demostrar que x + y = 0 si x = -y

			x + y = 0
			x + (-x) = 0
			x - x = 0
			0 = 0

			En este caso es una demostracion directa

		En una demostracion indirecta:

			x + y != o si yeR
			x + y = 0
			x + (-x) = 0
			0=0

			Se parte de lo contrario para demostrar una verdad

		En el tercer caso

			es una demostracion directa

			si x=2, x^2 = 0


		No hay solo 4 metodos, pero son los mas utilizados.

		Reduccion al absurdo: 

			Demustra que es falso haciendo una reduccion al absurdo.



		Tarea: 

		Consultar 1 demostracion de cada tipo de manera individual :D

		en el portafoleo, que se muestra el dia del examen hay que traer los resumenes

		Diapositivas:

			Consultar los temas objetivos del 1 al 4
			Solo 4 diapositivas

			Tenemos que enviar al espacio virtual estas diapositivas :'v

		Esto es un taller para la siguiente clase. Buscar 4 demostraciones 1 de cada tema explicarlas y ubicar el teorema

		2. 

		Aporte

			Tablas de verdad
			Para todo existencial
			Leyes, demostracion por leyes

		Siguiente clase:
		Induccion matematica

		* Conjuntos: 

		Termina la clase :DDDDDDDDDD 10:33 XDDDDDD
			'''

def clases (clase):
	if clase == '1':
		print('\n\tClase 5 xd')
		print(clase_1)

def clase1 ():
	print('\n\tWeeeey si funciono!!!! - Clase 1')

def c_math():
	print('\tWe are the champions')