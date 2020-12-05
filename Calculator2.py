from tkinter import *
import keyboard as kk
root = Tk()
root.title('Calculator')
root.minsize(900,100)
root.maxsize(900,100)
def what():
	for i in range(0,99999999999):
		try:
			root.update()
			if kk.is_pressed('enter'):
				aa_aa.set(eval((aa_aa.get())))
		except:
			pass
aa_aa = StringVar()
Entry(textvariable = aa_aa,font = "comicsansms 60",width = 100,justify = "center").pack()
what()
root.mainloop()
