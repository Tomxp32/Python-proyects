import time
#from math_main.clases.clase1 import *
#from math_main.clases.clase2 import *
from homeworks import *
from math_main.math import *
#from math_main.math import *
#from math_main import clases

clase1()
clase2()
math(' Omamori himari :v')
cmath()

tim = 0

print('\n\t',time.asctime())
print("\n\tHello, I'm Heuristically Programmed Algorithmic Computer also know as Hal 9000")

def exit():
	print("\n\tGoodbye don't forget to open me everyday")

def hal():
	make = input('\n\t: ')

	if make == 'subjects':
		
		home = input('\n\tsubjects>: ')

		if home == '1':
			print('\n\tWatch a video about logical quantifiers')
			print("\n\tYou haven't programmed anything yet >:v lazy")
			hal()
		elif home == 'help':
			print('\n\tSubjects')
			print('\n\t1. Fundamentals of information systems')
			print('\t2. Discrete mathematics')
			print('\t3. Introduction to programming')
			print('\t4. Operating systems')
			hal()
		elif home == '2':
			print("\n\tcheck the classes of this subject that you don't know")
			print('\n\tDios no existe :v')
			print("\n\tYou haven't programmed anything yet >:v lazy")
			clases('1')

			hal()
		elif home == '3':
			print('''
		Practice python, today (11-19-2019), my teacher has told me that he is taught for his 
		mastery, artificial intelligence in this language.''')
			print("\n\tYou haven't programmed anything yet >:v lazy")
			hal()
		elif home == 'exit':
			exit()
		else:
			hal()

	elif make == '2':
		print('\n\tRead a book, and do not waste your time in social networks')
		print("\n\tYou haven't programmed anything yet >:v lazy")
		hal()
	elif make == '3':
		print("\n\tKill 'em all")
		print("\n\tYou haven't programmed anything yet >:v lazy")
		hal()

	elif make == 'time':
		print('''
	You are young and life is long and there is time to kill today.
	And then one day you find ten years have got behind you.
	No one told you when to run, you missed the starting gun.
			''')
		print('\n\t',time.asctime()) 
		hal()

	elif make == 'homeworks':
		print('\n\t',homeworks())
		hal()

	elif make == 'exit':
		exit()

	elif make == 'help':
		print('\n\tMy functions are:')
		print('\t1. First semester subjects')
		print('\t2. Make you better')
		print('\t3. Seek and destroy')
		hal()
	
	elif make == 'who are you':
		print('''
		HAL 9000 is a fictional artificial intelligence character and the main antagonist in Arthur C. Clarke's 
		Space Odyssey series. First appearing in the 1968 film 2001: A Space Odyssey, HAL (Heuristically Programmed 
		ALgorithmic Computer) is a sentient computer (or artificial general intelligence) that controls the systems 
		of the Discovery One spacecraft and interacts with the ship's astronaut crew. Part of HAL's hardware is 
		shown toward the end of the film, but he is mostly depicted as a camera lens containing a red or yellow dot, 
		instances of which are located throughout the ship. HAL speaks in a soft, calm voice and a conversational manner, 
		in contrast to the crewmen, David Bowman and Frank Poole.

		In the film, HAL became operational on 12 January 1992 at the HAL Laboratories in Urbana, Illinois as 
		production number 3. The activation year was 1991 in earlier screenplays and changed to 1997 in Clarke's 
		novel written and released in conjunction with the movie. In addition to maintaining the Discovery 
		One spacecraft systems during the interplanetary mission to Jupiter (or Saturn in the novel), HAL is capable 
		of speech, speech recognition, facial recognition, natural language processing, lip reading, art appreciation, 
		interpreting emotional behaviours, automated reasoning, spacecraft piloting and playing chess.
				''')
		hal()
	else:
		hal()

hal()



