from tkinter import*

class TeacherSystem:
    def __init__(self,root):
        self.root=root
        self.root.title("Teacher Profile:")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")

        title = Label(self.root,text="Teacher Profile",font=("times new roman",30,"bold"),bg="cadet blue",fg="lightgrey").place(x=0,y=0,relwidth=1)

        self.var_teacher_id=StringVar()
        self.var_designation = StringVar()
        self.var_name = StringVar()
        self.var_age = StringVar()
        self.var_gender = StringVar()
        self.var_email = StringVar()
        self.var_hr_location= StringVar()
        self.var_dob = StringVar()
        self.var_doj = StringVar()
        self.var_proof_id=StringVar()
        self.var_contact=StringVar()
        self.var_status=StringVar()
        self.var_experience = StringVar()




        Frame1=Frame(self.root,bd=3,relief=RIDGE,bg="powderblue")
        Frame1.place(x=10,y=70,width=750,height=620)
        title2 = Label(Frame1,text="Teacher Details", font=("times new roman", 20), bg="cadet blue", fg="powderblue",anchor="w").place(x=0,y=0,relwidth=1)


        lbl_Id = Label(Frame1,text="Teacher ID", font=("times new roman", 20),bg="powderblue",fg="cadetblue").place(x=10,y=70)
        txt_id = Entry(Frame1,font=("times new roman",15),textvariable=self.var_teacher_id,bg="light grey",fg="black").place(x=220,y=74,width=200)
        btn_search=Button(Frame1,text="Search",font=("times new roman",20),bg="cadet blue",fg="powder blue").place(x=440,y=72,height =30)


        lbl_designation = Label(Frame1, text="Designation", font=("times new roman", 20), bg="cadet blue",fg="powderblue").place(x=10, y=120)
        txt_designation = Entry(Frame1, font=("times new roman", 15),textvariable=self.var_designation, bg="light grey", fg="black").place(x=170, y=125,width=200)
        lbl_dob = Label(Frame1, text="D.O.B", font=("times new roman", 20), bg="cadet blue", fg="powderblue").place(x=390, y=120)
        txt_dob = Entry(Frame1, font=("times new roman", 15),textvariable=self.var_dob, bg="light grey", fg="black").place(x=520, y=125)

        lbl_Name = Label(Frame1, text="Name", font=("times new roman", 20), bg="cadet blue",fg="powderblue").place(x=10, y=170)
        txt_Name = Entry(Frame1, font=("times new roman", 15),textvariable=self.var_name, bg="light grey", fg="black").place(x=170, y=175, width=200)
        lbl_doj = Label(Frame1, text="D.O.J", font=("times new roman", 20), bg="cadet blue", fg="powderblue").place( x=390, y=170)
        txt_doj = Entry(Frame1, font=("times new roman", 15),textvariable=self.var_doj, bg="light grey", fg="black").place(x=520, y=175)

        lbl_age = Label(Frame1, text="Age", font=("times new roman", 20), bg="cadet blue", fg="powderblue").place( x=10, y=220)
        txt_age = Entry(Frame1, font=("times new roman", 15),textvariable=self.var_age,bg="light grey", fg="black").place(x=170, y=225, width=200)
        lbl_experience = Label(Frame1, text="Experience", font=("times new roman", 20), bg="cadet blue", fg="powderblue").place(x=390, y=220)
        txt_experience = Entry(Frame1, font=("times new roman", 15),textvariable=self.var_experience, bg="light grey", fg="black").place(x=520, y=225)

        lbl_gender = Label(Frame1, text="Gender", font=("times new roman", 20), bg="cadet blue", fg="powderblue").place(x=10, y=270)
        txt_gender = Entry(Frame1, font=("times new roman", 15),textvariable=self.var_gender, bg="light grey", fg="black").place(x=170, y=275, width=200)
        lbl_proof = Label(Frame1, text="Proof ID", font=("times new roman", 20), bg="cadet blue",fg="powderblue").place(x=390, y=270)
        txt_proof = Entry(Frame1, font=("times new roman", 15),textvariable=self.var_proof_id,bg="light grey", fg="black").place(x=520, y=275)

        lbl_email = Label(Frame1, text="Email", font=("times new roman", 20), bg="cadet blue", fg="powderblue").place(x=10, y=320)
        txt_email = Entry(Frame1, font=("times new roman", 15),textvariable=self.var_email,bg="light grey", fg="black").place(x=170, y=325, width=200)
        lbl_contact= Label(Frame1, text="Contact", font=("times new roman", 20), bg="cadet blue",fg="powderblue").place(x=390, y=320)
        txt_contact = Entry(Frame1, font=("times new roman", 15),textvariable=self.var_contact,bg="light grey", fg="black").place(x=520, y=325)


        lbl_hired = Label(Frame1, text="Hired location", font=("times new roman", 18), bg="cadet blue", fg="powderblue").place(x=10, y=372)
        txt_hired = Entry(Frame1, font=("times new roman", 15),textvariable=self.var_hr_location, bg="light grey", fg="black").place(x=170, y=375, width=200)
        lbl_status = Label(Frame1, text="Status", font=("times new roman", 20), bg="cadet blue",fg="powderblue").place(x=390, y=370)
        txt_status= Entry(Frame1, font=("times new roman", 15),textvariable=self.var_status,bg="light grey", fg="black").place(x=520, y=375)

        lbl_address = Label(Frame1, text="Address", font=("times new roman", 18), bg="cadet blue",fg="powderblue").place(x=10, y=422)
        self.txt_address = Entry(Frame1, font=("times new roman", 15), bg="light grey", fg="black")
        self.txt_address.place(x=170, y=425, width=550,height=150)




        self.var_teacher_id=StringVar()
        self.var_designation=StringVar()
        self.var_name = StringVar()
        self.var_age = StringVar()
        self.var_gender = StringVar()
        self.var_email = StringVar()
        self.var_hr_location= StringVar()
        self.var_dob = StringVar()





        self.var_month=StringVar()
        self.var_year = StringVar()
        self.var_salary = StringVar()
        self.var_t_days = StringVar()
        self.var_absent = StringVar()
        self.var_medical = StringVar()
        self.var_pf = StringVar()
        self.var_convence = StringVar()
        self.var_net_salary = StringVar()





        Frame2 = Frame(self.root, bd=3, relief=RIDGE, bg="powderblue")
        Frame2.place(x=770, y=70, width=580, height=300)



        title3 = Label(Frame2, text="Salary Details", font=("times new roman", 20), bg="cadet blue", fg="powderblue", anchor="w").place(x=0, y=0, relwidth=1)
        lbl_month = Label(Frame2, text="Month", font=("times new roman", 18), bg="powderblue", fg="cadetblue").place( x=10, y=60)
        txt_month = Entry(Frame2, font=("times new roman", 15),textvariable=self.var_month, bg="light grey", fg="black").place(x=90, y=62, width=100)
        lbl_year = Label(Frame2, text="Year", font=("times new roman", 18), bg="powderblue", fg="cadetblue").place( x=210, y=60)
        txt_year = Entry(Frame2, font=("times new roman", 15),textvariable=self.var_year, bg="light grey", fg="black").place(x=270, y=62, width=100)

        lbl_salary = Label(Frame2, text="Salary", font=("times new roman", 18), bg="powderblue", fg="cadetblue").place( x=380, y=60)
        txt_salary = Entry(Frame2, font=("times new roman", 15),textvariable=self.var_salary, bg="light grey", fg="black").place(x=460, y=62,width=100)


        lbl_days= Label(Frame2, text="Total Days", font=("times new roman", 18), bg="cadet blue",fg="powderblue").place(x=10, y=120)
        txt_days = Entry(Frame2, font=("times new roman", 15),textvariable=self.var_t_days, bg="light grey", fg="black").place(x=170, y=125, width=100)
        lbl_absent = Label(Frame2, text="Absent", font=("times new roman",18), bg="cadet blue", fg="powderblue").place( x=300, y=120)
        txt_absent = Entry(Frame2, font=("times new roman", 15),textvariable=self.var_absent, bg="light grey", fg="black").place(x=420, y=125,width=120)



        lbl_medical= Label(Frame2, text="Medical", font=("times new roman", 18), bg="cadet blue",fg="powderblue").place(x=10, y=150)
        txt_medical = Entry(Frame2, font=("times new roman", 15),textvariable=self.var_medical, bg="light grey", fg="black").place(x=170, y=155, width=100)
        lbl_pf = Label(Frame2, text="PF", font=("times new roman",18), bg="cadet blue", fg="powderblue").place( x=300, y=150)
        txt_pf = Entry(Frame2, font=("times new roman", 15),textvariable=self.var_pf, bg="light grey", fg="black").place(x=420, y=155,width=120)



        lbl_convence= Label(Frame2, text="Convence", font=("times new roman", 18), bg="cadet blue",fg="powderblue").place(x=10, y=180)
        txt_convence = Entry(Frame2, font=("times new roman", 15),textvariable=self.var_convence, bg="light grey", fg="black").place(x=170, y=185, width=100)
        lbl_netsalary = Label(Frame2, text="Net Salary", font=("times new roman",18), bg="cadet blue", fg="powderblue").place( x=300, y=180)
        txt_netsalary = Entry(Frame2, font=("times new roman", 15),textvariable=self.var_net_salary, bg="light grey", fg="black").place(x=420, y=185,width=120)

        btn_calculate = Button(Frame2, text="Calculate",command=self.calculate, font=("times new roman", 20), bg="brown",fg="powder blue").place(x=150, y=240, height=30,width=120)
        btn_save = Button(Frame2, text="Save", font=("times new roman", 20), bg="light green", fg="red").place(x=285, y=240, height=30,width=120)
        btn_clear = Button(Frame2, text="Clear", font=("times new roman", 20), bg="red",fg="black").place(x=420, y=240, height=30,width=120)



        Frame3 = Frame(self.root, bd=3, relief=RIDGE, bg="cadetblue")
        Frame3.place(x=770, y=380, width=580, height=310)

        self.var_txt=StringVar()
        self.var_operator=''
        def btn_click(num):
            self.var_operator = self.var_operator + str(num)
            self.var_txt.set(self.var_operator)
        def result():
            res = str(eval(self.var_operator))
            self.var_txt.set(res)
            self.var_operator=''

        def clear_cal():
            self.var_txt.set('')
            self.var_operator=''




        cal_Frame=Frame(Frame3,bg="cadetblue",bd=2,relief=RIDGE)
        cal_Frame.place(x=2,y=2,width=248,height=300)

        txt_Result=Entry(cal_Frame,bg="light grey",textvariable=self.var_txt,font=("times new roman",20,"bold"),justify=RIGHT).place(x=0,y=0,relwidth=1,height=50)
        btn_7=Button(cal_Frame,text='7',command=lambda:btn_click(7),font=("times new roman",15,"bold",),fg="black",bg="grey").place(x=0,y=52,w=60,h=60)
        btn_8 = Button(cal_Frame, text='8',command=lambda:btn_click(8),font=("times new roman", 15, "bold"),fg="black",bg="grey").place(x=61, y=52, w=60, h=60)
        btn_9 = Button(cal_Frame, text='9',command=lambda:btn_click(9),font=("times new roman", 15, "bold",),fg="black",bg="grey").place(x=122, y=52, w=60, h=60)
        btn_div = Button(cal_Frame, text='/',command=lambda:btn_click("/"),font=("times new roman", 15, "bold"),fg="black",bg="grey").place(x=183, y=52, w=60, h=60)
        btn_4 = Button(cal_Frame, text='4', command=lambda:btn_click(4),font=("times new roman", 15, "bold",), fg="black", bg="grey").place(x=0,y=112,w=60,h=60)
        btn_5 = Button(cal_Frame, text='5',command=lambda:btn_click(5),font=("times new roman", 15, "bold"), fg="black", bg="grey").place(x=61,  y=112,w=60, h=60)
        btn_6 = Button(cal_Frame, text='6',command=lambda:btn_click(6),font=("times new roman", 15, "bold",), fg="black", bg="grey").place(x=122, y=112,w=60,h=60)
        btn_mul = Button(cal_Frame, text='*',command=lambda:btn_click("*"), font=("times new roman", 15, "bold"), fg="black", bg="grey").place(x=183,y=112,w=60,h=60)


        btn_1 = Button(cal_Frame, text='1',command=lambda:btn_click(1), font=("times new roman", 15, "bold",), fg="black", bg="grey").place(x=0,y=172,w=60,h=60)
        btn_2 = Button(cal_Frame, text='2',command=lambda:btn_click(2), font=("times new roman", 15, "bold"), fg="black", bg="grey").place(x=61,  y=172,w=60, h=60)
        btn_3 = Button(cal_Frame, text='3',command=lambda:btn_click(3), font=("times new roman", 15, "bold",), fg="black", bg="grey").place(x=122, y=172,w=60,h=60)
        btn_min = Button(cal_Frame, text='-',command=lambda:btn_click("-"), font=("times new roman", 15, "bold"), fg="black", bg="grey").place(x=183,y=172,w=60,h=60)



        btn_0 = Button(cal_Frame, text='0',command=lambda:btn_click(0), font=("times new roman", 15, "bold",), fg="black", bg="grey").place(x=0,y=233,w=60,h=60)
        btn_dot = Button(cal_Frame, text='C',command=clear_cal, font=("times new roman", 15, "bold"), fg="black", bg="grey").place(x=61,  y=233,w=60, h=60)
        btn_sum = Button(cal_Frame, text='+', command=lambda:btn_click("+"),font=("times new roman", 15, "bold",), fg="black", bg="grey").place(x=122, y=233,w=60,h=60)
        btn_equal = Button(cal_Frame, text='=',command=result, font=("times new roman", 15, "bold"), fg="black", bg="grey").place(x=183,y=233,w=60,h=60)

        sal_Frame=Frame(Frame3,bg="powderblue",bd=2,relief=RIDGE)
        sal_Frame.place(x=251,y=2,width=320,height=300)
        title_sal= Label(sal_Frame, text="Salary Reciept", font=("times new roman", 20), bg="cadet blue", fg="powderblue",anchor="w").place(x=0, y=0, relwidth=1)

        sal_Frame2=Frame(sal_Frame,bg="light gray",bd=2,relief=RIDGE)
        sal_Frame2.place(x=0,y=30,relwidth=1,height=230)

        scroll_y=Scrollbar(sal_Frame2,orient=VERTICAL)
        scroll_y.pack(fill=Y,side=RIGHT)

        self.txt_salary_recipt=Text(sal_Frame2,font=("times new roman",15),bg="light grey",yscrollcommand=scroll_y.set)
        self.txt_salary_recipt.pack(fill=BOTH,expand=1)
        scroll_y.config(command=self.txt_salary_recipt.yview)

        btn_print = Button(sal_Frame, text="Print", font=("times new roman", 20), bg="powderblue",fg="black").place(x=180, y=262, height=30, width=120)

    def calculate(self):

         print(self.var_teacher_id.get(),
         self.var_designation.get(),
         self.var_name.get(),
         self.var_age.get(),
         self.var_gender.get(),
         self.var_email.get(),
         self.var_hr_location.get(),
         self.var_dob.get(),
         self.var_doj.get(),
         self.var_proof_id.get(),
         self.var_contact.get(),
         self.var_status.get(),
         self.var_experience.get(),




         self.var_month.get(),
         self.var_year.get(),
         self.var_salary.get(),
         self.var_t_days.get(),
         self.var_absent.get(),
         self.var_medical.get(),
         self.var_pf.get(),
         self.var_convence.get(),
         self.var_net_salary.get(),
         self.txt_address.get(),
         )




root=Tk()
obj=TeacherSystem(root)
root.mainloop()






















