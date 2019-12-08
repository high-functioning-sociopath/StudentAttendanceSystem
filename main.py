from tkinter import *
from PIL import Image,ImageTk
from tkintertable import TableCanvas, TableModel
from tkinter import ttk #For combobox
import sys
import keyboard

#Make all the windows global..so that we can use it in other windows as well.



def donothing():
   filewin = Toplevel(logIn)
   button = Button(filewin, text="Do nothing button")
   button.pack()

def exitApp():
	print("Closing...")
	sys.exit(0)

def fetchB(self):
	print("Fetching data from database..")


def viewStats():

	# window.destroy()
	try:
		global stats
		logIn.withdraw()
		# logIn.destroy()
		stats = Tk()

		l_B = Label(stats,text = "Branch")
		l_B.grid(column=0, row=0)
		branch = ttk.Combobox(stats, values=["Electronics", "EXTC","Electrical"],width = 30,height = 30)

		branch.grid(column=0, row=2)
		branch.current(1)

		l_S = Label(stats,text = "Semester")
		l_S.grid(column=10, row=0)
		sem = ttk.Combobox(stats, values=["I", "II","III","IV"],width = 15,height = 25)

		sem.grid(column=10, row=2,padx = 10)
		sem.current(1)

		fetchD = Button(stats, text = "Fetch", width = 15,height = 2, bg = "light grey",fg = "black")
		# fetchD.pack(pady = 28, padx = 40)
		fetchD.grid(column=20, row=0)
		fetchD.bind("<Button-1>",fetchB)	

		# exitB = Button(stats,text = "Exit")
		# exitB.grid(column = 90, row = 2, padx = 10)
		# exitB.bind("<Button-1>",exitApp())
		# comboExample.bind("<<ComboboxSelected>>", callbackFunc)

		stats.geometry('1200x650')	#size of the main frame 
		stats.mainloop()
	except:
		pass


def loggedInWindow():
	# print("Here")
	try:
		global logIn
		#window.withdraw()
		window.destroy()		#https://www.daniweb.com/programming/software-development/threads/243559/need-help-tkinter-hide-window-then-show
		logIn = Tk()
		logIn.title("Faculty- Dipika Ma'am")
		logIn.geometry('1200x650')	#size of the main frame 
		
		

		# b1=Button(logIn,text="STATS",width=40,height=12,bg="light gray",fg="black",font="5",relief=FLAT,overrelief=RIDGE,borderwidth='5',command = print("YO"))
		b1=Button(logIn,text="STATS",width=40,height=12,bg="light gray",fg="black",font="5",relief=FLAT,overrelief=RIDGE,borderwidth='5',command = viewStats)
		b1.place(x=100,y=74)
		# b1.bind("<Button-1>",viewStats())

		b2=Button(logIn,text="REGISTER NEW CLASS",width=40,height=12,bg="light gray",fg="black",font="5",relief=FLAT,overrelief=RIDGE,borderwidth='5')
		b2.place(x=100,y=374)
		# b2.bind("<Button-1>",viewStats())
		b3=Button(logIn,text="NEW ATTENDANCE",width=40,height=12,bg="light gray",fg="black",font="5",relief=FLAT,overrelief=RIDGE,borderwidth='5')
		b3.place(x=730,y=74)
		# b3.bind("<Button-1>",viewStats())
		b4=Button(logIn,text="UPDATE INFO",width=40,height=12,bg="light gray",fg="black",font="5",relief=FLAT,overrelief=RIDGE,borderwidth='5')
		b4.place(x=730,y=374)
		# b4.bind("<Button-1>",viewStats())

		# b1=Button(logIn,text="logout",width=5,bg=gg,fg=gw,command=logIn.destroy)
		# b1.place(x=1210,y=20)
		logIn.mainloop()


	except:
		print("Exception occured.")
		logIn.withdraw()
		window.update()
		window.deiconify()

def mainWindow():

	def onSubmit(self):
		print("Click Click")
		userN = uname.get()
		# print(type(userN))
		userP = pwd.get()
		
		if(userN == "Dipika" and int(userP) == 1234):
			print("Welcome: {} - {}".format(userN,userP))
			loggedInWindow()
				
		else:
			print("Username and Password dont match!")
			l5=Label(window,text="Invalid username/password",bg="yellow",width="50",height="2",font=("Calibri",15))
			l5.pack(pady = 10,padx = 10)
			l5.after(3000,l5.destroy)
			

	global window

	window = Tk()
	window.title("VJTI Attendance App")
	Image_open=Image.open("vjtiIcon.jpg")
	image=ImageTk.PhotoImage(Image_open)
	logo=Label(window,image=image)
	logo.pack(anchor = W,fill = X,expand=NO)
	l1 = Label(window, text="Welcome to VJTI Attendance App", font=("Times Bold", 24),anchor = "center")
	l1.pack(pady = 25,side=TOP, anchor=W, fill=X, expand=NO)
	l1 = Label(window, text="for VJTI'ians by VJTI'ians", font=("Times italic", 8),anchor = "center")
	l1.config(font = ("italic"))
	l1.pack(side=TOP, anchor=W, fill=X, expand=NO)
	l2 = Label(window, text="Please Login to continue", font=("Times Italic", 16),anchor = "center")
	l2.pack( pady = 40, anchor=W,fill = X, expand=NO)
	
	l3 =Label(window, text="Username", font=("Times Bold", 14))
	l3.pack(pady = 10,padx = 10)
	uname = Entry(window)
	uname.pack()

	l4 =Label(window, text="Password", font=("Times Bold", 14))
	l4.pack(pady = 10,padx = 10)
	pwd = Entry(window)
	pwd.pack()

	submit = Button(window, text = "Log in", width = 15,height = 2, bg = "grey",fg = "black")
	submit.pack(pady = 28, padx = 40)
	submit.bind("<Button-1>",onSubmit)		#binded with left button click

	l6 = Label(window, text="Created by: Twisha Shah, Ketaki Mulye, Anusua Roy (DEE)", font=("Times Italic", 10),anchor = "center")
	l6.place(x=100,y=620)

	window.geometry('1200x650')	#size of the main frame 
	window.mainloop()


mainWindow()

# while True:
# 	if keyboard.is_pressed('Esc'):
# 		print("Exiting...")
# 		sys.exit()
# 	mainWindow()



