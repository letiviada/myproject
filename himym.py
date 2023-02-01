#!/usr/local/bin/python3
import tkinter as tk
import webbrowser
import random

def roll():
    x=random.randint(1,9)
    lbl["text"]='{x=}'
    if x<=2:
        y=random.randint(1,22)
        lbl2["text"]='{y}'
    elif x==3:
        y=random.randint(1,20)
        lbl2["text"]='{y}'
    else:
        y=random.randint(1,24)
        lbl2["text"]='{y}'
def open_browser():
    webbrowser.open_new("https://www.disneyplus.com/en-gb/series/how-i-met-your-mother/3kpBeRQiKjkq")

window=tk.Tk()
window.title("How I met your mother")
window.columnconfigure([0,1],minsize=250,weight=1)
window.rowconfigure([0,1],minsize=50,weight=1)

btn=tk.Button(master=window, text="How I met your mother",command=roll)
btn.grid(row=0,column=0,sticky="nsew")
btn2=tk.Button(master=window, text="Disney",command=open_browser)
btn2.grid(row=0,column=1,sticky="nsew")
lbl=tk.Label(master=window, text="Season")
lbl2=tk.Label(master=window, text="Episode")
lbl.grid(row=1,column=0,sticky="nsew")
lbl2.grid(row=1,column=1,sticky="nsew")

window.mainloop()
