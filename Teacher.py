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

        self.btn_clear = Button(self.project, text="Clear", font=("times new roman", 15), bg="Gray",
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

        id_name_label = Label(self.project, text="ID", font=("goudy old style", 15, "bold"), fg="#7307f7")
        id_name_label.place(x=0, y=80)

        self.id_entry = Entry(self.project,  font=("goudy old style", 15, "bold"),
                              bg="white").place(x=90, y=83)

        name_name_label = Label(self.project, text="Name", font=("goudy old style", 15, "bold"), fg="#7307f7")
        name_name_label.place(x=0, y=112)

        self.name_entry = Entry(self.project, font=("goudy old style", 15, "bold"),
                                bg="white").place(x=90, y=117)

        address_name_label = Label(self.project, text="Address", font=("goudy old style", 15, "bold"), fg="#7307f7")
        address_name_label.place(x=0, y=150)

        self.address_entry = Entry(self.project,  font=("goudy old style", 15, "bold"),
                                   bg="white").place(x=90, y=150)

        #
        # mobile_name_label = Label(self.project, text="Mobile No.", font=("goudy old style", 15, "bold"), fg="#7307f7")
        # mobile_name_label.place(x=0, y=180)
        #
        # self.mobile_entry = Entry(self.project,  font=("goudy old style", 15, "bold"),
        #                           bg="white").place(x=90, y=182)

        # state_name_label = Label(self.project, text="State", font=("goudy old style", 15, "bold"), fg="#7307f7")
        # state_name_label.place(x=0, y=220)
        #
        # self.state_entry = Entry(self.project,  font=("goudy old style", 15, "bold"),
        #                          bg="white").place(x=90, y=217)

        subject_name_label = Label(self.project, text="Subject Taught", font=("goudy old style", 15, "bold"),
                                  fg="#7307f7")
        subject_name_label.place(x=300, y=85)

        self.subject_entry = Entry(self.project,  font=("goudy old style", 15, "bold"),
                                  bg="white").place(
            x=480, y=85)

        bookauthur_name_label = Label(self.project, text="Contact N0.", font=("goudy old style", 15, "bold"),
                                      fg="#7307f7")
        bookauthur_name_label.place(x=300, y=117)

        self.bookauthur_entry = Entry(self.project,  font=("goudy old style", 15, "bold"),
                                      bg="white").place(x=480, y=119)

        booktitle_name_label = Label(self.project, text="Description", font=("goudy old style", 15, "bold"),
                                     fg="#7307f7")
        booktitle_name_label.place(x=300, y=149)

        self.booktitle_entry = Entry(self.project,  font=("goudy old style", 15, "bold"),
                                     bg="white").place(x=480, y=153)

        # dateborrow_name_label = Label(self.project, text=" Date Borrow", font=("goudy old style", 15, "bold"),
        #                               fg="#7307f7")
        # dateborrow_name_label.place(x=300, y=181)
        #
        # self.dateborrow_entry = Entry(self.project,  font=("goudy old style", 15, "bold"),
        #                               bg="white").place(x=480, y=185)
        #
        # duedate_label = Label(self.project, text="Due Date", font=("goudy old style", 15, "bold"), fg="#7307f7")
        # duedate_label.place(x=300, y=215)
        #
        # self.duedate_entry = Entry(self.project,  font=("goudy old style", 15, "bold"),
        #                            bg="white").place(x=480, y=219)

        scroll_x = Scrollbar(self.mainframe, orient=HORIZONTAL)
        scroll_y = Scrollbar(self.mainframe, orient=VERTICAL)
        self.course_table = ttk.Treeview(self.mainframe, columns=(
            ' Id', ' Name', 'Address', 'Subject Taught', 'Contact',  'Description'),
                                         xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.course_table.xview)
        scroll_y.config(command=self.course_table.yview)
        self.course_table.heading(' Id', text=' Id')
        self.course_table.heading(' Name', text=' Name')
        self.course_table.heading('Address', text='Address')
        self.course_table.heading('Subject Taught', text='Subject Taught')
        self.course_table.heading('Contact', text='Contact')
        self.course_table.heading('Description', text='Description')
        self.course_table['show'] = 'headings'
        self.course_table.pack(fill=BOTH, expand=TRUE)
        self.course_table.pack()

if __name__=="__main__":
    tk=Tk()
    obj=Teacher(tk)
    tk.mainloop()
