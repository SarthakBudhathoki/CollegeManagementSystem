from tkinter import *
from tkinter import ttk
from tkinter import  messagebox
from PIL import Image, ImageTk
import Backend.dbconnection


class Library:
    def __init__(self,project):
        self.project=project
        self.project.title("Library")
        self.project.geometry("1300x498+0+280")
        self.project.focus_force()
        self.db = Backend.dbconnection.Database()
        self.ID = IntVar()
        self.Name = StringVar()
        self.Address = StringVar()
        self.Mobile_No = StringVar()
        self.Member_Type = StringVar()
        self.Book_Id = StringVar()
        self.Book_Authur = StringVar()
        self.Book_Title = StringVar()
        self.Date_Borrow = StringVar()
        self.Due_Date = StringVar()


        title = Label(self.project, text="Library", compound=LEFT, font=("goudy old style", 30, "bold"),
                      bg="#363e45", fg="Yellow")

        title.place(x=0, y=0, relwidth=1, height=50)


        self.mainframe = Frame(self.project, bg="white", bd=4, relief="groove")
        self.mainframe.place(x=690, y=55, height=310, width=580)

        self.btn_clear = Button(self.project,command=self.clear, text="Clear",  font=("times new roman", 15), bg="Gray",
                                fg="white")
        self.btn_clear.place(x=395, y=325, height=30, width=120)
        #
        self.btn_update = Button(self.project,command=self.update, text="Update",  font=("times new roman", 15),
                                 bg="Gray", fg="white")
        self.btn_update.place(x=135, y=325, height=30, width=120)

        self.btn_delete = Button(self.project,command=self.delete, text="Delete",  font=("times new roman", 15),
                                 bg="Gray", fg="white")
        self.btn_delete.place(x=265, y=325, height=30, width=120)

        self.btn_add = Button(self.project,command=self.add_library, text="Add", font=("times new roman", 15), bg="Gray",
                              fg="white")
        self.btn_add.place(x=5, y=325, height=30, width=120)

        id_name_label = Label(self.project, text="ID", font=("goudy old style", 15, "bold"), fg="#7307f7")
        id_name_label.place(x=0, y=80)

        self.id_entry = Entry(self.project,textvar=self.ID,  font=("goudy old style", 15, "bold"),
                                     bg="white").place(x=90, y=83)


        name_name_label = Label(self.project, text="Name", font=("goudy old style", 15, "bold"), fg="#7307f7")
        name_name_label.place(x=0, y=112)

        self.name_entry = Entry(self.project,textvar=self.Name,  font=("goudy old style", 15, "bold"),
                                bg="white").place(x=90, y=117)

        address_name_label = Label(self.project, text="Address", font=("goudy old style", 15, "bold"), fg="#7307f7")
        address_name_label.place(x=0, y=150)

        self.address_entry = Entry(self.project,textvar=self.Address,  font=("goudy old style", 15, "bold"),
                                 bg="white").place(x=90, y=150)

        mobile_name_label = Label(self.project, text="Mobile No.", font=("goudy old style", 15, "bold"), fg="#7307f7")
        mobile_name_label.place(x=0, y=180)

        self.mobile_entry = Entry(self.project,textvar=self.Mobile_No,  font=("goudy old style", 15, "bold"),
                                  bg="white").place(x=90, y=182)

        # state_name_label = Label(self.project, text="State", font=("goudy old style", 15, "bold"), fg="#7307f7")
        # state_name_label.place(x=0, y=220)
        #
        # self.state_entry = Entry(self.project,  font=("goudy old style", 15, "bold"),
        #                          bg="white").place(x=90, y=217)



        bookid_name_label = Label(self.project, text="Book Id", font=("goudy old style", 15, "bold"),
                                fg="#7307f7")
        bookid_name_label.place(x=300, y=85)

        self.bookid_entry = Entry(self.project,textvar=self.Book_Id,  font=("goudy old style", 15, "bold"), bg="white").place(
            x=480, y=85)

        bookauthur_name_label = Label(self.project, text="Book Authur", font=("goudy old style", 15, "bold"), fg="#7307f7")
        bookauthur_name_label.place(x=300, y=117)

        self.bookauthur_entry = Entry(self.project,textvar=self.Book_Authur,  font=("goudy old style", 15, "bold"),
                                   bg="white").place(x=480, y=119)

        booktitle_name_label = Label(self.project, text="Book Title", font=("goudy old style", 15, "bold"),
                                        fg="#7307f7")
        booktitle_name_label.place(x=300, y=149)

        self.booktitle_entry = Entry(self.project,textvar=self.Book_Title, font=("goudy old style", 15, "bold"),
                                        bg="white").place(x=480, y=153)

        dateborrow_name_label = Label(self.project, text=" Date Borrow", font=("goudy old style", 15, "bold"),
                                      fg="#7307f7")
        dateborrow_name_label.place(x=300, y=181)

        self.dateborrow_entry = Entry(self.project,textvar=self.Date_Borrow,  font=("goudy old style", 15, "bold"),
                                      bg="white").place(x=480, y=185)



        duedate_label = Label(self.project, text="Due Date", font=("goudy old style", 15, "bold"), fg="#7307f7")
        duedate_label.place(x=300, y=215)

        self.duedate_entry = Entry(self.project,textvar=self.Due_Date,  font=("goudy old style", 15, "bold"),
                               bg="white").place(x=480, y=219)

        member_name_label = Label(self.project, text="Member Type", font=("goudy old style", 15, "bold"), fg="#7307f7")
        member_name_label.place(x=0, y=260)

        # self.stw_search_combobox = ttk.Combobox(self.project,value=('Student','Teacher','Staff'),   font=("calibri light", 12), width=12)
        # self.stw_search_combobox.place(x=140, y=260, width=150)
        # self.stw_search_combobox.set("Select")

        self.member_entry = Entry(self.project,textvar=self.Member_Type,  font=("goudy old style", 15, "bold"),
                                   bg="white").place(x=140, y=260)

        scroll_x = Scrollbar(self.mainframe, orient=HORIZONTAL)
        scroll_y = Scrollbar(self.mainframe, orient=VERTICAL)
        self.library_table = ttk.Treeview(self.mainframe, columns=(
            'ID',  'Name', 'Address', 'Mobile No.',  'Member Type', 'Book Id', 'Book Authur',
            'Date Borrow', 'Due Date'),
                                          xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.library_table.xview)
        scroll_y.config(command=self.library_table.yview)
        self.library_table.heading('ID', text='ID')
        self.library_table.heading('Name', text='Name')
        self.library_table.heading('Address', text='Address')
        self.library_table.heading('Mobile No.', text='Mobile No.')
        self.library_table.heading('Member Type', text='Member Type')
        self.library_table.heading('Book Id', text='Book Id')
        self.library_table.heading('Book Authur', text='Book Authur')
        self.library_table.heading('Date Borrow', text='Date Borrow')
        self.library_table.heading('Due Date', text='Due Date')


        self.library_table['show'] = 'headings'
        self.library_table.pack(fill=BOTH, expand=TRUE)
        self.library_table.pack()
        self.library_table.bind("<ButtonRelease-1>", self.cursor)
        self.fetchdata()

    def add_library(self):
            ID = self.ID.get()
            Name = self.Name.get()
            Address = self.Address.get()
            Mobile_No = self.Mobile_No.get()
            Member_Type = self.Member_Type.get()
            Book_Id = self.Book_Id.get()
            Book_Authur = self.Book_Authur.get()
            Book_Title = self.Book_Title.get()
            Date_Borrow = self.Date_Borrow.get()
            Due_Date = self.Due_Date.get()

            if ID == '' or Name == '' or Address == '' or Mobile_No == ''  or Member_Type == '' or Book_Id == '' or Book_Authur == '' or Book_Title == '' or Date_Borrow == '' or Due_Date == '' :
                messagebox.showerror("Error", "All field are required to add data")
            else:
                query = " select * from library where id=%s or name=%s "
                values = (ID, Name)
                rows = self.db.fetch(query, values)
            if rows != None:
                messagebox.showerror("Error", "id name is already present", parent=self.project)
            else:
                q1 = "Insert into library(id,name,address,mobile_no,member_type,book_id,book_authur,book_title,date_borrow,due_date)values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                values = (
                ID,  Name, Address, Mobile_No, Member_Type, Book_Id, Book_Authur, Book_Title, Date_Borrow, Due_Date,)
                self.db.add(q1, values)
                self.fetchdata()
                messagebox.showinfo("Sucess", "Data added sucessfully")

    def fetchdata(self):
            query = "select * from library "
            data = self.db.fetch_all(query)
            if len(data) != 0:
                self.library_table.delete(*self.library_table.get_children())
            for rows in data:
                self.library_table.insert('', END, value=rows)

    def cursor(self, a):
            coursor_rows = self.library_table.focus()
            data = self.library_table.item(coursor_rows)
            row = data['values']
            self.ID.set(row[0])
            self.Name.set(row[1])
            self.Address.set(row[2])
            self.Mobile_No.set(row[3])
            self.Member_Type.set(row[4])
            self.Book_Id.set(row[5])
            self.Book_Authur.set(row[6])
            self.Book_Title.set(row[7])
            self.Date_Borrow.set(row[8])
            self.Due_Date.set(row[9])


    def update(self):
            ID = self.ID.get()
            Name = self.Name.get()
            Address = self.Address.get()
            Mobile_No = self.Mobile_No.get()
            Member_Type = self.Member_Type.get()
            Book_Id = self.Book_Id.get()
            Book_Authur = self.Book_Authur.get()
            Book_Title = self.Book_Title.get()
            Date_Borrow = self.Date_Borrow.get()
            Due_Date = self.Due_Date.get()
            query = "update library set  name=%s, address=%s, mobile_no=%s, member_type=%s, book_id=%s, book_authur=%s, book_title=%s, date_borrow=%s, due_date=%s  where id=%s"
            value = (
             Name, Address, Mobile_No, Member_Type, Book_Id, Book_Authur, Book_Title, Date_Borrow, Due_Date, ID)
            self.db.update(query, value)
            messagebox.showinfo("sucess", "data update sucessfully")
            self.fetchdata()

    def delete(self):
        id= self.ID.get()
        query="delete from library where id=%s"
        value=(id,)
        self.db.delete(query,value)
        messagebox.showinfo("sucess","data delete sucessfully")
        self.fetchdata()

    def clear(self):
        self.ID.set("")
        self.Name.set("")
        self.Address.set("")
        self.Mobile_No.set("")
        self.Member_Type.set("")
        self.Book_Id.set("")
        self.Book_Authur.set("")
        self.Book_Title.set("")
        self.Date_Borrow.set("")
        self.Due_Date.set("")



if __name__=="__main__":
    tk=Tk()
    obj=Library(tk)
    tk.mainloop()