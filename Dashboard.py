from tkinter import *
from tkinter import  messagebox
from PIL import Image, ImageTk
import Frontend.Course
import Frontend.Result
import Frontend.students
import Frontend.Vresult
#import Frontend.teacher2
import Frontend.Library
#import Frontend.Staff
import Backend.dbconnection



class Dashboard:
    def __init__(self,project):
        self.project=project
        self.project.title("College Management System")


        self.project.geometry("1900x1500+0+0")
        self.ob=Backend.dbconnection.Database()

        #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Student Image <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

        self.stu_image=ImageTk.PhotoImage(Image.open("C:/Users/DELL/PycharmProjects/pythonProject26/image/student.png"))
        # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Title <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
        title=Label(self.project,text="College Management System",compound=LEFT,image=self.stu_image,font=("goudy old style",30,"bold"),bg="#0af0e8",fg="blue")
        title.place(x=0,y=0,relwidth=1,height=70)
        #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Frame <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
        self.frame=LabelFrame(self.project,text="Menu Bar",font=("times new roman",15),bg="white",relief=RAISED)
        self.frame.place(x=10,y=80,height=100,width=1340)
        #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Button Course <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

        self.btn_course=Button(self.frame,text="Course",font=("times new roman",15),command=self.add_course,bg="#330000",fg="white",activeforeground="#0bf207",activebackground="#f1f507")
        self.btn_course.place(x=5,y=0,height=40,width=200)

        self.btn_student = Button(self.frame, text="Student", font=("times new roman", 15),command=self.add_student, bg="#330000", fg="white",activeforeground="#0bf207", activebackground="#f1f507")
        self.btn_student.place(x=215, y=0, height=40, width=200)

        self.btn_result = Button(self.frame, text="Result", font=("times new roman", 15),command=self.add_result, bg="#330000", fg="white",activeforeground="#0bf207", activebackground="#f1f507")
        self.btn_result.place(x=425, y=0, height=40, width=200)

        self.btn_view_student_result = Button(self.frame, text="ViewStudentResult",font=("times new roman", 15),command=self.add_viewstudentresult, bg="#330000", fg="white",activeforeground="#0bf207", activebackground="#f1f507")
        self.btn_view_student_result.place(x=635, y=0, height=40, width=200)

        self.btn_logout = Button(self.project, text="Logout",command=self.Logout,font=("times new roman", 15), bg="#330000", fg="white",activeforeground="#0bf207", activebackground="#f1f507")
        self.btn_logout.place(x=1000, y=150, height=40, width=100)

        # self.btn_change_password = Button(self.frame, text="ChangePassword", font=("times new roman", 15), bg="#330000", fg="white",activeforeground="#0bf207", activebackground="#f1f507")
        # self.btn_change_password.place(x=1055, y=0, height=40, width=200)

        self.btn_teacher_info = Button(self.frame, text="Teacher Info", font=("times new roman", 15), bg="#330000",
                                          fg="white",command=self.add_teacher2, activeforeground="#0bf207", activebackground="#f1f507")
        self.btn_teacher_info.place(x=845, y=0, height=40, width=200)

        # self.btn_teacher_info = Button(self.frame, text="Teacher Info", font=("times new roman", 15), bg="#330000",
        #                                fg="white", command=self.add_teacher, activeforeground="#0bf207",
        #                                activebackground="#f1f507")
        # self.btn_teacher_info.place(x=845, y=0, height=40, width=200)

        self.btn_library = Button(self.frame, text="Library", font=("times new roman", 15), bg="#330000",
                                       fg="white",command=self.add_library,  activeforeground="#0bf207", activebackground="#f1f507")
        self.btn_library.place(x=1055, y=0, height=40, width=200)


        # self.btn_staff = Button(self.frame, text="Staff Details", font=("times new roman", 15),
        #                                bg="#330000",fg="white", command=self.add_staff, activeforeground="#0bf207",activebackground="#f1f507")
        # self.btn_staff.place(x=215, y=90, height=40, width=200)







        self.background_image = ImageTk.PhotoImage(Image.open("C:/Users/DELL/PycharmProjects/pythonProject26/image/background.jpg"))
        #self.background_image = self.background_image.resize((920,350),Image.ANTIALIAS)
        self.bg_level=Label(self.project,image=self.background_image)
        self.bg_level.place(x=0,y=180,height=600,width=1300)




