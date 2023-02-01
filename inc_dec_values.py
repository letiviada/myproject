import tkinter as tk

def increase():
    value=int(lbl["text"])
    lbl["text"]=f"{value+1}"

def decrease():
    value=int(lbl["text"])
    lbl["text"]=f"{value-1}"

window=tk.Tk()
window.title("Dice")
window.rowconfigure(0,minsize=50,weight=1)
window.columnconfigure([0,1,2], minsize=50,weight=1)

btn_minus=tk.Button(master=window, relief=tk.RAISED, text="-", command=decrease)
btn_minus.grid(row=0,column=0,sticky="nsew")

lbl=tk.Label(master=window,text="0")
lbl.grid(row=0,column=1,sticky="nsew")

btn_plus=tk.Button(master=window,relief=tk.RAISED, text="+",command=increase)
btn_plus.grid(row=0,column=2,sticky="nsew")

window.mainloop()
