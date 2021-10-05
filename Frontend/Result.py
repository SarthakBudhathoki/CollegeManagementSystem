from tkinter import *
from tkinter import ttk
from tkinter import  messagebox
from PIL import Image, ImageTk
import Backend.dbconnection




class Result:
    def __init__(self,project):
        self.project=project
        self.project.title("Result")
        self.project.geometry("1300x458+0+280")
        self.project.focus_force()
        self.db=Backend.dbconnection.Database()
        self.Select_Student = StringVar()
        self.Name = StringVar()
        self.Course = StringVar()
        self.Mark_Obtained = StringVar()
        self.Full_Mark = StringVar()
        self.Roll_Number= StringVar()
        self.Roll_List=[]
        self.fetch_Roll()


        title = Label(self.project, text="Add Student Result", compound=LEFT, font=("goudy old style", 30, "bold"),bg="#363e45", fg="Yellow")
        title.place(x=0, y=0, relwidth=1, height=50)

        self.stu_image = ImageTk.PhotoImage(Image.open("C:/Users/DELL/PycharmProjects/pythonProject26/image/examresult.jpg"))
        # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Title <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
        title = Label(self.project, image=self.stu_image, font=("goudy old style", 30, "bold"),bg="#0af0e8",fg="blue")
        title.place(x=600,y=80,height=325,width=600)

        selectstudent_name_label = Label(self.project, text="Select Student", font=("goudy old style", 15, "bold"), fg="#7307f7")
        selectstudent_name_label.place(x=0, y=75)

        self.stw_search_combobox = ttk.Combobox(self.project,textvar=self.Roll_Number,values=self.Roll_List, font=("calibri light", 12), width=12)
        self.stw_search_combobox.place(x=140, y=80,width=150)
        self.stw_search_combobox.set("Select")



        name_name_label = Label(self.project, text="Name", font=("goudy old style", 15, "bold"),fg="#7307f7")
        name_name_label.place(x=0, y=120)

        self.name_entry = Entry(self.project,textvar=self.Name, font=("goudy old style", 15, "bold"), bg="white").place(x=140,y=125)

        course_name_label = Label(self.project, text="Course", font=("goudy old style", 15, "bold"), fg="#7307f7")
        course_name_label.place(x=0, y=160)

        self.course_entry = Entry(self.project,textvar=self.Course, font=("goudy old style", 15, "bold"), bg="white").place(x=140, y=165)

        mark_name_label = Label(self.project, text="Mark Obtained", font=("goudy old style", 15, "bold"), fg="#7307f7")
        mark_name_label.place(x=0, y=200)

        self.mark_entry = Entry(self.project,textvar=self.Mark_Obtained, font=("goudy old style", 15, "bold"), bg="white").place(x=140, y=205)

        fullmark_name_label = Label(self.project, text="Full Marks", font=("goudy old style", 15, "bold"), fg="#7307f7")
        fullmark_name_label.place(x=0, y=240)

        self.fullmark_entry = Entry(self.project,textvar=self.Full_Mark, font=("goudy old style", 15, "bold"), bg="white").place(x=140, y=245)

        self.btn_clear = Button(self.project, text="Clear",command=self.clear, font=("times new roman", 15), bg="Gray", fg="white")
        self.btn_clear.place(x=260, y=300,width=80)


        self.btn_submit = Button(self.project, text="Submit",command=self.submit, font=("times new roman", 15), bg="green", fg="white")
        self.btn_submit.place(x=140, y=300,width=100)

        self.btn_search = Button(self.project, text="Search",command=self.search, font=("times new roman", 15), bg="#0BBDF9", fg="white",activeforeground="#0bf207", activebackground="#f1f507")
        self.btn_search.place(x=350, y=80, height=30, width=200)

    def fetch_Roll(self):
        query="select roll from student "
        row=self.db.fetch_all(query)
        if len(row)>0:
            for data in row:
                self.Roll_List.append(data[0])

    def search(self):
        try:
            query="select name , select_gender from student where roll=%s"
            values=(self.Roll_Number.get(),)
            data=self.db.fetch(query,values)
            if len(data)!=0:
                self.Name.set(data[0])
                self.Course.set(data[1])
            else:
                messagebox.showerror("Error","No record found",parent=self.project)
        except Exception as exe:
            messagebox.showerror("Error", f"Error due to: {str(exe)}", parent=self.project)

    def submit(self):
        try:
            if self.Name.get()=="":
                messagebox.showerror("Error","Please first search the student record")
            else:
                query="select * from reult where roll=%s and course=%s "
                value=(self.Roll_Number.get(),self.Course.get())
                data=self.db.fetch(query,value)
                if data != None:
                    messagebox.showerror("Error","Result already present")
                else:
                    per=(int(self.Mark_Obtained.get())*100)/int(self.Full_Mark.get())
                    q1="Insert into reult(roll,name,course,mark_obtained,full_mark,percentage) values(%s,%s,%s,%s,%s,%s)"
                    v1=(self.Roll_Number.get(),self.Name.get(),self.Course.get(),self.Mark_Obtained.get(),self.Full_Mark.get(),str(per))
                    self.db.add(q1,v1)
                    messagebox.showinfo("sucess","Result Submitted Sucessfully")
        except Exception as exe:
         messagebox.showerror("Error", f"Error due to: {str(exe)}", parent=self.project)

    def clear(self):
        self.Name.set("")
        self.Course.set("")
        self.Mark_Obtained.set("")
        self.Full_Mark.set("")





if __name__=="__main__":
    tk=Tk()
    obj=Result(tk)

    tk.mainloop()
