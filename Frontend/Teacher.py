from tkinter import *
from tkinter import ttk
from tkinter import  messagebox
from PIL import Image, ImageTk
import Backend.dbconnection

class Teacher:
    def __init__(self,project):
        self.project=project
        self.project.title("Teacher")
        self.project.geometry("1300x498+0+280")
        self.project.focus_force()

        title = Label(self.project, text="Teacher Details", compound=LEFT, font=("goudy old style", 30, "bold"),
                      bg="#363e45", fg="Yellow")

        title.place(x=0, y=0, relwidth=1, height=50)



        self.mainframe = Frame(self.project, bg="white", bd=4, relief="groove")
        self.mainframe.place(x=690, y=55, height=310, width=580)

        self.btn_clear = Button(self.project, text="Clear",  font=("times new roman", 15), bg="Gray",
                                fg="white")
        self.btn_clear.place(x=395, y=400, height=30, width=120)
        #
        self.btn_update = Button(self.project, text="Update",  font=("times new roman", 15),
                                 bg="Gray", fg="white")
        self.btn_update.place(x=135, y=400, height=30, width=120)

        self.btn_delete = Button(self.project, text="Delete",  font=("times new roman", 15),
                                 bg="Gray", fg="white")
        self.btn_delete.place(x=265, y=400, height=30, width=120)

        self.btn_add = Button(self.project, text="Add", font=("times new roman", 15), bg="Gray",
                              fg="white")
        self.btn_add.place(x=5, y=400, height=30, width=120)


        scroll_x = Scrollbar(self.mainframe, orient=HORIZONTAL)
        scroll_y = Scrollbar(self.mainframe, orient=VERTICAL)
        self.course_table = ttk.Treeview(self.mainframe, columns=(
            ),
                                         xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.course_table.xview)
        scroll_y.config(command=self.course_table.yview)


if __name__=="__main__":
    tk=Tk()
    obj=Teacher(tk)
    tk.mainloop()
