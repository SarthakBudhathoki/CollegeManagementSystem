from tkinter import *
from tkinter import ttk
from tkinter import  messagebox
from PIL import Image, ImageTk
import Backend.dbconnection


class ViewResult:
    def __init__(self,project):
        self.project=project
        self.project.title("View Result")
        self.project.geometry("1300x458+0+280")
        self.project.focus_force()
        self.obj=Backend.dbconnection.Database()
        self.search = StringVar()
        self.Id=""

        title = Label(self.project, text="View Student Results", compound=LEFT, font=("goudy old style", 30, "bold"),bg="#363e45", fg="Yellow")
        title.place(x=0, y=0, relwidth=1, height=50)

        search_name_label = Label(self.project, text="Search By | Roll N0. ", font=("goudy old style", 15, "bold"),fg="#7307f7")
        search_name_label.place(x=10, y=80)

        self.search_entry = Entry(self.project,textvar=self.search, font=("goudy old style", 15, "bold"), bg="white").place(x=200,y=83)

        self.btn_search = Button(self.project, text="Search",command=self.Search, font=("times new roman", 15),bg="#0BBDF9", fg="white", activeforeground="#0bf207", activebackground="#f1f507")
        self.btn_search.place(x=420, y=80, height=30, width=200)

        self.btn_delete = Button(self.project, text="Delete",command=self.delete, font=("times new roman", 15), bg="#0BBDF9", fg="white",activeforeground="#0bf207", activebackground="#f1f507")
        self.btn_delete.place(x=650, y=80, height=30, width=200)

        self.btn_clear = Button(self.project, text="Clear", font=("times new roman", 15), bg="Gray", fg="white")
        self.btn_clear.place(x=880, y=80, height=30, width=200)


        self.mainframe = Frame(self.project, bg="white", bd=4, relief="groove")
        self.mainframe.place(x=30, y=130, height=240, width=1050)

        scroll_x = Scrollbar(self.mainframe, orient=HORIZONTAL)
        scroll_y = Scrollbar(self.mainframe, orient=VERTICAL)
        self.result_table = ttk.Treeview(self.mainframe, columns=(
            'Result ID', 'Roll Number', 'Name','Course', 'Mark Obtained', 'Full Mark', 'Percentage'),
                                         xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.result_table.xview)
        scroll_y.config(command=self.result_table.yview)
        self.result_table.heading('Result ID', text='Result ID')
        self.result_table.heading('Roll Number', text='Roll Number')
        self.result_table.heading('Name', text='Name')
        self.result_table.heading('Course', text='Course')
        self.result_table.heading('Mark Obtained', text='Mark Obtained')
        self.result_table.heading('Full Mark', text='Full Mark')
        self.result_table.heading('Percentage', text='Percentage')
        self.result_table['show'] = 'headings'
        self.result_table.pack(fill=BOTH, expand=TRUE)
        self.result_table.pack()


    def Search(self):
      try:
        if self.search.get()=="":
            messagebox.showerror("Error","Roll NUmber must be required")
        else:
                query="select * from reult where roll=%s "
                value=(self.search.get(),)
                row=self.obj.fetch(query,value)

                if row!=None:
                    self.result_table.delete(*self.result_table.get_children())
                    self.result_table.insert('', END, value=row)
                     #messagebox.showerror("Error","Invalid roll number",parent=self.project)
                else:
                    messagebox.showerror("Error", "Record no found", parent=self.project)

      except Exception as exe:
         messagebox.showerror("Error", f"Error due to: {str(exe)}", parent=self.project)

    def delete(self):
        selected_items = self.result_table.selection()[0]
        uid = self.result_table.item(selected_items)['values'][0]
        query = "delete from reult where rid=%s"
        values = (uid,)
        self.obj.delete(query, values)
        self.result_table.delete(selected_items)
        messagebox.showinfo("success", "data deleted successfully")



if __name__=="__main__":
    tk=Tk()
    obj=ViewResult(tk)

    tk.mainloop()