#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Update Levels <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

        self.lvl_course=Label(self.project,text="Total Courses\n[ 0 ]",font=("times new roman",35),bg="#9d13d4",fg="blue",relief="ridge",bd=10)
        self.lvl_course.place(x=20,y=250,width=350,height=300)
        self.update_course()

        self.lvl_student = Label(self.project, text="Total Students\n[ 0 ]", font=("times new roman", 35), bg="#9d13d4",fg="blue", relief="ridge", bd=10)
        self.lvl_student.place(x=450, y=250, width=350, height=300)


        self.lvl_totalresult = Label(self.project, text="Total Results\n[ 0 ]", font=("times new roman", 35), bg="#9d13d4",fg="blue", relief="ridge", bd=10)
        self.lvl_totalresult.place(x=900, y=250, width=350, height=300)
        self.update_result()
        self.update_student()
        self.update_course()
        #
        # self.mini_frame= Label(self.project)
        # self.mini_frame.place(x=1000,y=600,width=200,height=40)



    def update_course(self):
        try:
            query="select * from new_table"
            row=self.ob.fetch_all(query)
            self.lvl_course.config(text=f"Total Courses\n[{str(len(row))}]")
            self.lvl_course.after(10,self.update_course)
        except Exception as exe:
            messagebox.showerror("Error", f"Error due to: {str(exe)}", parent=self.project)

    def update_student(self):
        try:
            query="select * from student"
            row=self.ob.fetch_all(query)
            self.lvl_student.config(text=f"Total Students\n[{str(len(row))}]")
            self.lvl_student.after(10,self.update_student)
        except Exception as exe:
            messagebox.showerror("Error", f"Error due to: {str(exe)}", parent=self.project)

    def update_result(self):
        try:
            query="select * from reult"
            row=self.ob.fetch_all(query)
            print(len(row))
            self.lvl_totalresult.config(text=f"Total Results\n[{str(len(row))}]")
            self.lvl_totalresult.after(10,self.update_result)
        except Exception as exe:
            messagebox.showerror("Error", f"Error due to: {str(exe)}", parent=self.project)


    def add_course(self):
        self.n1=Toplevel(self.project)
        self.newobj=Frontend.Course.Course(self.n1)


    def add_student(self):
        self.n2=Toplevel(self.project)
        self.newobj=Frontend.students.Student(self.n2)

    def add_result(self):
        self.n3=Toplevel(self.project)
        self.newobj=Frontend.Result.Result(self.n3)

    def add_viewstudentresult(self):
        self.n4=Toplevel(self.project)
        self.newobj=Frontend.Vresult.ViewResult(self.n4)

    def add_teacher2(self):
        self.n5=Toplevel(self.project)
        self.newobj=Frontend.Teacher.Teacher(self.n5)

    def add_library(self):
        self.n6 = Toplevel(self.project)
        self.newobj = Frontend.Library.Library(self.n6)


    def Logout(self):
        response = messagebox.askyesno('Exit', 'Are you sure you want to logout?')
        if response:
           self.project.destroy()

    # def add_staff(self):
    #     self.n7 = Toplevel(self.project)
    #     self.newobj = Frontend.Staff.Staff(self.n7)

    # def add_logout(self):
    #     self.n8 = Toplevel(self.project)
    #     self.newobj = Frontend.(self.n8)




if __name__=="__main__":
    tk=Tk()
    obj=Dashboard(tk)

    tk.mainloop()


