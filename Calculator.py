import os
for i in range(0,99999999999999):
	a = input('> ')
	try:
		os.system('cls')
		print(f'{a} = {eval(a)}')
	except:
		os.system('cls')
		print('Wrong Input')
	if 'e' in a:
		os.system('cls')
		bb = input('Press Any Key To Continue: ')
		break
