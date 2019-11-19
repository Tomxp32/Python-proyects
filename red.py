# This is red is named by berserk, it'll be the program that will make's me a better human

ruta = 'C:/Users/usuario/Desktop/Primer semestre/Introduccion a la programacion C/Proyectos/Materias a python/prueba_red.txt'
carl_sagan = 'C:/Users/usuario/Desktop/Primer semestre/Introduccion a la programacion C/Proyectos/Materias a python/El mundo y sus demonios capitulos/capitulo1.txt'
archivo = open(ruta, 'r')
carl = open(carl_sagan, 'r')
ok = str(carl.read())

#print(archivo.read())

# LOL si lee los archivos externos y hasta los imprime!!!

carls_s = '''
	El mundo y sus demonios. La ciencia como una luz en la oscuridad, es un libro de Carl Sagan 
	publicado en 1995 que intenta explicar el método científico al ciudadano corriente, y anima 
	a los lectores a utilizar el pensamiento crítico o escéptico.

	El libro en general, es una reflexión contra la pseudociencia, pero más específicamente, es 
	una defensa profunda y muy acertada de todos los enormes beneficios que la ciencia ha 
	producido a lo largo de la historia (vacunas, antibióticos, medicamentos, aviación, etc.). 
	Así mismo y sin perder nunca el suelo, Sagan en uno de sus capítulos hace referencia al mal 
	uso que se ha hecho de la ciencia, y enfatiza que en buen nivel se debió a la "ingenuidad" 
	de aquellos científicos que lo permitieron (ej. Proyecto Manhattan), dejando entonces muy 
	claro que la investigación científica no solo tiene un marco moral o ético de procedimientos 
	(metodología científica estricta), sino que el científico además, debe tener una idea muy 
	clara del impacto que pudiesen tener en la sociedad sus investigaciones.

	Sagan explica métodos muy útiles que ayudarían al lector a poder distinguir entre las ideas 
	que provienen de una ciencia genuina, de las que solo parecen simularla bastante bien: 
	pseudociencia. También indica, que cuando se plantea una nueva idea, ésta debiera considerarse 
	como posible solamente, entonces, tendría que ser probada muy rigurosamente, y luego solo 
	así, aceptarse. El pensamiento escéptico, dice, nos da medios para construir, entender y 
	razonar, para reconocer ideas válidas o erróneas hasta donde la verificación sea posible.

	En alguno de sus capítulos tiene argumentos fuertes que hacen una crítica dura contra el 
	sistema educativo estadounidense de los noventas.

		Leer el libro en pdf:

		- Pagina: 14 (capitulo 1)

	'''



def book_1():
	print(carl)

homework = input('\n\tDo you have homework? y/n ')

if homework == 'y' or homework == 'yes':
	print('\n\tWhat are you waiting to do it')
elif homework == 'n' or homework == 'no':
	print('\n\tThen, you should study')
else:
	print("\n\tI't seems you dont have nothing to do")
	print('\tDo you want to read somethin?')
	read = input('\n\tWanna read: ')
	if read == 'y':
		print('\n\tWhat book do you want to read')
		print("\t1. The wordl and it's demons")
		print("\t2. Oyasumi punpun")
		print("\t3. Berserk")

		book = input('\n\tBook: ')
		if book == '1':
			print(ok)
	elif read == 'n':
		print('\n\tOk, then go waste your time on facebook')


