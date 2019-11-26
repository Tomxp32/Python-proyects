#from clase1 import *
# En este archivo

from math_main.clases.Clase1_logica import *
from math_main.clases.clase1 import *
from math_main.clases.clase2 import *


clases = '''
		Temas Matematicas discretas:
		-Logica
		-Operadores logicos
		-Precedencia de operadores logicos
		-Operaciones con bits
		-Tautologia, contingencia, contradicción y satisfactoria
		-Equivalencias logicas (Leyes logicas)
		-Cuantificadores
		-Metodos de demostración
'''

about = '''
		Las matemáticas discretas son un área de las matemáticas encargadas del estudio de los conjuntos discretos: 
		finitos o infinitos numerables.
		
		En oposición a las matemáticas continuas, que se encargan del estudio de conceptos como la continuidad y el 
		cambio continuo, las matemáticas discretas estudian estructuras cuyos elementos pueden contarse uno por uno 
		separadamente. Es decir, los procesos en matemáticas discretas son contables, como por ejemplo, los números 
		enteros, grafos y sentencias de lógica.
		
		Mientras que el cálculo infinitesimal está fundado en los números reales que no son numerables, la matemática 
		discreta es la base de todo lo relacionado con los números naturales o conjuntos numerables.
		
		Son fundamentales para la ciencia de la computación, porque solo son computables las funciones de conjuntos 
		numerables.
		
		La clave en matemáticas discretas es que no es posible manejar las ideas de proximidad o límite y suavidad en 
		las curvas, como se puede en el cálculo. Por ejemplo, en matemáticas discretas una incógnita puede ser 2 o 3, 
		pero nunca se aproximará a 3 por la izquierda con 2.9, 2.99, 2.999, etc. Las gráficas en matemáticas discretas 
		vienen dadas por un conjunto finito de puntos que se pueden contar por separado; es decir, sus variables son 
		discretas o digitales, mientras que las gráficas en cálculo son trazos continuos de rectas o curvas; es decir, 
		sus variables son continuas o analógicas.
'''

def math():
	op = input('\n\tWelcome to discrete math, what do you want to do: ')
	if op == 'help':
		print('''
		Help

		1. Ver la lista de clases
		2. Tomar un test de todas las clases
		3. Acerca de esta materia
			''')
		math()
	elif op == '1':
		print(clases)
		math()
	elif op == '2':
		logica_test()
		math()
	elif op == '3':
		print(about)
		math()
	elif op == 'exit':
		print('\n\tSaliendo...')
	else:
		math()