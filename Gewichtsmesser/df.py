
from distutils import command
from tkinter import *
import tkinter.font as tkfont

master = Tk()
master.geometry('250x250')
überschrift_style = tkfont.Font(family='Helvetica', size=28)
text_style =tkfont.Font(family = 'Helvetica', size=20)

def var_states(self):
    self.wert1 = var1.get()
    self.wert2 = var2.get()
    wert1_int = int(wert1)
    wert2_int = int(wert2)
    zahl = Entry.get()
    zahl_int = int(zahl)
    if wert1_int == 1:
       print(zahl_int * 1000)
    elif wert2_int == 1:
        print(zahl_int / 1000)

    


text = Label(master, font = überschrift_style ,text="Umrechner:").grid(row=0, sticky=W)
var1 = IntVar()
kg_in_g = Checkbutton(master, font = text_style, text="kg zu g", variable=var1).grid(row=1, sticky=W)
var2 = IntVar()
g_in_kg = Checkbutton(master, font = text_style, text="g zu kg", variable=var2).grid(row=2, sticky=W)
eingabe = Entry(master).grid(row=3, sticky=W)
Button(master, text='Quit', command=master.quit).grid(row=5, sticky=W, pady=4)
Button(master, text='Show', command=var_states).grid(row=4, sticky=W, pady=4)
mainloop()



