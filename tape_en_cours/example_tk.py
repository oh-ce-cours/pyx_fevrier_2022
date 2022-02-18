from tkinter import *
from tkinter import ttk

root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=0, row=1)

widget = Tk()
mask = READABLE | WRITABLE
widget.tk.createfilehandler(file, mask, callback)

root.mainloop()
