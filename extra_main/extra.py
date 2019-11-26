from extra_main.english.eng import *

print('\n\tHi, im extra new module for english and others')

# Esta es la funcion que se llamara desde hal
def extra():
	ext = input('\n\textra>: ')
	if ext == 'help':
		print('''
		Funciones principales:
		1. Repasar ingles
		2. Leer un libro
		3. Aprender python
		''')