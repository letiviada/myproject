#!/usr/local/bin/python3
import tkinter as tk
import random

def roll():
    x=random.randint(1,6)
    lbl["text"]=f'''{x}'''

window=tk.Tk()
window.title("Roll a six-sided die")
window.columnconfigure(0,minsize=250,weight=1)
window.rowconfigure([0,1],minsize=50,weight=1)

btn=tk.Button(master=window, text="Roll",command=roll)
btn.grid(row=0,column=0,sticky="nsew")

lbl=tk.Label(master=window, text="1")
lbl.grid(row=1,column=0,sticky="nsew")

window.mainloop()
