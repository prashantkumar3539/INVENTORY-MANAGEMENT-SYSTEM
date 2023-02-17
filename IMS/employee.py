from tkinter import *
from PIL import Image,ImageTk 
from tkinter import ttk,messagebox
import sqlite3

class employeeClass:
    def __init__(self,root):
        self.root=root
        self.root.title("Inventory Database Management By Prashant")
        self.root.geometry("1225x670+255+125")
        self.root.config(bg="#ecf8f9")
        self.root.focus_force()
        # ======================
        #  All variables========================
        self.var_searchby=StringVar()
        self.var_searchtxt=StringVar()
        self.var_emp_id=StringVar()
        self.var_gender=StringVar()
        self.var_contact=StringVar()
        self.var_name=StringVar()
        self.var_dob=StringVar()
        self.var_doj=StringVar()
        self.var_email=StringVar()
        self.var_pass=StringVar()
        self.var_utype=StringVar()
        self.var_salary=StringVar()
        
        # ======================================================
        searchFrame=LabelFrame(self.root,text="Search Employee",font=("goudy old style",15,"bold"),bd=4,relief=RIDGE,bg="#ecf8f9",fg="#f30f0f")
        searchFrame.place(x=350,y=10,width=600,height=70)
        
        # ==========Option================
        cmb_search=ttk.Combobox(searchFrame,textvariable=self.var_searchby,values=("Select","Email","Name","Contact"),state='readonly',justify=CENTER,font=("goudy old style", 13,"bold"))
        cmb_search.place(x=10,y=10,width=180)
        cmb_search.current(0)
        
        txt_search=Entry(searchFrame,textvariable=self.var_searchtxt,font=("goudy old style",15,"bold"),bg="lightyellow",fg="#f51435").place(x=200,y=10)
        
        btn_search=Button(searchFrame,command=self.search,text="Search",cursor="hand2",font=("goudy old style",15,"bold"),bg="#ffdab9",fg="#ff00ff").place(x=410,y=8,width=150,height=30)
        
        # =======Title===============
        title=Label(self.root,text="Employee Details",font=("times new roman" "bold",18,"bold"),bd=3,relief=RIDGE,bg="#faf0e6",fg="#c71585").place(x=50,y=120,width=1100)
        
        #========Content===================
        
        #============ Row 1 ==============================
        lbl_empid=Label(self.root,text="Emp ID",font=("times new roman" ,18,"bold"),bg="#ecf8f9").place(x=50,y=180)
        
        lbl_gender=Label(self.root,text="Gender",font=("times new roman" ,18,"bold"),bg="#ecf8f9").place(x=450,y=180)

        lbl_contact=Label(self.root,text="Contact",font=("times new roman" ,18,"bold"),bg="#ecf8f9").place(x=800,y=180)
        
        txt_empid=Entry(self.root,textvariable=self.var_emp_id,font=("goudy old style",15,"bold"),bg="lightyellow",fg="#f51435").place(x=150,y=180)
        
        cmb_gender=ttk.Combobox(self.root,textvariable=self.var_gender,values=("Select","Male","Female","Others"),state='readonly',justify=CENTER,font=("goudy old style", 13,"bold"))
        
        cmb_gender.place(x=550,y=180,width=180)
        cmb_gender.current(0)

        txt_contact=Entry(self.root,textvariable=self.var_contact,font=("goudy old style",15,"bold"),bg="lightyellow",fg="#f51435").place(x=900,y=180)
        
        #============ Row 2 ==============================
        lbl_name=Label(self.root,text="Name",font=("times new roman" ,18,"bold"),bg="#ecf8f9").place(x=50,y=230)
        
        lbl_dob=Label(self.root,text="D.O.B.",font=("times new roman" ,18,"bold"),bg="#ecf8f9").place(x=450,y=230)

        lbl_doj=Label(self.root,text="D.O.J.",font=("times new roman" ,18,"bold"),bg="#ecf8f9").place(x=800,y=230)
        
        txt_name=Entry(self.root,textvariable=self.var_name,font=("goudy old style",15,"bold"),bg="lightyellow",fg="#f51435").place(x=150,y=230)
        
        txt_dob=Entry(self.root,textvariable=self.var_dob,font=("goudy old style",15,"bold"),bg="lightyellow",fg="#f51435").place(x=550,y=230)

        
        txt_doj=Entry(self.root,textvariable=self.var_doj,font=("goudy old style",15,"bold"),bg="lightyellow",fg="#f51435").place(x=900,y=230)

        #============ Row 3 ==============================
        lbl_email=Label(self.root,text="Email",font=("times new roman" ,18,"bold"),bg="#ecf8f9").place(x=50,y=280)
        
        lbl_pass=Label(self.root,text="Password",font=("times new roman" ,18,"bold"),bg="#ecf8f9").place(x=430,y=280)

        lbl_utype=Label(self.root,text="User Type",font=("times new roman" ,18,"bold"),bg="#ecf8f9").place(x=800,y=280)
        
        txt_email=Entry(self.root,textvariable=self.var_email,font=("goudy old style",15,"bold"),bg="lightyellow",fg="#f51435").place(x=150,y=280)
        
        txt_pass=Entry(self.root,textvariable=self.var_pass,font=("goudy old style",15,"bold"),bg="lightyellow",fg="#f51435").place(x=550,y=280)

        cmb_utype=ttk.Combobox(self.root,textvariable=self.var_utype,values=("Admin","Employee"),state='readonly',justify=CENTER,font=("goudy old style", 13,"bold"))
        cmb_utype.place(x=950,y=280,width=180)
        cmb_utype.current(0)
        
        #============ Row 4 ==============================
        lbl_address=Label(self.root,text="Address",font=("times new roman" ,18,"bold"),bg="#ecf8f9").place(x=50,y=330)
        
        lbl_salary=Label(self.root,text="Salary",font=("times new roman" ,18,"bold"),bg="#ecf8f9").place(x=550,y=330)
        
        self.txt_address=Text(self.root,font=("goudy old style",15,"bold"),bg="lightyellow",fg="#f51435")
        self.txt_address.place(x=150,y=330,width=300,height=60)
        
        txt_salary=Entry(self.root,textvariable=self.var_salary,font=("goudy old style",15,"bold"),bg="lightyellow",fg="#f51435").place(x=650,y=330)

        # ======= Buttons====================
        btn_add=Button(self.root,command=self.add,text="Save",cursor="hand2",font=("goudy old style",15,"bold"),bg="#4682b4",fg="white").place(x=550,y=400,width=100,height=30)
        
        btn_update=Button(self.root,command=self.update,text="Update",cursor="hand2",font=("goudy old style",15,"bold"),bg="#228b22",fg="white").place(x=700,y=400,width=100,height=30)
        
        btn_delete=Button(self.root,command=self.delete,text="Delete",cursor="hand2",font=("goudy old style",15,"bold"),bg="#f94d00",fg="white").place(x=850,y=400,width=100,height=30)
        
        btn_clear=Button(self.root,command=self.clear,text="Clear",cursor="hand2",font=("goudy old style",15,"bold"),bg="red",fg="white").place(x=1010,y=400,width=100,height=30)
        
        #======= Faculty Details ========================
        
        emp_frame=Frame(self.root,bd=4,relief=RIDGE)
        emp_frame.place(x=0,y=450,relwidth=1,height=220)
        
        scrollx=Scrollbar(emp_frame,orient=HORIZONTAL)
        scrolly=Scrollbar(emp_frame,orient=VERTICAL)
        
        self.EmployeeTable=ttk.Treeview(emp_frame,columns=("eid","name","email","gender","contact","dob","doj","pass","utype","address","salary"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.EmployeeTable.xview)
        scrolly.config(command=self.EmployeeTable.yview)
        
        self.EmployeeTable.heading("eid",text="EMP ID")
        self.EmployeeTable.heading("name",text="Name")
        self.EmployeeTable.heading("email",text="Email")
        self.EmployeeTable.heading("gender",text="Gender")
        self.EmployeeTable.heading("contact",text="Contact")
        self.EmployeeTable.heading("dob",text="DOB")
        self.EmployeeTable.heading("doj",text="DOJ")
        self.EmployeeTable.heading("pass",text="Password")
        self.EmployeeTable.heading("utype",text="User Type")
        self.EmployeeTable.heading("address",text="Address")
        self.EmployeeTable.heading("salary",text="Salary")   

        self.EmployeeTable["show"]="headings"
        
        self.EmployeeTable.column("eid",width=90)
        self.EmployeeTable.column("name",width=100)
        self.EmployeeTable.column("email",width=100)
        self.EmployeeTable.column("gender",width=100)
        self.EmployeeTable.column("contact",width=100)
        self.EmployeeTable.column("dob",width=100)
        self.EmployeeTable.column("doj",width=100)
        self.EmployeeTable.column("pass",width=100)
        self.EmployeeTable.column("utype",width=100)
        self.EmployeeTable.column("address",width=100)
        self.EmployeeTable.column("salary",width=100)
        self.EmployeeTable.pack(fill=BOTH,expand=1)
        self.EmployeeTable.bind("<ButtonRelease-1>",self.get_data)
        self.show()
#================ Functions ===============================        
    def add(self):
        con=sqlite3.connect(database=r'ims.db' )
        cur=con.cursor()
        try:
            if self.var_emp_id.get()=="":
                messagebox.showerror("Error","Employee ID Must be Required",parent=self.root)
                
            else:
                cur.execute("Select * from employee where eid=?",(self.var_emp_id.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","This Employee ID already asssigned , Try different Employee ID")
                else:
                    cur.execute("Insert into employee(eid , name , email , gender , contact , dob , doj , pass , utype , address , salary ) values(?,?,?,?,?,?,?,?,?,?,?)",(
                                                    self.var_emp_id.get(),
                                                    self.var_name.get(),
                                                    self.var_email.get(),
                                                    self.var_gender.get(),
                                                    self.var_contact.get(),
                                                    self.var_dob.get(),
                                                    self.var_doj.get(),
                                                    self.var_pass.get(),
                                                    self.var_utype.get(),
                                                    self.txt_address.get('1.0',END),
                                                    self.var_salary.get()
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Employee Added SUCCESSFULLY !!",parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)

    def show(self):
        con=sqlite3.connect(database=r'ims.db' )
        cur=con.cursor()
        try:
            cur.execute("Select * from employee")
            rows=cur.fetchall()
            self.EmployeeTable.delete(*self.EmployeeTable.get_children())
            for row in rows:
                self.EmployeeTable.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)
            
    def get_data(self,ev):
        f=self.EmployeeTable.focus()
        content=(self.EmployeeTable.item(f))
        row=content['values']
        self.var_emp_id.set(row[0])
        self.var_name.set(row[1])
        self.var_email.set(row[2])
        self.var_gender.set(row[3])
        self.var_contact.set(row[4])
        self.var_dob.set(row[5])
        self.var_doj.set(row[6])
        self.var_pass.set(row[7])
        self.var_utype.set(row[8])
        self.txt_address.delete('1.0',END)
        self.txt_address.insert(END, row[9])
        self.var_salary.set(row[10])
        
        
    def update(self):
        con=sqlite3.connect(database=r'ims.db' )
        cur=con.cursor()
        try:
            if self.var_emp_id.get()=="":
                messagebox.showerror("Error","Employee ID Must be Required",parent=self.root)
                
            else:
                cur.execute("Select * from employee where eid=?",(self.var_emp_id.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid Employee ID")
                else:
                    cur.execute("Update employee set  name=? , email=? , gender=? , contact=? , dob=? , doj=? , pass=?, utype=? , address=? , salary=? where eid=?",(
                                                    self.var_name.get(),
                                                    self.var_email.get(),
                                                    self.var_gender.get(),
                                                    self.var_contact.get(),
                                                    self.var_dob.get(),
                                                    self.var_doj.get(),
                                                    self.var_pass.get(),
                                                    self.var_utype.get(),
                                                    self.txt_address.get('1.0',END),
                                                    self.var_salary.get(),
                                                    self.var_emp_id.get()
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Employee  Updated SUCCESSFULLY !!",parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)
            
            
    def delete(self):
        con=sqlite3.connect(database=r'ims.db' )
        cur=con.cursor()
        try:
            if self.var_emp_id.get()=="":
                messagebox.showerror("Error","Employee ID Must be Required",parent=self.root)
                
            else:
                op=messagebox.askyesno("CONFIRM","Do You Really want to DELETE ??",parent=self.root)
                if op==True:
                    cur.execute("Delete from employee where eid=?",(self.var_emp_id.get(),))
                    con.commit()
                    messagebox.showinfo("DELETE","Employee Deleted SUCCESSFULLY !!",parent=self.root)
                    self.clear()
    
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)
            
    def clear(self):
        self.var_emp_id.set("")
        self.var_name.set("")
        self.var_email.set("")
        self.var_gender.set("Select")
        self.var_contact.set("")
        self.var_dob.set("")
        self.var_doj.set("")
        self.var_pass.set("")
        self.var_utype.set("Admin")
        self.txt_address.delete('1.0',END)
        self.var_salary.set("")
        self.var_searchtxt.set("")
        self.var_searchby.set("Select")
        self.show()
        
    
        

        
    def search(self):
        con=sqlite3.connect(database=r'ims.db' )
        cur=con.cursor()
        try:
            if self.var_searchby.get()=="Select":
                messagebox.showerror("Error","Select a valid Option",parent=self.root)
            elif self.var_searchtxt.get()=="":
                messagebox.showerror("Error","Give  Search Area Input",parent=self.root)
            else:
                cur.execute("select * from employee where "+self.var_searchby.get()+" LIKE '%"+self.var_searchtxt.get()+"%'")
                rows=cur.fetchall()
                if len(rows)!=0:
                    self.EmployeeTable.delete(*self.EmployeeTable.get_children())
                    for row in rows:
                        self.EmployeeTable.insert('',END,values=row)
                else:
                    messagebox.showerror("Error","No Record Found !!!",parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)
                
        

if  __name__=="__main__":
    root=Tk()
    obj=employeeClass(root)
    root.mainloop()