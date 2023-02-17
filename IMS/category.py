from tkinter import *
from PIL import Image,ImageTk 
from tkinter import ttk,messagebox
import sqlite3

class categoryClass:
    def __init__(self,root):
        self.root=root
        self.root.title("Inventory Database Management   |   Developed By PRASHANT KUMAR  !!")
        self.root.geometry("1225x670+255+125")
        self.root.config(bg="#ecf8f9")
        self.root.focus_force()
        
        # =========All variables=========
        self.var_name=StringVar()
        self.var_cat_id=StringVar()
        
        title=Label(self.root,text="Manage Product Categories",font=("goudy old style" "bold",20 ,"bold"),bd=3,relief=RIDGE,bg="#184a45",fg="#ffffff").pack(side=TOP,fill=X,padx=10,pady=20)
        
        lbl_name=Label(self.root,text="Enter Category Name",font=("goudy old style" "bold",20 ,"bold"),bg="#ecf8f9",fg="#a52a2a").place(x=10,y=100)
        
        txt_supplier_invoice=Entry(self.root,textvariable=self.var_name,font=("goudy old style",20,),bg="lightyellow",fg="#00008b").place(x=330,y=100)
        
        btn_add=Button(self.root,text="ADD",command=self.add,cursor="hand2",font=("goudy old style",20,"bold"),bg="#4682b4",fg="white").place(x=650,y=100,width=130,height=35)
        
        btn_delete=Button(self.root,text="Delete",command=self.delete,cursor="hand2",font=("goudy old style",20,"bold"),bg="red",fg="white").place(x=820,y=100,width=120,height=35)
        
        # ======== Product Details ===========
        
        cat_frame=Frame(self.root,bd=4,relief=RIDGE)
        cat_frame.place(x=10,y=160,width=500,height=500)
        
        scrollx=Scrollbar(cat_frame,orient=HORIZONTAL)
        scrolly=Scrollbar(cat_frame,orient=VERTICAL)
        
        self.category_table=ttk.Treeview(cat_frame,columns=("cid","name",),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.category_table.xview)
        scrolly.config(command=self.category_table.yview)
        
        self.category_table.heading("cid",text="C ID")
        self.category_table.heading("name",text="Name")
        self.category_table["show"]="headings"
        
        self.category_table.column("cid",width=20)
        self.category_table.column("name",width=150)
        self.category_table.pack(fill=BOTH,expand=1)
        self.category_table.bind("<ButtonRelease-1>",self.get_data)   
        self.show()
        # ===== Images =====================
        self.im1=Image.open("D:\VS Studio Code\IMS\image/sale.jpg")
        self.im1=self.im1.resize((630,250))
        self.im1=ImageTk.PhotoImage(self.im1)
        
        self.lbl_im1=Label(self.root,image=self.im1,bd=3,relief=RAISED)
        self.lbl_im1.place(x=550,y=160)
        
        self.im2=Image.open("D:\VS Studio Code\IMS\image/cat.jpg")
        self.im2=self.im2.resize((630,240))
        self.im2=ImageTk.PhotoImage(self.im2)
        
        self.lbl_im2=Label(self.root,image=self.im2,bd=3,relief=RAISED)
        self.lbl_im2.place(x=550,y=420)
        
        # ========Functions==============
    def add(self):
        con=sqlite3.connect(database=r'ims.db' )
        cur=con.cursor()
        try:
            if self.var_name.get()=="":
                messagebox.showerror("Error","Category Name Must be Required",parent=self.root)
                
            else:
                cur.execute("Select * from category where name=?",(self.var_name.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","category Name  Already Present , Try different Name !!.")
                else:
                    cur.execute("Insert into category( name ) values(?)",(
                                                    
                                                    self.var_name.get(),
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Category Added SUCCESSFULLY !!",parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)

    def show(self):
        con=sqlite3.connect(database=r'ims.db' )
        cur=con.cursor()
        try:
            cur.execute("Select * from category")
            rows=cur.fetchall()
            self.category_table.delete(*self.category_table.get_children())
            for row in rows:
                self.category_table.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)
            
    def get_data(self,ev):
        f=self.category_table.focus()
        content=(self.category_table.item(f))
        row=content['values']
        self.var_cat_id.set(row[0])
        self.var_name.set(row[1])   
        
    def delete(self):
        con=sqlite3.connect(database=r'ims.db' )
        cur=con.cursor()
        try:
            if self.var_cat_id.get()=="":
                messagebox.showerror("Error","Please Select Category from List !!",parent=self.root)
                
            else:
                op=messagebox.askyesno("CONFIRM","Do You Really want to DELETE ??",parent=self.root)
                if op==True:
                    cur.execute("Delete from category where cid=?",(self.var_cat_id.get(),))
                    con.commit()
                    messagebox.showinfo("DELETE","Category Deleted SUCCESSFULLY !!",parent=self.root)
                    self.show()
                    self.var_cat_id.set("")
                    self.var_name.set("")
    
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)
        
if  __name__=="__main__":
    root=Tk()
    obj=categoryClass(root)
    root.mainloop()