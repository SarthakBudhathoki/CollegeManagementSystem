from tkinter import *
from tkinter import messagebox

def on_close():
    response=messagebox.askyesno('Exit','Are you sure you want to exit?')
    if response:
        root.destroy()

root=Tk()
root.protocol('WM_DELETE_WINDOW',on_close)

root.mainloop()