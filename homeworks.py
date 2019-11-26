# I will not delete any task, the numbers will be added and added, 
# these will be indicated in the physical notebook.
from datetime import date
from datetime import datetime
from fundamentos_test import *
from extra_main.semanas import *

def homeworks() :
	print('\n\t\t1. Pass math classes')
	print('\n\t\t2. Make the slides about the mathematical demonstrations')
	print('\n\t\t3. Study for the math exam')
	print('\n\t\t4. Ask Sam if she has used the welfare unit (25-11-2019)')
	print('\n\t\t5. Make an appointment with the dentist (25-11-2019)')
	home = input('\n\t\thomeworks>: ')
	if home == '1':
		print('''
		Pass the math classes by hand, for the portfolio, which will be delivered 
		before the final exam.''')
	elif home == 'exit':
		exit()

#print(today)
#print(today.day)
#https://codigofacilito.com/articulos/fechas-python

def christmas():
	today = date.today()
	day = today.day

	print('\n\tFaltan:', (27- day), 'dias para la prueba de matematicas discretas')
	print('\n\tFaltan:', (28 - day), 'dias para la leccion de sistemas operativos')
	print('\n\tFaltan:', (30 - day) + 8, 'dias para el cumpleanos de busy')
	print('\n\tFaltan:', (30 - day) + 20, 'dias para la cena en la casa de Julio, JOJO!!')
	print('\n\tFaltan:', (30 - day) + 25, 'dias navidad, JOJO!!')
	print('\n\tFaltan:', (30 - day) + 31, 'dias para fin de ano')


def semana47(state):
	if state == True:
		print('Estamos en la semana 47 del 2019 (18 noviembre 2019 - 24 noviembre 2019)')
		christmas()
	else:
		print('No estamos en la semana 47 del 2019 :')

#semana47(True)
#semana47(False)