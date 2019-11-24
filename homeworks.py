# I will not delete any task, the numbers will be added and added, 
# these will be indicated in the physical notebook.

def homeworks() :
	print('\n\t\t1. Pass math classes')
	print('\n\t\t2. Make the slides about the mathematical demonstrations')
	print('\n\t\t3. Study for the math exam')
	home = input('\n\t\thomeworks>: ')
	if home == '1':
		print('''
	Pass the math classes by hand, for the portfolio, which will be delivered 
	before the final exam.
			''')
	elif home == 'exit':
		exit()