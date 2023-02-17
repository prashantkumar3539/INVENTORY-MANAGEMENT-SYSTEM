from tkinter import *
from PIL import Image,ImageTk 
from tkinter import ttk,messagebox
import sqlite3

class supplierClass:
    def __init__(self,root):
        self.root=root
        self.root.title("Inventory Database Management   |   Developed By PRASHANT KUMAR  !!")
        self.root.geometry("1225x670+255+125")
        self.root.config(bg="#ecf8f9")
        self.root.focus_force()
        # ======================
        #  All variables========================
        self.var_searchby=StringVar()
        self.var_searchtxt=StringVar()
        self.var_sup_invoice=StringVar()
        self.var_name=StringVar()
        self.var_contact=StringVar()
        
        # ======================================================
        # searchFrame=LabelFrame(self.root,text="Search Supplier",font=("goudy old style",15,"bold"),bd=4,relief=RIDGE,bg="#faf0e6",fg="#f30f0f")
        # # searchFrame.place(x=350,y=10,width=600,height=70)
        
        # ==========Option================
        lbl_search=Label(self.root,text="Search by Invoice No.",font=("goudy old style", 13,"bold"),fg="#f30f0f")
        lbl_search.place(x=650,y=80)

        
        txt_search=Entry(self.root,textvariable=self.var_searchtxt,font=("goudy old style",15,"bold"),bg="lightyellow",fg="#f51435").place(x=820,y=80)
        
        btn_search=Button(self.root,command=self.search,text="Search",cursor="hand2",font=("goudy old style",15,"bold"),bg="#ffdab9",fg="#ff00ff").place(x=1050,y=80,width=100,height=28)
        
        # =======Title===============
        title=Label(self.root,text="Manage Supplier Details",font=("sans sarif" "bold",20 ,"bold"),bd=3,relief=RIDGE,bg="#c71585",fg="#ffffff").place(x=50,y=10,width=1100,height=40)
        
        #========Content===================
        
        #============ Row 1 ==============================
        lbl_supplier_invoice=Label(self.root,text="Invoice No.",font=("times new roman" ,18,"bold"),bg="#ecf8f9").place(x=50,y=60)
        
        txt_supplier_invoice=Entry(self.root,textvariable=self.var_sup_invoice,font=("goudy old style",15,"bold"),bg="lightyellow",fg="#f51435").place(x=200,y=60)
    
        
        #============ Row 2 ==============================
        lbl_name=Label(self.root,text="Name",font=("times new roman" ,18,"bold"),bg="#ecf8f9").place(x=50,y=110)
        
        txt_name=Entry(self.root,textvariable=self.var_name,font=("goudy old style",15,"bold"),bg="lightyellow",fg="#f51435").place(x=200,y=110)

        #============ Row 3 ==============================
        lbl_contact=Label(self.root,text="Contact",font=("times new roman" ,18,"bold"),bg="#ecf8f9").place(x=50,y=170)
        
        txt_contact=Entry(self.root,textvariable=self.var_contact,font=("goudy old style",15,"bold"),bg="lightyellow",fg="#f51435").place(x=200,y=170)

        
        #============ Row 4 ==============================
        lbl_desc=Label(self.root,text="Description",font=("times new roman" ,18,"bold"),bg="#ecf8f9").place(x=50,y=230)
        
        self.txt_desc=Text(self.root,font=("goudy old style",15,"bold"),bg="lightyellow",fg="#f51435")
        self.txt_desc.place(x=200,y=230,width=400,height=90)
        
        
        # ======= Buttons====================
        btn_add=Button(self.root,command=self.add,text="Save",cursor="hand2",font=("goudy old style",15,"bold"),bg="#4682b4",fg="white").place(x=10,y=500,width=120,height=30)
        
        btn_update=Button(self.root,command=self.update,text="Update",cursor="hand2",font=("goudy old style",15,"bold"),bg="#228b22",fg="white").place(x=150,y=500,width=120,height=30)
        
        btn_delete=Button(self.root,command=self.delete,text="Delete",cursor="hand2",font=("goudy old style",15,"bold"),bg="#f94d00",fg="white").place(x=290,y=500,width=120,height=30)
        
        btn_clear=Button(self.root,command=self.clear,text="Clear",cursor="hand2",font=("goudy old style",15,"bold"),bg="red",fg="white").place(x=430,y=500,width=120,height=30)
        
        #======= Employee Details ========================
        
        emp_frame=Frame(self.root,bd=4,relief=RIDGE)
        emp_frame.place(x=650,y=120,width=500,height=410)
        
        scrollx=Scrollbar(emp_frame,orient=HORIZONTAL)
        scrolly=Scrollbar(emp_frame,orient=VERTICAL)
        
        self.supplierTable=ttk.Treeview(emp_frame,columns=("invoice","name","contact","desc"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.supplierTable.xview)
        scrolly.config(command=self.supplierTable.yview)
        
        self.supplierTable.heading("invoice",text="Invoice")
        self.supplierTable.heading("name",text="Name")
        self.supplierTable.heading("contact",text="Contact No.")
        self.supplierTable.heading("desc",text="Description") 

        self.show()
        
        self.supplierTable["show"]="headings"
        
        self.supplierTable.column("invoice",width=90)
        self.supplierTable.column("name",width=100)
        self.supplierTable.column("contact",width=100)
        self.supplierTable.column("desc",width=100)
        self.supplierTable.pack(fill=BOTH,expand=1)
        self.supplierTable.bind("<ButtonRelease-1>",self.get_data)
        self.show()
#================ Functions ===============================        
    def add(self):
        con=sqlite3.connect(database=r'ims.db' )
        cur=con.cursor()
        try:
            if self.var_sup_invoice.get()=="":
                messagebox.showerror("Error","Invoice Must be Required",parent=self.root)
                
            else:
                cur.execute("Select * from supplier where invoice=?",(self.var_sup_invoice.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","Invoice No.  already asssigned , Try different Invoice No.")
                else:
                    cur.execute("Insert into supplier(invoice , name , contact , desc  ) values(?,?,?,?)",(
                                                    self.var_sup_invoice.get(),
                                                    self.var_name.get(),
                                                    self.var_contact.get(),
                                                    self.txt_desc.get('1.0',END),
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Supplier Added SUCCESSFULLY !!",parent=self.root)
                    # self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)

    def show(self):
        con=sqlite3.connect(database=r'ims.db' )
        cur=con.cursor()
        try:
            cur.execute("Select * from supplier")
            rows=cur.fetchall()
            self.supplierTable.delete(*self.supplierTable.get_children())
            for row in rows:
                self.supplierTable.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)
            
    def get_data(self,ev):
        f=self.supplierTable.focus()
        content=(self.supplierTable.item(f))
        row=content['values']
        self.var_sup_invoice.set(row[0])
        self.var_name.set(row[1])
        self.var_contact.set(row[2])
        self.txt_desc.delete('1.0',END)
        self.txt_desc.insert(END, row[3])
        
        
    def update(self):
        con=sqlite3.connect(database=r'ims.db' )
        cur=con.cursor()
        try:
            if self.var_sup_invoice.get()=="":
                messagebox.showerror("Error","Invoice Must be Required",parent=self.root)
                
            else:
                cur.execute("Select * from supplier where invoice=?",(self.var_sup_invoice.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid Invoice No. !!")
                else:
                    cur.execute("Update supplier set  name=? , contact=? ,  desc=? where invoice=?",(
                                                    self.var_name.get(),
                                                    self.var_contact.get(),
                                                    self.txt_desc.get('1.0',END),
                                                    self.var_sup_invoice.get()
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Supplier Updated SUCCESSFULLY !!",parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)
            
            
    def delete(self):
        con=sqlite3.connect(database=r'ims.db' )
        cur=con.cursor()
        try:
            if self.var_sup_invoice.get()=="":
                messagebox.showerror("Error","Invoice No. Must be Required",parent=self.root)
                
            else:
                op=messagebox.askyesno("CONFIRM","Do You Really want to DELETE ??",parent=self.root)
                if op==True:
                    cur.execute("Delete from supplier where invoice=?",(self.var_sup_invoice.get(),))
                    con.commit()
                    messagebox.showinfo("DELETE","Supplier Deleted SUCCESSFULLY !!",parent=self.root)
                    self.clear()
    
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)
            
    def clear(self):
        self.var_sup_invoice.set("")
        self.var_name.set("")
        self.var_contact.set("")
        self.txt_desc.delete('1.0',END)
        self.var_searchtxt.set("")
        self.show()
        
        
    def search(self):
            con=sqlite3.connect(database=r'ims.db' )
            cur=con.cursor()
            try:
                if self.var_searchtxt.get()=="":
                    messagebox.showerror("Error","Invoice No. must be required !!",parent=self.root)
                else:
                    cur.execute("Select * from supplier where invoice=?",(self.var_searchtxt.get(),))
                    row=cur.fetchone()
                    if row!=None:
                        self.supplierTable.delete(*self.supplierTable.get_children())   
                        self.supplierTable.insert('',END,values=row)
                    else:
                        messagebox.showerror("Error","No Record Found !!!",parent=self.root)
            except Exception as ex:
                messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)

if  __name__=="__main__":
    root=Tk()
    obj=supplierClass(root)
    root.mainloop()