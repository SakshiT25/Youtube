import tkinter as tk
from tkinter import Message ,Text
from PIL import Image, ImageTk
import pandas as pd
from tkinter import*

import tkinter.ttk as ttk
import tkinter.font as font
import tkinter.messagebox as tm
import matplotlib.pyplot as plt
from tabulate import tabulate

import csv
import numpy as np
from PIL import Image, ImageTk
from tkinter import filedialog
import tkinter.messagebox as tm

import DataProcessing as pre
import ContentBasedCollaborativeFilteringModels as cbcf

bgcolor="#DAF7A6"
bgcolor1="#B7C526"
fgcolor="black"


def clear():
    print("Clear1")
    txt.delete(0, 'end')
    txt1.delete(0, 'end')
    txt3.delete(0, 'end')



window = tk.Tk()
window.title("youtube")

 
window.geometry('1280x720')
window.configure(background=bgcolor)
#window.attributes('-fullscreen', True)

window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)


message1 = tk.Label(window, text="Youtube" ,bg=bgcolor  ,fg=fgcolor  ,width=50  ,height=3,font=('times', 30, 'italic bold underline')) 
message1.place(x=100, y=20)

lbl = tk.Label(window, text="Select Dataset",width=20  ,height=2  ,fg=fgcolor  ,bg=bgcolor ,font=('times', 15, ' bold ') ) 
lbl.place(x=10, y=200)

txt = tk.Entry(window,width=20,bg="white" ,fg="black",font=('times', 15, ' bold '))
txt.place(x=250, y=215)

lbl1 = tk.Label(window, text="Enter Query",width=20  ,height=2  ,fg=fgcolor  ,bg=bgcolor ,font=('times', 15, ' bold ') ) 
lbl1.place(x=10, y=300)

txt1 = tk.Entry(window,width=20,bg="white" ,fg="black",font=('times', 15, ' bold '))
txt1.place(x=250, y=315)


txt3 = Text(window, wrap = WORD,width = 40, height = 12,fg="red",font=('times', 15, ' bold '))


vscroll = Scrollbar(txt3, orient=VERTICAL, command=txt3.yview)
txt3['yscroll'] = vscroll.set

#vscroll.pack(side="right", fill="y")
txt3.pack(side="left", fill="both", expand=True)

txt3.place(x=800, y=150)



#lbl4 = tk.Label(window, text="Notification : ",width=20  ,fg=fgcolor,bg=bgcolor  ,height=2 ,font=('times', 15, ' bold underline ')) 
#lbl4.place(x=100, y=400)

#message = tk.Label(window, text="" ,bg="white"  ,fg="black",width=20  ,height=3, activebackground = bgcolor ,font=('times', 15, ' bold ')) 
#message.place(x=400, y=400)

def browse():
	path=filedialog.askopenfilename()
	print(path)
	txt.insert('end',path)
	if path !="":
		print(path)
	else:
		tm.showinfo("Input error", "Select Dataset")	


def preprocess():
	pre.process()
	tm.showinfo("Input", "Preprocess Successfully Finished")
	
def contentCF():
	sym=txt.get()
	sym1=txt1.get()
	if sym != "" and sym1 !="":

		res=cbcf.process(sym,sym1)
		print(res)
		result=''
		for n in res:
			print(n)
			result=result+"\n"+n
			n = re.sub(r'[^a-zA-Z0-9 ]',r'',n)
			txt3.insert(END,"\n")
			txt3.insert(END,n)
		print(result)
		
		tm.showinfo("Input", "CF Successfully Finished")
	else:
		tm.showinfo("Input error", "Select Dataset and Enter Query")
	

browse = tk.Button(window, text="Browse", command=browse  ,fg=fgcolor  ,bg=bgcolor1  ,width=20  ,height=2, activebackground = "Red" ,font=('times', 15, ' bold '))
browse.place(x=500, y=200)


 
process = tk.Button(window, text="Creat Dataset", command=preprocess  ,fg=fgcolor   ,bg=bgcolor1   ,width=15  ,height=2, activebackground = "Red" ,font=('times', 15, ' bold '))
process.place(x=410, y=600)

cf = tk.Button(window, text="CF", command=contentCF  ,fg=fgcolor   ,bg=bgcolor1   ,width=15  ,height=2, activebackground = "Red" ,font=('times', 15, ' bold '))
cf.place(x=610, y=600)

clearButton = tk.Button(window, text="Clear", command=clear  ,fg=fgcolor  ,bg=bgcolor1  ,width=15  ,height=2 ,activebackground = "Red" ,font=('times', 15, ' bold '))
clearButton.place(x=810, y=600)
 
quitWindow = tk.Button(window, text="Quit", command=window.destroy  ,fg=fgcolor   ,bg=bgcolor1  ,width=15  ,height=2, activebackground = "Red" ,font=('times', 15, ' bold '))
quitWindow.place(x=1020, y=600)

 
window.mainloop()


