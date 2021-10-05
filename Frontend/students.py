from tkinter import *
from tkinter import ttk
from tkinter import  messagebox
from PIL import Image, ImageTk
import  Backend.dbconnection


class Student:
    def __init__(self,project):
        self.project=project
        self.project.title("Student")
        self.project.geometry("1300x498+0+280")
        self.project.focus_force()
        self.db=Backend.dbconnection.Database()
        self.StudentID=IntVar()
        self.Roll= StringVar()
        self.Name = StringVar()
        self.Email = StringVar()
        self.Gender= StringVar()
        self.State = StringVar()
        self.Address = StringVar()
        self.DOB = StringVar()
        self.Contact = StringVar()
        self.SelectCourse = StringVar()
        self.Addmission = StringVar()
        self.City = StringVar()
        self.PinCode = StringVar()

        #>>>>>>>>>>>>>>>>> Title >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

        title = Label(self.project, text="Student Details", compound=LEFT,font=("goudy old style", 30, "bold"), bg="#363e45", fg="Yellow")
        title.place(x=0, y=0, relwidth=1, height=50)

        studentid_name_label = Label(self.project, text="StudentID", font=("goudy old style", 15, "bold"), fg="#7307f7")
        studentid_name_label.place(x=0, y=290)

        self.studendid_entry = Entry(self.project, textvar=self.StudentID, font=("goudy old style", 15, "bold"), bg="white").place(x=90, y=290)

        rollnumber_name_label = Label(self.project, text="Roll No.", font=("goudy old style", 15, "bold"), fg="#7307f7")
        rollnumber_name_label.place(x=0, y=80)

        self.rollnumber_entry = Entry(self.project, textvar=self.Roll,font=("goudy old style", 15, "bold"), bg="white").place(x=90,y=83)

        name_name_label = Label(self.project, text="Name", font=("goudy old style", 15, "bold"), fg="#7307f7")
        name_name_label.place(x=0, y=112)

        self.name_entry = Entry(self.project,textvar=self.Name, font=("goudy old style", 15, "bold"), bg="white").place(x=90, y=117)

        email_name_label = Label(self.project, text="Email", font=("goudy old style", 15, "bold"), fg="#7307f7")
        email_name_label.place(x=0, y=140)

        self.email_entry = Entry(self.project,textvar=self.Email, font=("goudy old style", 15, "bold"), bg="white").place(x=90, y=150)

        gender_name_label = Label(self.project, text="Gender", font=("goudy old style", 15, "bold"), fg="#7307f7")
        gender_name_label.place(x=0, y=180)

        self.gender_entry = Entry(self.project,textvar=self.Gender, font=("goudy old style", 15, "bold"), bg="white").place(x=90, y=182)

        state_name_label = Label(self.project, text="State", font=("goudy old style", 15, "bold"), fg="#7307f7")
        state_name_label.place(x=0, y=220)

        self.state_entry = Entry(self.project,textvar=self.State, font=("goudy old style", 15, "bold"), bg="white").place(x=90, y=217,width=170)

        address_name_label = Label(self.project, text="Address", font=("goudy old style", 15, "bold"), fg="#7307f7")
        address_name_label.place(x=0, y=260)

        self.address_entry = Entry(self.project,textvar=self.Address, font=("goudy old style", 15, "bold"), bg="white").place(x=90, y=251)

        date_name_label = Label(self.project, text="D.O.B(dd-mm-yyyy)", font=("goudy old style", 15, "bold"), fg="#7307f7")
        date_name_label.place(x=300, y=85)

        self.date_entry = Entry(self.project,textvar=self.DOB,font=("goudy old style", 15, "bold"), bg="white").place(x=480, y=85)

        contact_name_label = Label(self.project, text="Contact", font=("goudy old style", 15, "bold"),fg="#7307f7")
        contact_name_label.place(x=300, y=117)

        self.contact_entry = Entry(self.project,textvar=self.Contact, font=("goudy old style", 15, "bold"), bg="white").place(x=480, y=119)

        selectcourse_name_label = Label(self.project, text="Select Course", font=("goudy old style", 15, "bold"),fg="#7307f7")
        selectcourse_name_label.place(x=300, y=149)

        self.selectcourse_entry = Entry(self.project,textvar=self.SelectCourse, font=("goudy old style", 15, "bold"), bg="white").place(x=480, y=153)

        addmission_name_label = Label(self.project, text="Addmission Date", font=("goudy old style", 15, "bold"),fg="#7307f7")
        addmission_name_label.place(x=300, y=181)

        self.addmission_entry = Entry(self.project,textvar=self.Addmission, font=("goudy old style", 15, "bold"), bg="white").place(x=480, y=185)

        city_name_label = Label(self.project, text="City", font=("goudy old style", 15, "bold"), fg="#7307f7")
        city_name_label.place(x=230, y=215)

        self.city_entry = Entry(self.project,textvar=self.City, font=("goudy old style", 15, "bold"), bg="white").place(x=270,y=219,width=170)

        pin_name_label = Label(self.project, text="Pin Code", font=("goudy old style", 15, "bold"), fg="#7307f7")
        pin_name_label.place(x=400, y=215)

        self.pin_entry = Entry(self.project,textvar=self.PinCode, font=("goudy old style", 15, "bold"), bg="white").place(x=500, y=219, width=185)

        self.mainframe = Frame(self.project, bg="white", bd=4, relief="groove")
        self.mainframe.place(x=690, y=55, height=310, width=580)

        self.btn_clear = Button(self.project, text="Clear",command=self.clear, font=("times new roman", 15), bg="Gray",fg="white")
        self.btn_clear.place(x=395, y=325, height=30, width=120)
        #
        self.btn_update = Button(self.project, text="Update",command=self.update, font=("times new roman", 15),bg="Gray", fg="white")
        self.btn_update.place(x=135, y=325, height=30, width=120)

        self.btn_delete = Button(self.project, text="Delete",command=self.delete,  font=("times new roman", 15),bg="Gray", fg="white")
        self.btn_delete.place(x=265, y=325, height=30, width=120)

        self.btn_add = Button(self.project, text="Add",command=self.add, font=("times new roman", 15), bg="Gray",fg="white")
        self.btn_add.place(x=5, y=325, height=30, width=120)

        scroll_x = Scrollbar(self.mainframe, orient=HORIZONTAL)
        scroll_y = Scrollbar(self.mainframe, orient=VERTICAL)
        self.student_table = ttk.Treeview(self.mainframe, columns=(
           'StudentID','Roll No.','Name','Email','Gender','State','D.O.B(dd-mm-yy)','Contact','Select Course','Addmission','City','Pin Code','Address'),
                                         xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)
        self.student_table.heading('StudentID', text='StudentID')
        self.student_table.heading('Roll No.', text='Roll No.')
        self.student_table.heading('Name', text='Name')
        self.student_table.heading('Email', text='Email')
        self.student_table.heading('Gender', text='Gender')
        self.student_table.heading('State', text='State')
        self.student_table.heading('D.O.B(dd-mm-yy)', text='D.O.B(dd-mm-yy)')
        self.student_table.heading('Contact', text='Contact')
        self.student_table.heading('Select Course', text='Select Course')
        self.student_table.heading('Addmission', text='Addmission')
        self.student_table.heading('City', text='City')
        self.student_table.heading('Pin Code', text='Pin Code')
        self.student_table.heading('Address', text='Address')

        self.student_table['show'] = 'headings'
        self.student_table.pack(fill=BOTH, expand=TRUE)
        self.student_table.pack()
        self.student_table.bind("<ButtonRelease-1>", self.cursor)
        self.fetchdata()

    def add(self):
        StudentID=self.StudentID.get()
        Roll=self.Roll.get()
        Name=self.Name.get()
        Email=self.Email.get()
        Gender=self.Gender.get()
        State=self.State.get()
        Address=self.Address.get()
        DOB=self.DOB.get()
        Contact=self.Contact.get()
        SelectCourse=self.SelectCourse.get()
        Addmission=self.Addmission.get()
        City=self.City.get()
        PinCode=self.PinCode.get()

        if   Roll=='' or Name=='' or Email=='' or Gender=='' or State=='' or Address=='' or DOB=='' or Contact==''or  SelectCourse=='' or  Addmission=='' or City=='' or PinCode=='' :
            messagebox.showerror("Error" , "All field are required to add data")
        else:
            query=" select * from student where student_id=%s or name=%s "
            values=(StudentID,Name)
            rows=self.db.fetch(query,values)
        if rows != None:
            messagebox.showerror("Error", "student name is already present",parent=self.project)
        else:
            q1="Insert into student(student_id,roll,name,email,gender,state,dob,contact,select_gender,addmission,city,pin_code,address)values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            values=(StudentID,Roll,Name,Email,Gender,State,DOB,Contact,SelectCourse,Addmission,City,PinCode,Address)
            self.db.add(q1,values)
            self.fetchdata()
            messagebox.showinfo("Sucess","Data added sucessfully")

    def fetchdata(self):
        query="select * from student "
        data=self.db.fetch_all(query)
        if len(data) != 0:
            self.student_table.delete(*self.student_table.get_children())
        for rows in data:
            self.student_table.insert('',END, value=rows)

    def cursor(self,a):
        coursor_rows = self.student_table.focus()
        data = self.student_table.item(coursor_rows)
        row = data['values']
        self.StudentID.set(row[0])
        self.Roll.set(row[1])
        self.Name.set(row[2])
        self.Email.set(row[3])
        self.Gender.set(row[4])
        self.State.set(row[5])
        self.DOB.set(row[6])
        self.Contact.set(row[7])
        self.SelectCourse.set(row[8])
        self.Addmission.set(row[9])
        self.City.set(row[10])
        self.PinCode.set(row[11])
        self.Address.set(row[12])

    def update(self):
        StudentID = self.StudentID.get()
        Roll = self.Roll.get()
        Name = self.Name.get()
        Email = self.Email.get()
        Gender = self.Gender.get()
        State = self.State.get()
        DOB = self.DOB.get()
        Contact = self.Contact.get()
        SelectCourse = self.SelectCourse.get()
        Addmission = self.Addmission.get()
        City = self.City.get()
        PinCode = self.PinCode.get()
        Address = self.Address.get()
        query="update student set  roll=%s, name=%s, email=%s, gender=%s, state=%s, dob=%s, contact=%s, select_gender=%s, addmission=%s, city=%s, pin_code=%s, address=%s where student_id=%s"
        value=(Roll,Name,Email,Gender,State,DOB,Contact,SelectCourse,Addmission,City,PinCode,Address,StudentID)
        self.db.update(query,value)
        messagebox.showinfo("sucess","data update sucessfully")
        self.fetchdata()

    def delete(self):
        student_id= self.StudentID.get()
        query="delete from student where student_id=%s"
        value=(student_id,)
        self.db.delete(query,value)
        messagebox.showinfo("sucess","data delete sucessfully")
        self.fetchdata()

    def clear(self):
        self.StudentID.set("")
        self.Roll.set("")
        self.Name.set("")
        self.Email.set("")
        self.Gender.set("")
        self.State.set("")
        self.Address.set("")
        self.DOB.set("")
        self.Contact.set("")
        self.SelectCourse.set("")
        self.Addmission.set("")
        self.City.set("")
        self.PinCode.set("")





if __name__=="__main__":
    tk=Tk()
    obj=Student(tk)
    tk.mainloop()
