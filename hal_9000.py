print("\n\tHello, I'm Heuristically Programmed Algorithmic Computer also know as Hal 9000")
def hal():
	make = input('\n\t: ')

	if make == '1':
		print('\n\tDo what you want to do')
		hal()
	elif make == '2':
		print('\n\tRead a book, and do not waste your time in social networks')
		hal()
	elif make == '3':
		print("\n\tKill 'em all")
		hal()
	elif make == 'exit':
		print("\n\tGoodbye don't forget to open me everyday")

	elif make == 'help':
		print('\n\tMy functions are:')
		print('\t1. Make your homework')
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
		instances of which are located throughout the ship. HAL 9000 is voiced by Douglas Rain in the two feature 
		film adaptations of the Space Odyssey series. HAL speaks in a soft, calm voice and a conversational manner, 
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



