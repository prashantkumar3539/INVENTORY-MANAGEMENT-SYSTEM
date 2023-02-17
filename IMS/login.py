from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
import sqlite3
import os
import email_pass
import smtplib
import time

class Login_System:
    def __init__(self,root):
        self.root=root
        self.root.title("Inventory Database Management   |   Developed By PRASHANT KUMAR  !!")
        self.root.geometry("1900x1080+0+0")
        self.root.config(bg="#fafafa")
        
        
        self.otp=""
        #====== Images==============
        self.phone_image=ImageTk.PhotoImage(file="D:\VS Studio Code\IMS\image/phone.png")
        self.lbl_phone_image=Label(self.root,image=self.phone_image,bd=0).place(x=300,y=50)
        
        # =======  Login Frame ============
        
        self.employee_id=StringVar()
        self.password=StringVar()
        
        login_frame=Frame(self.root,bd=3,relief=RIDGE,bg="#fafafa")
        login_frame.place(x=750,y=90,width=375,height=480)
        
        title=Label(login_frame,text="Login System",font=("Elephant",30,"bold"),bg="#fafafa",fg="#9400d3").place(x=0,y=30,relwidth=1)
        
        lbl_user=Label(login_frame,text="Employee ID :",font=("Times New Roman",18,"bold"),bg="#fafafa").place(x=30,y=100)
        
        txt_username=Entry(login_frame,textvariable=self.employee_id,font=("goudy old style",18),bg="#ECECEC",fg="#00008b").place(x=35,y=140,width=280,height=35)

        lbl_pass=Label(login_frame,text="Password :",font=("Times New Roman",18,"bold"),bg="#fafafa").place(x=30,y=200)
        
        txt_pass=Entry(login_frame,textvariable=self.password,font=("goudy old style",18),show="*",bg="#ECECEC",fg="#00008b").place(x=35,y=240,width=280,height=35)
        
        btn_login=Button(login_frame, text="Log In",command=self.login, font=("times new roman",18,"bold"),bg="#f8dcfb",cursor="hand2",activebackground="#f8dcfb").place(x=30,y=300,height=50,width=280)
        
        hr=Label(login_frame,bg="lightgrey").place(x=30,y=385,width=280,height=2)
        
        or_=Label(login_frame,text="OR",font=("Times New Roman",15,"bold"),bg="#fafafa",fg="lightgrey").place(x=150,y=370)
        
        btn_forgot=Button(login_frame,text="Forget Password?",command=self.forget_window,font=("Times New Roman",15,"bold"),bd=0,activebackground="#fafafa",activeforeground="#00759E",bg="#fafafa",fg="#00759E" ,cursor="hand2").place(x=40,y=400,width=280)
        
        
        # Footer
        lbl_footer=Label(self.root,text="IMS: Inventory Database Management System  | Developed by PRASHANT KUMAR\n For any Technical Query CONTACT 9122706809",font=("times new roman",18),bg="#008b8b",fg="#ffffff").pack(side=BOTTOM,fill=X)
        
        
        
        
        # ======Animation Images =================
        
        self.loginim1=ImageTk.PhotoImage(file="D:\VS Studio Code\IMS\image/logim1.png")
        self.loginim2=ImageTk.PhotoImage(file="D:\VS Studio Code\IMS\image/logim2.png")
        self.loginim3=ImageTk.PhotoImage(file="D:\VS Studio Code\IMS\image/logim3.png")
        
        
        
        self.lbl_change_image=Label(self.root,bg="#fafafa")
        self.lbl_change_image.place(x=467,y=153,width=240,height=428)
        
        self.animate()
        
    def animate(self):
        self.im=self.loginim1
        self.loginim1=self.loginim2    
        self.loginim2=self.loginim3    
        self.loginim3=self.im
        self.lbl_change_image.config(image=self.im)
        self.lbl_change_image.after(2000,self.animate)
    
        
    def login(self):
        con=sqlite3.connect(database=r'ims.db' )
        cur=con.cursor()
        try:
            if self.employee_id.get()=="" or self.password.get()=="":
                messagebox.showerror("Error","All Credentials are Required !!",parent=self.root)
            else:
                cur.execute("select utype from employee where eid=? AND pass=?",(self.employee_id.get(),self.password.get()))
                user=cur.fetchone()
                if user==None:
                    messagebox.showerror("Error","Invalid USERNAME / PASSWORD !!",parent=self.root)
                else:
                    if user[0]=="Admin":
                        self.root.destroy()
                        os.system("python IMS/dashboard.py")
                    else:
                        self.root.destroy()
                        os.system("python IMS/billing.py")
                    
        except Exception as ex:
                messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)
    
    
    def forget_window(self):
        con=sqlite3.connect(database=r'ims.db' )
        cur=con.cursor()
        try:
            if self.employee_id.get()=="":
                messagebox.showerror("Error","Employee ID must be Required !!",parent=self.root)
            else:
                cur.execute("select email from employee where eid=?",(self.employee_id.get(),))
                email=cur.fetchone()
                if email==None:
                    messagebox.showerror("Error","Invalid Employee ID !!\n Try Again with correct Employee ID !!",parent=self.root)
                else:
                    # ======== Forget Window ===========
                    self.var_otp=StringVar()
                    self.var_new_pass=StringVar()
                    self.var_conf_pass=StringVar()
                    # Call Send Email Function =============
                    chk=self.send_email(email[0])
                    if chk=='f':
                        messagebox.showerror("Error","Connection Error !!!\nTry Again !!!",parent=self.root)
                    else:
                        
                        self.forget_win=Toplevel(self.root)
                        self.forget_win.title("RESET PASSWORD ")
                        self.forget_win.geometry("600x450+750+120")
                        self.forget_win.config(bg="#f8f8ff")
                        self.forget_win.focus_force()
                    
                        
                        title=Label(self.forget_win,text="Reset Password",font=("goudy old style",20,"bold"),bg="#800080",fg="#f8f8ff",bd=5,relief=RAISED).pack(side=TOP,fill=X)
                        lbl_reset=Label(self.forget_win,text="Enter OTP sent on Registered Email ",font=("Times new roman",16),bg="#f8f8ff").place(x=20,y=80)
                        txt_reset=Entry(self.forget_win,textvariable=self.var_otp,font=("goudy old style",18),bg="#ECECEC",fg="#00008b").place(x=20,y=120,width=200,height=35)
                        
                        self.btn_reset=Button(self.forget_win, text="Submit",command=self.validate_otp, font=("times new roman",18,"bold"),bg="#ff1493",fg="#f8f8ff",cursor="hand2",activebackground="#ff1493")
                        self.btn_reset.place(x=340,y=115,height=35,width=120)
                        
                        lbl_new_pass=Label(self.forget_win,text="New Password ",font=("Times new roman",16),bg="#f8f8ff").place(x=20,y=160)
                        txt_new_pass=Entry(self.forget_win,textvariable=self.var_new_pass,font=("goudy old style",18),bg="#ECECEC",fg="#00008b").place(x=20,y=200,width=200,height=35)
                        
                        lbl_conf_pass=Label(self.forget_win,text="Confirm Password  ",font=("Times new roman",16),bg="#f8f8ff").place(x=20,y=250)
                        txt_conf_pass=Entry(self.forget_win,textvariable=self.var_conf_pass,font=("goudy old style",18),bg="#ECECEC",fg="#00008b").place(x=20,y=290,width=200,height=35)
                        
                        self.btn_update=Button(self.forget_win, text="Update",command=self.update_password,state=DISABLED, font=("times new roman",18,"bold"),bg="#f8dcfb",cursor="hand2",activebackground="#f8dcfb")
                        self.btn_update.place(x=160,y=345,height=35,width=120)
                
        except Exception as ex:
                messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)
    
    
    def update_password(self):
        if self.var_new_pass.get()=="" or self.var_conf_pass.get()=="":
            messagebox.showerror("Error","Fill the required Credential !!",parent=self.forget_win)
        elif self.var_new_pass.get()!=self.var_conf_pass.get():
            messagebox.showerror("Error","New Password and Confirm Password must be same !!",parent=self.forget_win)
        else:
            con=sqlite3.connect(database=r'ims.db' )
            cur=con.cursor()
            try:
                cur.execute("update employee SET pass=?  where eid=?",(self.var_new_pass.get(),self.employee_id.get()))
                con.commit()
                messagebox.showinfo("Success","Password Updated Successfully !!",parent=self.forget_win)
                self.forget_win.destroy()
            except Exception as ex:
                messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)
    
    def validate_otp(self):
        if int(self.otp)==int(self.var_otp.get()):
            self.btn_update.config(state=NORMAL)            
            self.btn_reset.config(state=DISABLED)
        else:
            messagebox.showerror("Error","Invalid OTP !!\nTry Again with correct OTP !!",parent=self.forget_win)
                        
    def send_email(self,to_):
        s=smtplib.SMTP('smtp.gmail.com',587) # 587 for gmail works on 587 port number
        s.starttls()
        email_=email_pass.email_
        pass_=email_pass.pass_
        
        s.login(email_, pass_)
        
        self.otp=int(time.strftime("%H%S%M"))+int(time.strftime("%S"))
        
        subj="IMS : By Prashant Kumar -Reset Password OTP"
        msg=f"Dear Sir/Madam,\n\nYour Reset OTP is {str(self.otp)}.\n\n\nWith Regards,\nIMS Team\n(Prashant Kumar)"
        msg="Subject:{}\n\n{}".format(subj,msg)
        s.sendmail(email_, to_, msg)
        chk=s.ehlo()
        if chk[0]==250:
            return 's'
        else:
            return 'f' 

    
if  __name__=="__main__":
    root=Tk()
    obj=Login_System(root)
    root.mainloop()