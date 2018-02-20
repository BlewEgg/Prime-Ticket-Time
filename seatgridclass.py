from tkinter import *


def seats():

	var = IntVar()

	row = int(input('Enter number of rows: '))
	column = int(input('Enter number of columns: '))
	buttonnumber= row * column
	buttonlist = [0] *buttonnumber
	currentbutton = 1

	rowlist= ['A','B','C','D', 'E', 'F', 'G', 'H','I', 'J', 'K', 'L', 'M']
	columnlist= ['1','2','3','4','5','6','7','8' '9', '10', '11', '12']

	rowlabels = [0] * row
	rnum=0
	columnlabels = [0] * column
	colnum=0

	purchasedseats = [8, 5, 1, 13]
	seatvalues = [IntVar()] * buttonnumber

	def printseat():
		for i in range(0, buttonnumber):
			print(seatvalues[i].get())

	for r in range(0,row):
		rowlabels[rnum] = StringVar()
		label = Label( root, textvariable=rowlabels[rnum],)

		rowlabels[rnum].set(rowlist[rnum])
		label.grid(row=rnum+1, column=0)
		rnum+=1

	for c in range(0,column):
		columnlabels[colnum] = StringVar()
		label = Label( root, textvariable=columnlabels[colnum],)

		columnlabels[colnum].set(columnlist[colnum])
		label.grid(row=0, column=colnum+1)
		colnum+=1

	for i in range (0+1,row+1):
		for x in range(0+1,column+1):

			if currentbutton in purchasedseats:
				buttonlist[currentbutton-1] = Checkbutton(root, text="", variable=currentbutton,onvalue = 1, offvalue= 0, state=DISABLED, highlightcolor='orange')
			else:
				buttonlist[currentbutton-1] = Checkbutton(root, text="", variable=seatvalues[currentbutton-1],onvalue = currentbutton, offvalue= 0, selectcolor='#000fff000', command =printseat)

		

			buttonlist[currentbutton-1].grid(row=i, column=x )
			currentbutton += 1

	label = Label(root)

