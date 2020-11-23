import os
import time
os.system('echo off')
os.system('cls')
print('For Help Press H')
time.sleep(5)
os.system('cls')
for i in range(0,9999999999999999):
	a = input(': ')
	b = input(': ')
	c = input(': ')
	if a == 'H' or b == "H" or c == "H" or a == 'h' or b == "h" or c == "h":
		os.system('cls')
		print('********************************************************************************')
		print('********************************************************************************')
		print('********************************************************************************')
		print('                                   Help')
		print('********************************************************************************')
		print('********************************************************************************')
		print('********************************************************************************')
		print('\nType In This Way:\nNumber\n\nOperator\n\nNumber')
		print('\n\nFor Example:')
		print('If U Press \n:1\n:+\n:1\nYou will get 2')
		print('\n\n\n\n\n\n\n\n\n')
		a = input('Press Any Key To Continue...')
		os.system('cls')
	try:
		if '+' in b:
			os.system('cls')
			conc = int(a) + int(c)
			print(f'{a} {b} {c} = {conc}')
		elif '-' in b:
			os.system('cls')
			conc = int(a) - int(c)
			print(f'{a} {b} {c} = {conc}')
		elif '*' in b:
			os.system('cls')
			conc = int(a) * int(c)
			print(f'{a} {b} {c} = {conc}')
		elif '/' in b:
			os.system('cls')
			conc = int(a) / int(c)
			print(f'{a} {b} {c} = {conc}')
		else:
			os.system('cls')
			print('Number Error..')
	except:
		os.system('cls')
		print('You are not allowed to give A to Z characters')


