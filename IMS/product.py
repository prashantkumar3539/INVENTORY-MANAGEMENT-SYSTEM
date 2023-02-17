from tkinter import *
from PIL import Image,ImageTk 
from tkinter import ttk,messagebox
import sqlite3

class productClass:
    def __init__(self,root):
        self.root=root
        self.root.title("Inventory Database Management    |   Developed By PRASHANT KUMAR  !!")
        self.root.geometry("1225x670+255+125")
        self.root.config(bg="#ecf8f9")
        self.root.focus_force()
        # ======================
        #  All variables========================
        self.var_searchby=StringVar()
        self.var_searchtxt=StringVar()
        self.var_cat=StringVar()
        self.var_pid=StringVar()
        self.var_sup=StringVar()
        self.var_name=StringVar()
        self.var_price=StringVar()
        self.var_qty=StringVar()
        self.var_status=StringVar()
        self.cat_list=[]
        self.sup_list=[]
        self.fetch_cat_and_sup()
        
        
    # ==== Frame ======================
        prouct_Frame=Frame(self.root,bd=2,relief=RIDGE,bg="#f8f8ff")
        prouct_Frame.place(x=10,y=10,width=500,height=650)
        
    # =======Title===============
        title=Label(prouct_Frame,text="Manage Products Details",font=("goudy old style" ,25,"bold"),bd=3,bg="#00008b",fg="#f8f8ff").pack(side=TOP,fill=X)
        lbl_category=Label(prouct_Frame,text="Category",font=("times new roman" ,18,),bd=3,bg="#f8f8ff").place(x=30,y=60)
        lbl_supplier=Label(prouct_Frame,text="Supplier",font=("times new roman" ,18,),bd=3,bg="#f8f8ff").place(x=30,y=120)
        lbl_product=Label(prouct_Frame,text="Name",font=("times new roman" ,18,),bd=3,bg="#f8f8ff").place(x=30,y=180)
        lbl_price=Label(prouct_Frame,text="Price",font=("times new roman" ,18,),bd=3,bg="#f8f8ff").place(x=30,y=240)
        lbl_quantity=Label(prouct_Frame,text="Quantity",font=("times new roman" ,18,),bd=3,bg="#f8f8ff").place(x=30,y=300)
        lbl_status=Label(prouct_Frame,text="Status",font=("times new roman" ,18,),bd=3,bg="#f8f8ff").place(x=30,y=360)
            
        cmb_cat=ttk.Combobox(prouct_Frame,textvariable=self.var_cat,values=self.cat_list,state='readonly',justify=CENTER,font=("goudy old style", 15,"bold"))
        cmb_cat.place(x=150,y=60,width=200)
        cmb_cat.current(0)
        
        cmb_sup=ttk.Combobox(prouct_Frame,textvariable=self.var_sup,values=self.sup_list,state='readonly',justify=CENTER,font=("goudy old style", 15,"bold"))
        cmb_sup.place(x=150,y=120,width=200)
        cmb_sup.current(0)
        
        txt_sup=Entry(prouct_Frame,textvariable=self.var_name,bg="lightyellow",fg="#000039",font=("goudy old style", 18)).place(x=150,y=180,width=200)
        txt_price=Entry(prouct_Frame,textvariable=self.var_price,bg="lightyellow",fg="#000039",font=("goudy old style", 18)).place(x=150,y=240,width=200)
        txt_qty=Entry(prouct_Frame,textvariable=self.var_qty,bg="lightyellow",fg="#000039",font=("goudy old style", 18)).place(x=150,y=300,width=200)
        
        cmb_status=ttk.Combobox(prouct_Frame,textvariable=self.var_status,values=("Active","Inactive"),state='readonly',justify=CENTER,font=("goudy old style", 15,"bold"))
        cmb_status.place(x=150,y=360,width=200)
        cmb_status.current(0)
        
        btn_add=Button(self.root,command=self.add,text="Save",cursor="hand2",font=("goudy old style",15,"bold"),bg="#4682b4",fg="white").place(x=50,y=500,width=100,height=30)
        
        btn_update=Button(self.root,command=self.update,text="Update",cursor="hand2",font=("goudy old style",15,"bold"),bg="#228b22",fg="white").place(x=160,y=500,width=100,height=30)
        
        btn_delete=Button(self.root,command=self.delete,text="Delete",cursor="hand2",font=("goudy old style",15,"bold"),bg="#f94d00",fg="white").place(x=270,y=500,width=100,height=30)
        
        btn_clear=Button(self.root,command=self.clear,text="Clear",cursor="hand2",font=("goudy old style",15,"bold"),bg="red",fg="white").place(x=380,y=500,width=100,height=30)

        searchFrame=LabelFrame(self.root,text="Search ",font=("goudy old style",15,"bold"),bd=4,relief=RIDGE,bg="#ecf8f9",fg="#f30f0f")
        searchFrame.place(x=550,y=10,width=600,height=70)
        
        # ==========Option================
        cmb_search=ttk.Combobox(searchFrame,textvariable=self.var_searchby,values=("Select","Name","Category","Supplier"),state='readonly',justify=CENTER,font=("goudy old style", 13,"bold"))
        cmb_search.place(x=10,y=10,width=180)
        cmb_search.current(0)
        
        txt_search=Entry(searchFrame,textvariable=self.var_searchtxt,font=("goudy old style",15,"bold"),bg="lightyellow",fg="#f51435").place(x=200,y=10)
        
        btn_search=Button(searchFrame,command=self.search,text="Search",cursor="hand2",font=("goudy old style",15,"bold"),bg="#ffdab9",fg="#ff00ff").place(x=410,y=8,width=150,height=30)
        
        #======= Product Details Tree  View ========================
        
        p_frame=Frame(self.root,bd=4,relief=RIDGE)
        p_frame.place(x=550,y=120,width=620,height=540)
        
        scrollx=Scrollbar(p_frame,orient=HORIZONTAL)
        scrolly=Scrollbar(p_frame,orient=VERTICAL)
        
        self.product_table=ttk.Treeview(p_frame,columns=("pid","Category","Supplier","name","price","qty","status"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.product_table.xview)
        scrolly.config(command=self.product_table.yview)
        
        self.product_table.heading("pid",text="P ID")
        self.product_table.heading("Category",text="Category")
        self.product_table.heading("Supplier",text="Supplier")
        self.product_table.heading("name",text="Product Name")
        self.product_table.heading("price",text="Price")
        self.product_table.heading("qty",text="Quantity")
        self.product_table.heading("status",text="Status") 

        self.product_table["show"]="headings"
        
        self.product_table.column("pid",width=35)
        self.product_table.column("Category",width=85)
        self.product_table.column("Supplier",width=85)
        self.product_table.column("name",width=90)
        self.product_table.column("price",width=85)
        self.product_table.column("qty",width=85)
        self.product_table.column("status",width=85)
        self.product_table.pack(fill=BOTH,expand=1)
        self.product_table.bind("<ButtonRelease-1>",self.get_data)
        # self.product_table.bind("<ButtonRelease-1>",self.get_data)
        self.show()
        
#================ Functions ===============================        
    
    def fetch_cat_and_sup(self):
        
        con=sqlite3.connect(database=r'ims.db' )
        cur=con.cursor()
        try:
# ==================================get data from category========
            cur.execute("select name from category")
            cat=cur.fetchall()
            self.cat_list.append("Empty")
            if len(cat)>0:
                del self.cat_list[:]
                self.cat_list.append("Select")
                for i in cat:
                    self.cat_list.append(i[0])
# ==================================get data from supplier========
            cur.execute("select name from supplier")
            sup=cur.fetchall()
            self.sup_list.append("Empty")
            if len(sup)>0:
                del self.sup_list[:]
                self.sup_list.append("Select")
                for i in sup:
                    self.sup_list.append(i[0])
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)
        
        
    def add(self):
        con=sqlite3.connect(database=r'ims.db' )
        cur=con.cursor()
        try:
            if self.var_cat.get()=="Select" or self.var_cat.get()=="Empty" or self.var_sup.get()=="Select" or  self.var_sup.get()=="Empty"  or self.var_name.get()=="":
                messagebox.showerror("Error","Fill the Required Fields",parent=self.root)
                
            else:
                cur.execute("Select * from product where name=?",(self.var_name.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","Product is  Already Present , Try Different ")
                else:
                    cur.execute("Insert into product( Category , Supplier , name , price , qty , status ) values(?,?,?,?,?,?)",(
                                                    self.var_cat.get(),
                                                    self.var_sup.get(),
                                                    self.var_name.get(),
                                                    self.var_price.get(),
                                                    self.var_qty.get(),
                                                    self.var_status.get(),
                                                
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Product Added SUCCESSFULLY !!",parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)

    def show(self):
        con=sqlite3.connect(database=r'ims.db' )
        cur=con.cursor()
        try:
            cur.execute("Select * from product")
            rows=cur.fetchall()
            self.product_table.delete(*self.product_table.get_children())
            for row in rows:
                self.product_table.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)
            
    def get_data(self,ev):
        f=self.product_table.focus()
        content=(self.product_table.item(f))
        row=content['values']
        self.var_pid.set(row[0])
        self.var_cat.set(row[1])
        self.var_sup.set(row[2])
        self.var_name.set(row[3])
        self.var_price.set(row[4])
        self.var_qty.set(row[5])
        self.var_status.set(row[6])

        
        
    def update(self):
        con=sqlite3.connect(database=r'ims.db' )
        cur=con.cursor()
        try:
            if self.var_pid.get()=="":
                messagebox.showerror("Error","Please Select the Product",parent=self.root)
                
            else:
                cur.execute("Select * from product where pid=?",(self.var_pid.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid Product")
                else:
                    cur.execute("Update product set  Category=? , Supplier=? , name=? , price=? , qty=? , status=? where pid=?",(
                                                    self.var_cat.get(),
                                                    self.var_sup.get(),
                                                    self.var_name.get(),
                                                    self.var_price.get(),
                                                    self.var_qty.get(),
                                                    self.var_status.get(),
                                                    self.var_pid.get()
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Product Updated SUCCESSFULLY !!",parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)
            
            
    def delete(self):
        con=sqlite3.connect(database=r'ims.db' )
        cur=con.cursor()
        try:
            if self.var_pid.get()=="":
                messagebox.showerror("Error","Please Select the Product !!",parent=self.root)
                
            else:
                op=messagebox.askyesno("CONFIRM","Do You Really want to DELETE ??",parent=self.root)
                if op==True:
                    cur.execute("Delete from product where pid=?",(self.var_pid.get(),))
                    con.commit()
                    messagebox.showinfo("DELETE","Product  Deleted SUCCESSFULLY !!",parent=self.root)
                    self.clear()
    
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)
            
    def clear(self):
        self.var_pid.set("")
        self.var_sup.set("Select")
        self.var_cat.set("Select")
        self.var_name.set("")
        self.var_price.set("")
        self.var_qty.set("")
        self.var_status.set("Active")
        self.var_searchtxt.set("")
        self.var_searchtxt.set("Select")
        self.show()
        
        
    def search(self):
            con=sqlite3.connect(database=r'ims.db' )
            cur=con.cursor()
            try:
                if self.var_searchby.get()=="Select":
                    messagebox.showerror("Error","Select a valid Option",parent=self.root)
                elif self.var_searchtxt.get()=="":
                    messagebox.showerror("Error"," Search Input should be Required !!",parent=self.root)
                else:
                    cur.execute("Select * from product where "+self.var_searchby.get()+" LIKE '%"+self.var_searchtxt.get()+"%'")
                    rows=cur.fetchall()
                    if len(rows)!=0:
                        self.product_table.delete(*self.product_table.get_children())
                        for row in rows:
                            self.product_table.insert('',END,values=row)
                    else:
                        messagebox.showerror("Error","No Record Found !!!",parent=self.root)
            except Exception as ex:
                messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)


        
if  __name__=="__main__":
    root=Tk()
    obj=productClass(root)
    root.mainloop()