from tkinter import *
from tkinter import ttk
import time


def mon_callback():
    print("avant")
    time.sleep(50)
    print("je suis cliqué")


root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
ttk.Button(frm, text="Quit", command=mon_callback).grid(column=0, row=1)

# widget = Tk()
# mask = READABLE | WRITABLE
# widget.tk.createfilehandler(file, mask, callback)

root.mainloop()
