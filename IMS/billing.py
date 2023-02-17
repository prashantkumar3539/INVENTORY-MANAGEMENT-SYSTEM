from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import sqlite3
import time
import os
import tempfile


class BillClass:
    def __init__(self,root):
        self.root=root
        self.root.title("Inventory Database Management   |   Developed By PRASHANT KUMAR  !!")
        self.root.geometry("1900x1080+0+0")




        # ====================All Variables ===================
        self.var_search=StringVar()
        self.var_cname=StringVar()
        self.var_contact=StringVar()
        self.cart_list=[]
        self.chk_print=0
        
        # ====Title of the Project======
        
        title=Label(self.root,text="Inventory Database Management System",font=("times new roman",40,"bold"),bg="#c7f1f4",fg="#fc2a99").place(x=0,y=0,relwidth=1,height=70)
        
        # ___Buttton Logout___
        
        btn_logout=Button(self.root, text="Logout",command=self.logout, font=("times new roman",15,"bold"),bg="#f8dcfb",cursor="hand2").place(x=1350,y=10,height=50,width=100)
        
        # # ___time____
        self.lbl_clock=Label(self.root,text=" You are Heartly Welcomed by Prashant Kumar !!\t\t  Date: DD-MM-YYYY\t\t Time: HH-MM-SS\t\t",font=("times new roman",15),bg="#4d636d",fg="#ffffff")
        self.lbl_clock.place(x=0,y=70,relwidth=1,height=30)
        
        
        #================Product Frame ===================
        
        ProductFrame1=Frame(self.root,bd=4,relief=RIDGE,bg="#f8f8ff")
        ProductFrame1.place(x=6,y=110,width=410,height=625)
        
        pTitle=Label(ProductFrame1,text="All Products",font=("Times New Roman",20,"bold"),bg="#ff7f50",fg="#f8f8ff").pack(side=TOP,fill=X)
        
        # ========== Product Search Frame================
        
        ProductFrame2=Frame(ProductFrame1,bd=2,relief=RIDGE,bg="#f8f8ff")
        ProductFrame2.place(x=2,y=38,width=398,height=100)
        
        
        lbl_search1=Label(ProductFrame2,text="Search Product | By Name",font=("Times New Roman",15,"bold"),bg="#f8f8ff",fg="#fc2a99").place(x=2,y=5)
        
        lbl_search=Label(ProductFrame2,text="Product Name",font=("Times New Roman",15,"bold"),bg="#f8f8ff",fg="#b94e48").place(x=5,y=40)
        
        txt_search=Entry(ProductFrame2,textvariable=self.var_search,font=("goudy old style",15),bg="lightyellow",fg="#00008b").place(x=135,y=45,width=150,height=25)
        
        btn_search=Button(ProductFrame2,text="Search",command=self.search,cursor="hand2",font=("goudy old style",17,"bold"),bg="#ff6fff",fg="white").place(x=295,y=43,width=90,height=28)
        
        btn_showall=Button(ProductFrame2,text="Show All",command=self.show,cursor="hand2",font=("goudy old style",17,"bold"),bg="#008b8b",fg="white").place(x=265,y=8,width=115,height=28)
        
        
        #======= Product Details  Frame ========================
        
        ProductFrame3=Frame(ProductFrame1,bd=4,relief=RIDGE)
        ProductFrame3.place(x=2,y=140,width=398,height=445)
        
        scrollx=Scrollbar(ProductFrame3,orient=HORIZONTAL)
        scrolly=Scrollbar(ProductFrame3,orient=VERTICAL)
        
        self.product_table=ttk.Treeview(ProductFrame3,columns=("pid","name","price","qty","status"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.product_table.xview)
        scrolly.config(command=self.product_table.yview)
        
        self.product_table.heading("pid",text="PID")
        self.product_table.heading("name",text="Name")
        self.product_table.heading("price",text="price")
        self.product_table.heading("qty",text="QTY") 
        self.product_table.heading("status",text="Status") 

        self.show()
        
        self.product_table["show"]="headings"
        
        self.product_table.column("pid",width=50)
        self.product_table.column("name",width=100)
        self.product_table.column("price",width=80)
        self.product_table.column("qty",width=70)
        self.product_table.column("status",width=80)
        self.product_table.pack(fill=BOTH,expand=1)
        self.product_table.bind("<ButtonRelease-1>",self.get_data)
        self.show()
        
        lbl_note=Label(ProductFrame1,text="NOTE !! Enetr 0 Quantity to Remove Product From Cart !!",font=("Times New Roman",13),bg="#f8f8ff",fg="red").pack(side=BOTTOM,fill=X)
        
        # ================Customer Frame ========================
        
        CustomerFrame=Frame(self.root,bd=4,relief=RIDGE,bg="#f8f8ff")
        CustomerFrame.place(x=450,y=110,width=560,height=90)
        
        cTitle=Label(CustomerFrame,text="Customer Details",font=("Times New Roman",20,"bold"),bg="#5f9ea0",fg="#f8f8ff").pack(side=TOP,fill=X)
        
        lbl_name=Label(CustomerFrame,text="Name",font=("Times New Roman",15,"bold"),bg="#f8f8ff",fg="#b94e48").place(x=5,y=45)
        
        txt_name=Entry(CustomerFrame,textvariable=self.var_cname,font=("goudy old style",15),bg="lightyellow",fg="#00008b").place(x=70,y=48,width=150)
        
        lbl_contact=Label(CustomerFrame,text="Contact",font=("Times New Roman",15,"bold"),bg="#f8f8ff",fg="#b94e48").place(x=250,y=45)
        
        txt_contact=Entry(CustomerFrame,textvariable=self.var_contact,font=("goudy old style",15),bg="lightyellow",fg="#00008b").place(x=335,y=48,width=150)
        
    
        
        # ===============Cal Cart Frame=====================
        
        Cal_Cart_Frame=Frame(self.root,bd=5,relief=RIDGE,bg="#f8f8ff")
        Cal_Cart_Frame.place(x=450,y=210,width=560,height=360)
        
        # ==============Calculator Frame===================
        
        self.var_cal_input=StringVar()
        
        Cal_Frame=Frame(Cal_Cart_Frame,bd=6,relief=RIDGE,bg="#f8f8ff")
        Cal_Frame.place(x=5,y=9,width=275,height=340)
        
        txt_cal_input=Entry(Cal_Frame,textvariable=self.var_cal_input,font=("arial",20),bg="#f2f3f4",fg="#ff0000",bd=9,width=16,relief=GROOVE,state="readonly",justify=RIGHT)
        txt_cal_input.grid(row=0,columnspan=4)
        
        # ==========Buttons=================================
        
        btn_7=Button(Cal_Frame,text="7",font=("arial",15,"bold"),bg="#ffddf4",command=lambda:self.get_input(7),bd=5,width=4,pady=12,cursor="hand2").grid(row=1,column=0)
        btn_8=Button(Cal_Frame,text="8",font=("arial",15,"bold"),bg="#ffddf4",command=lambda:self.get_input(8),bd=5,width=4,pady=12,cursor="hand2").grid(row=1,column=1)
        btn_9=Button(Cal_Frame,text="9",font=("arial",15,"bold"),bg="#ffddf4",command=lambda:self.get_input(9),bd=5,width=4,pady=12,cursor="hand2").grid(row=1,column=2)
        btn_sum=Button(Cal_Frame,text="+",font=("arial",15,"bold"),bg="#ffddf4",command=lambda:self.get_input("+"),bd=5,width=4,pady=12,cursor="hand2").grid(row=1,column=3)
        
        
        btn_4=Button(Cal_Frame,text="4",font=("arial",15,"bold"),bg="#ffddf4",command=lambda:self.get_input(4),bd=5,width=4,pady=12,cursor="hand2").grid(row=2,column=0)
        btn_5=Button(Cal_Frame,text="5",font=("arial",15,"bold"),bg="#ffddf4",command=lambda:self.get_input(5),bd=5,width=4,pady=12,cursor="hand2").grid(row=2,column=1)
        btn_6=Button(Cal_Frame,text="6",font=("arial",15,"bold"),bg="#ffddf4",command=lambda:self.get_input(6),bd=5,width=4,pady=12,cursor="hand2").grid(row=2,column=2)
        btn_sub=Button(Cal_Frame,text="-",font=("arial",15,"bold"),bg="#ffddf4",command=lambda:self.get_input("-"),bd=5,width=4,pady=12,cursor="hand2").grid(row=2,column=3)
        
        
        btn_1=Button(Cal_Frame,text="1",font=("arial",15,"bold"),bg="#ffddf4",command=lambda:self.get_input(1),bd=5,width=4,pady=12,cursor="hand2").grid(row=3,column=0)
        btn_2=Button(Cal_Frame,text="2",font=("arial",15,"bold"),bg="#ffddf4",command=lambda:self.get_input(2),bd=5,width=4,pady=12,cursor="hand2").grid(row=3,column=1)
        btn_3=Button(Cal_Frame,text="3",font=("arial",15,"bold"),bg="#ffddf4",command=lambda:self.get_input(3),bd=5,width=4,pady=12,cursor="hand2").grid(row=3,column=2)
        btn_mul=Button(Cal_Frame,text="*",font=("arial",15,"bold"),bg="#ffddf4",command=lambda:self.get_input("*"),bd=5,width=4,pady=12,cursor="hand2").grid(row=3,column=3)
        
        
        btn_c=Button(Cal_Frame,text="C",font=("arial",15,"bold"),bg="#ffddf4",command=self.clear,fg="red",bd=5,width=4,pady=10,cursor="hand2").grid(row=4,column=0)
        btn_0=Button(Cal_Frame,text="0",font=("arial",15,"bold"),bg="#ffddf4",command=lambda:self.get_input(0),bd=5,width=4,pady=10,cursor="hand2").grid(row=4,column=1)
        btn_eq=Button(Cal_Frame,text="=",font=("arial",16,"bold"),bg="#ffddf4",command=self.perform_cal,bd=5,width=4,pady=10,cursor="hand2").grid(row=4,column=2)
        btn_div=Button(Cal_Frame,text="/",font=("arial",16,"bold"),bg="#ffddf4",command=lambda:self.get_input("/"),bd=5,width=4,pady=10,cursor="hand2").grid(row=4,column=3)
        
        
        
        
        
        #======= Customers Details ========================
        
        # ======Cart Frame================
        cart_Frame=Frame(Cal_Cart_Frame,bd=4,relief=RIDGE)
        cart_Frame.place(x=280,y=9,width=275,height=340)
        
        self.cartTitle=Label(cart_Frame,text="Cart\t Total Products: [0]",font=("Times New Roman",15,"bold"),bg="#ff69b4",fg="#f8f8ff")
        self.cartTitle.pack(side=TOP,fill=X)
        
        scrollx=Scrollbar(cart_Frame,orient=HORIZONTAL)
        scrolly=Scrollbar(cart_Frame,orient=VERTICAL)
        
        self.CartTable=ttk.Treeview(cart_Frame,columns=("pid","name","price","qty"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        # ,"status"
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.CartTable.xview)
        scrolly.config(command=self.CartTable.yview)
        
        self.CartTable.heading("pid",text="PID")
        self.CartTable.heading("name",text="Name")
        self.CartTable.heading("price",text="price")
        self.CartTable.heading("qty",text="QTY") 
        # self.CartTable.heading("status",text="Status") 
        self.CartTable["show"]="headings"
        self.CartTable.column("pid",width=60)
        self.CartTable.column("name",width=80)
        self.CartTable.column("price",width=70)
        self.CartTable.column("qty",width=40)
        # self.CartTable.column("status",width=50)
        self.CartTable.pack(fill=BOTH,expand=1)
        self.CartTable.bind("<ButtonRelease-1>",self.get_data_cart)
        # self.show()
        
        
        # ==============ADD Cart  Widget Frame===================
        
        self.var_pid=StringVar()
        self.var_pname=StringVar()
        self.var_price=StringVar()
        self.var_qty=StringVar()
        self.var_stock=StringVar()
        
        Add_Cart_Widget_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="#f8f8ff")
        Add_Cart_Widget_Frame.place(x=450,y=575,width=560,height=160)
        
        lbl_p_name=Label(Add_Cart_Widget_Frame,text="Product Name",font=("Times New Roman",15,"bold"),bg="#f8f8ff",fg="#b94e48").place(x=5,y=5)
        
        txt_p_name=Entry(Add_Cart_Widget_Frame,textvariable=self.var_pname,font=("goudy old style",15),bg="lightyellow",fg="#00008b",state='readonly').place(x=5,y=45,width=140,height=25)
        
        lbl_p_price=Label(Add_Cart_Widget_Frame,text="Price Per Qty",font=("Times New Roman",15,"bold"),bg="#f8f8ff",fg="#b94e48").place(x=215,y=5)
        
        txt_p_price=Entry(Add_Cart_Widget_Frame,textvariable=self.var_price,font=("goudy old style",15),bg="lightyellow",fg="#00008b",state='readonly').place(x=205,y=45,width=140,height=25)
        
        lbl_p_qty=Label(Add_Cart_Widget_Frame,text="Quantity",font=("Times New Roman",15,"bold"),bg="#f8f8ff",fg="#b94e48").place(x=415,y=5)
        
        txt_p_qty=Entry(Add_Cart_Widget_Frame,textvariable=self.var_qty,font=("goudy old style",15),bg="lightyellow",fg="#00008b").place(x=405,y=45,width=140,height=25)
        
        self.lbl_instock=Label(Add_Cart_Widget_Frame,text="In Stack []",font=("Times New Roman",15,"bold"),bg="#f8f8ff",fg="#b94e48")
        self.lbl_instock.place(x=5,y=90)
        
        btn_clear_cart=Button(Add_Cart_Widget_Frame,text="Clear Cart",command=self.clear_cart,cursor="hand2",font=("Times New Roman",17,"bold"),bg="#ff1493",fg="white").place(x=170,y=85,width=130,height=30)
        
        btn_add_cart=Button(Add_Cart_Widget_Frame,text="ADD | Update Cart",command=self.add_update_cart,cursor="hand2",font=("Times New Roman",17,"bold"),bg="#008080",fg="white").place(x=325,y=85,width=210,height=30)
        
        # btn_update_cart=Button(Add_Cart_Widget_Frame,text="Update",cursor="hand2",font=("goudy old style",17,"bold"),bg="#545aa7",fg="white").place(x=420,y=85,width=100,height=30)
        
        
        # ======= Billing Frame =============================
        billFrame=Frame(self.root,bd=4,relief=RIDGE,bg="#f8f8ff")
        billFrame.place(x=1030,y=110,width=450,height=460)
        
        bTitle=Label(billFrame,text="Customer Bill Area",font=("Times New Roman",20,"bold"),bg="#ff69b4",fg="#f8f8ff").pack(side=TOP,fill=X)
        
        scrolly=Scrollbar(billFrame,orient=VERTICAL)
        self.txt_bill_area=Text(billFrame,yscrollcommand=scrolly.set)
        scrolly.pack(side=RIGHT,fill=Y)
        self.txt_bill_area.pack(fill=BOTH,expand=1)
        scrolly.config(command=self.txt_bill_area.yview)
        
        
        
        # ======= Billing Button Frame =============================
        billMenuFrame=Frame(self.root,bd=4,relief=RIDGE,bg="#f8f8ff")
        billMenuFrame.place(x=1030,y=575,width=450,height=160)
        
        
        self.lbl_amnt=Label(billMenuFrame,text="Total Amount\n ",font=("Times New Roman",15,"bold"),bd=2,relief=RIDGE,bg="#dcd0ff",fg="#b94e48")
        self.lbl_amnt.place(x=5,y=5,width=140,height=90)
        
        self.lbl_discount=Label(billMenuFrame,text="Total Discount\n 5%",font=("Times New Roman",15,"bold"),bd=2,relief=RIDGE,bg="#c9ffe5",fg="#b94e48")
        self.lbl_discount.place(x=155,y=5,width=135,height=90)
        
        self.lbl_net_pay=Label(billMenuFrame,text="Total Amount\n ",font=("Times New Roman",15,"bold"),bd=2,relief=RIDGE,bg="#ffddf4",fg="#b94e48")
        self.lbl_net_pay.place(x=300,y=5,width=140,height=90)
        
        btn_print=Button(billMenuFrame,text="Print",command=self.print_bill,cursor="hand2",font=("Times New Roman",17,"bold"),bg="#00b7eb",fg="#ffffff").place(x=15,y=110,width=100,height=40)
        
        btn_clear_all=Button(billMenuFrame,text="Clear All ",command=self.clear_all,cursor="hand2",font=("Times New Roman",17,"bold"),bg="#ff1493",fg="white").place(x=135,y=110,width=120,height=40)
        
        btn_generate_bill=Button(billMenuFrame,text="Generate Bill",command=self.generate_bill,cursor="hand2",font=("Times New Roman",17,"bold"),bg="#008b8b",fg="white").place(x=280,y=110,width=150,height=40)
        
        # ======================Footer================
        lbl_footer=Label(self.root,text="IMS: Inventory Database Management System  | Developed by PRASHANT KUMAR\n For any Technical Query CONTACT 9122706809",font=("times new roman",20),bd=5,relief=RAISED,bg="#008b8b",fg="#ffffff").place(x=2,y=770,width=1700,height=80)
        
        self.show()
        self.update_date_time()
# =============== Functions for Calculator ====================================

    def get_input(self,num):
        xnum=self.var_cal_input.get()+str(num)
        self.var_cal_input.set(xnum)
        
    def clear(self):
        self.var_cal_input.set("")
        
        
    def perform_cal(self):
        result=self.var_cal_input.get()
        self.var_cal_input.set(eval(result))
        
        
        # =======Functions ===========
        
    def show(self):
        con=sqlite3.connect(database=r'ims.db' )
        cur=con.cursor()
        try:
            cur.execute("Select pid,name,price,qty,status from product where status='Active' ")
            rows=cur.fetchall()
            self.product_table.delete(*self.product_table.get_children())
            for row in rows:
                self.product_table.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)   
    
    def search(self):
            con=sqlite3.connect(database=r'ims.db' )
            cur=con.cursor()
            try:
                if self.var_search.get()=="":
                    messagebox.showerror("Error"," Search Input should be Required !!",parent=self.root)
                else:
                    cur.execute("select pid,name,price,qty,status from product where name LIKE '%"+self.var_search.get()+"%' and status='Active' ")
                    rows=cur.fetchall()
                    if len(rows)!=0:
                        self.product_table.delete(*self.product_table.get_children())
                        for row in rows:
                            self.product_table.insert('',END,values=row)
                    else:
                        messagebox.showerror("Error","No Record Found !!!",parent=self.root)
            except Exception as ex:
                messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)

    def get_data(self,ev):
        f=self.product_table.focus()
        content=(self.product_table.item(f))
        row=content['values']
        self.var_pid.set(row[0])
        self.var_pname.set(row[1])
        self.var_price.set(row[2])
        self.lbl_instock.config(text=f"In Stock[{str(row[3])}]")
        self.var_stock.set(row[3])
        self.var_qty.set("1")
        
        
    def get_data_cart(self,ev):
        f=self.CartTable.focus()
        content=(self.CartTable.item(f))
        row=content['values']
        self.var_pid.set(row[0])
        self.var_pname.set(row[1])
        self.var_price.set(row[2])
        self.var_qty.set(row[3])
        self.lbl_instock.config(text=f"In Stock[{str(row[4])}]")
        self.var_stock.set(row[4])
        
        
    def add_update_cart(self):
        if self.var_pid.get()=="":
            messagebox.showerror("Error","Select the Product from List !!",parent=self.root)
        elif self.var_qty.get()=="":
            messagebox.showerror("Error","Fill The Quantity !!")
        elif int(self.var_qty.get())>int(self.var_stock.get()):
            messagebox.showerror("Warning","Quantity is less than what you have Entered  !!\n Please Try to enter the quantity within item present in Stock !!")
        else:
            # price_cal=int(self.var_qty.get())*float(self.var_price.get())
            # price_cal=float(price_cal)
            price_cal=self.var_price.get()
            cart_data=[self.var_pid.get(),self.var_pname.get(),price_cal,self.var_qty.get(),self.var_stock.get()]
            # self.cart_list.append(cart_data)
            # ======Update Cart ====================
            present='no'
            index_=0
            for row in self.cart_list:
                if self.var_pid.get()==row[0]:
                    present='yes'
                    break
                index_ +=1
            if present=='yes':
                op=messagebox.askyesno("Confirm !!","Product Already Present in the Cart  !!! \n Do You Want to Update | Remove from the Cart ?? ",parent=self.root)
                if op==True:
                    if self.var_qty.get()=="0":
                        self.cart_list.pop(index_)
                    else:
                        # self.cart_list[index_][2]=price_cal  # for updating the rice
                        self.cart_list[index_][3]=self.var_qty.get()  # for updating the Quantity
            else:
                self.cart_list.append(cart_data)
                
            self.show_cart()
            self.bill_updates()
    
    def show_cart(self):
        try:
            self.CartTable.delete(*self.CartTable.get_children())
            for row in self.cart_list:
                self.CartTable.insert("", END,values=row)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)
            
    def bill_updates(self):
        self.bill_amnt=0
        self.net_pay=0
        self.discount=0
        for row in self.cart_list:
            self.bill_amnt=self.bill_amnt+(float(row[2])*int(row[3]))
        self.discount=(self.bill_amnt*5)/100   
        self.net_pay=self.bill_amnt-self.discount
        self.lbl_amnt.config(text=f"Bill Amount\n{str(self.bill_amnt)}")    
        self.lbl_net_pay.config(text=f"Net Amount\n{str(self.net_pay)}")    
        self.cartTitle.config(text=f"Cart\t Total  Product : [{str(len(self.cart_list))}]")    
        
        
    def generate_bill(self):
        if self.var_cname.get()=="" or self.var_contact.get()=="":
            messagebox.showerror("Error","Please Fill the Customer Details !!",parent=self.root)
        elif len(self.cart_list)=="":
            messagebox.showerror("Error","Please Add the Products to Cart !!",parent=self.root)
        else:
            # =======Bill Top=========
            self.bill_top()
            # =======Bill Middle=========
            self.bill_middle()
            # =======Bill Bottom=========
            self.bill_bottom()
            
            fp=open(f'D:\VS Studio Code\IMS\Bills/{str(self.invoice)}.txt','w')
            fp.write(self.txt_bill_area.get('1.0',END))
            fp.close()
            messagebox.showinfo("Saved !!","File has Saved Successfully !!\n And Bill is generated Successfully !!!")
            self.chk_print=1

    def bill_top(self):
        self.invoice=int(time.strftime("%H%M%S"))+int(time.strftime("%d%m%Y"))
        bill_top_temp=f'''
\t\tPrashant's Inventory
\t Phone Num. 9122706809 , DBPUR - 561203
{str("-"*48)}
 Customer Name :{self.var_cname.get()}
 Phone No.  : {self.var_contact.get()}
 Bill No. {str(self.invoice)}\t\t\t Date: {str(time.strftime("%d-%m-%Y"))}
{str("-"*48)}
 Product Name \t\t\t QTY \t   Price
{str("-"*48)}
    '''
        self.txt_bill_area.delete("1.0",END)
        self.txt_bill_area.insert("1.0",bill_top_temp)
            
    def bill_bottom(self):
        bill_bottom_temp=f'''
{str("-"*48)}
 Bill Amount\t\t\t\t   Rs.{self.bill_amnt}
 Dicount\t\t\t\t   Rs.{self.discount}
 {str("-"*48)}
 Net Pay\t\t\t\t   Rs.{self.net_pay}
 
 \tTHANKS FOR SHOPPING , HAVE A GREAT DAY 
 \tAND VISIT AGAIN !!
 \tWE ARE ALWAYS TO HELP YOU !!!
        '''
        self.txt_bill_area.insert(END,bill_bottom_temp)     
        
    def bill_middle(self):
        con=sqlite3.connect(database=r'ims.db' )
        cur=con.cursor()
        try:
            for row in self.cart_list:
                pid=row[0]
                name=row[1]
                qty=int(row[4])-int(row[3])
                if int(row[3])==int(row[4]):
                    status="Inactive"
                if int(row[3])!=int(row[4]):
                    status="Active"
                price=float(row[2])*int(row[3])
                price=str(price)
                self.txt_bill_area.insert(END,"\n "+name+"\t\t\t  "+(row[3])+"\t   Rs. "+price)
                # == Updating the Quantity in Product Table
                cur.execute('Update product set qty=?,status=? where pid=?',(
                    qty,
                    status,
                    pid
                ))
                con.commit()
            con.close()
            self.show()
                
        except Exception as ex:
                messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)

    def clear_cart(self):
        self.var_pid.set("")
        self.var_pname.set("")
        self.var_price.set("")
        self.var_qty.set("")
        self.lbl_instock.config(text=f"In Stock")
        self.var_stock.set("")
        
    def clear_all(self):
        del self.cart_list[:]
        self.var_cname.set("")
        self.var_contact.set("")
        self.txt_bill_area.delete("1.0",END)
        self.cartTitle.config(text="Cart\t Total Products: [0]")
        self.var_search.set("")
        self.clear_cart()
        self.show()
        self.show_cart()
        self.chk_print=0
            
        
    def update_date_time(self):
        time_=time.strftime('%I:%M:%S')    
        date_=time.strftime('%d:%m:%Y')
        self.lbl_clock.config(text=f" You are Heartly Welcomed by Prashant Kumar !!\t\t  Date: {str(date_)}\t\t Time:{str(time_)}")   
        self.lbl_clock.after(200,self.update_date_time)
        
        
    def print_bill(self):
        if self.chk_print==1:
            messagebox.showinfo("Print !!","Please wait while printing the Bill Receipt !!",parent=self.root)
            new_file=tempfile.mktemp('.txt')
            open(new_file,'w').write(self.txt_bill_area.get('1.0',END))
            os.startfile(new_file,'print')
        else:
            messagebox.showerror("Print !!","Please Generate the Bill ,To Print the  !!")
        
    def logout(self):
        self.root.destroy()
        os.system("python IMS/login.py")    
        
        
        
            
if  __name__=="__main__":
    root=Tk()
    obj=BillClass(root)
    root.mainloop()