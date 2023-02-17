from tkinter import *
from PIL import Image,ImageTk
import time
from employee import employeeClass
from supplier import supplierClass
from category import categoryClass
from product import productClass
from sales import salesClass
from tkinter import ttk,messagebox
import sqlite3
import os

class BMS:
    def __init__(self,root):
        self.root=root
        self.root.title("Inventory Database Management   |   Developed By PRASHANT KUMAR  !!")
        self.root.geometry("1900x1080+0+0")
        

        # ====Title of the Project======
        self.icon_title=PhotoImage(file="D:\VS Studio Code\IMS\image/logo1.png")
        title=Label(self.root,text="Inventory Database Management System",image=self.icon_title,compound=LEFT,font=("times new roman",40,"bold"),bg="#c7f1f4",fg="#fc2a99",anchor='w',padx=60).place(x=0,y=0,relwidth=1,height=70)
        # ==============Buttton Logout=============
        
        btn_logout=Button(self.root, text="Logout",command=self.logout, font=("times new roman",15,"bold"),bg="#f8dcfb",cursor="hand2").place(x=1350,y=10,height=50,width=100)
        
        # ================Time==========================
        self.lbl_clock=Label(self.root,text=" You are Heartly Welcomed by Prashant Kumar !!\t\t  Date: DD-MM-YYYY\t\t Time: HH-MM-SS\t\t",font=("times new roman",15),bg="#4d636d",fg="#ffffff")
        self.lbl_clock.place(x=0,y=70,relwidth=1,height=30)
        
        # ================LeftMenu=================
        
        self.MenuLogo=Image.open("D://VS Studio Code//IMS//image//menu_im.png")
        self.MenuLogo=self.MenuLogo.resize((250,350))
        self.MenuLogo=ImageTk.PhotoImage(self.MenuLogo)
        
        LeftMenu=Frame(self.root,bd=2,relief=RIDGE,bg="#ffffff")
        LeftMenu.place(x=0,y=102,width=250,height=700 )
        
        lbl_menuLogo=Label(LeftMenu,image=self.MenuLogo)
        lbl_menuLogo.pack(side=TOP,fill=X)
        
        lbl_menu=Label(LeftMenu, text="Menu", font=("times new roman",25,),bg="#f8dcfb").pack(side=TOP,fill=X)
        
        
        btn_employee=Button(LeftMenu, text="Employee",command=self.employee, font=("times new roman",20,"bold"),bg="skyblue",bd=5,cursor="hand2").pack(side=TOP,fill=X)
        
        btn_Suuplier=Button(LeftMenu, text="Supplier", command=self.supplier,font=("times new roman",20,"bold"),bg="skyblue",bd=5,cursor="hand2").pack(side=TOP,fill=X)
        
        btn_Catrgories=Button(LeftMenu, text="Categories",command=self.category, font=("times new roman",20,"bold"),bg="skyblue",bd=5,cursor="hand2").pack(side=TOP,fill=X)
        
        btn_Products=Button(LeftMenu, text="Products", command=self.product,font=("times new roman",20,"bold"),bg="skyblue",bd=5,cursor="hand2").pack(side=TOP,fill=X)
        
        btn_Sales=Button(LeftMenu, text="Sales",command=self.sales, font=("times new roman",20,"bold"),bg="skyblue",bd=5,cursor="hand2").pack(side=TOP,fill=X)
        
        
    
        #===============Content==============
        
        self.lbl_employee=Label(self.root,text="Total Employees\n[ 0 ]",bd=5,relief=RIDGE,bg="#f1dcfd",fg="#ef0289",font=("goudy old style",22,"bold"))
        self.lbl_employee.place(x=300,y=120,height=150,width=300)
        
        self.lbl_supplier=Label(self.root,text="Total Suppliers\n[ 0 ]",bd=5,relief=RIDGE,bg="#c8f889",fg="#ef0289",font=("goudy old style",22,"bold"))
        self.lbl_supplier.place(x=650,y=120,height=150,width=300)
        
        self.lbl_categories=Label(self.root,text="Total Categories\n[ 0 ]",bd=5,relief=RIDGE,bg="#a9fef6",fg="#ef0289",font=("goudy old style",22,"bold"))
        self.lbl_categories.place(x=1000,y=120,height=150,width=300)
        
        self.lbl_product=Label(self.root,text="Total Products\n[ 0 ]",bd=5,relief=RIDGE,bg="#fdeec3",fg="#ef0289",font=("goudy old style",22,"bold"))
        self.lbl_product.place(x=300,y=300,height=150,width=300)
        
        self.lbl_sales=Label(self.root,text="Total Sales\n[ 0 ]",bd=5,relief=RIDGE,bg="#fed4e7",fg="#ef0289",font=("goudy old style",22,"bold"))
        self.lbl_sales.place(x=650,y=300,height=150,width=300)
        
        # Footer
        lbl_footer=Label(self.root,text="IMS: Inventory Database Management System  | Developed by PRASHANT KUMAR\n For any Technical Query CONTACT 9122706809",font=("times new roman",18),bg="#008b8b",fg="#ffffff").pack(side=BOTTOM,fill=X)
        
        self.update_content()
        
# ===================================================================
    def employee(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=employeeClass(self.new_win)
        
    def supplier(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=supplierClass(self.new_win)
        
    def category(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=categoryClass(self.new_win)
        
    def product(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=productClass(self.new_win)
        
    def sales(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=salesClass(self.new_win)  


    def update_content(self):
        con=sqlite3.connect(database=r'ims.db' )
        cur=con.cursor()
        try:
            cur.execute('select * from product')
            product=cur.fetchall()
            self.lbl_product.config(text=f"Total Product\n[ {str(len(product))} ]")
            
            cur.execute('select * from supplier')
            supplier=cur.fetchall()
            self.lbl_supplier.config(text=f'Total Suppliers\n[ {str(len(supplier))} ]')
            
            cur.execute("select *  from category")
            category=cur.fetchall()
            self.lbl_categories.config(text=f'Total Categories\n[ {str(len(category))} ]')
            
            cur.execute('select * from employee')
            employee=cur.fetchall()
            self.lbl_employee.config(text=f'Total Employess\n[ {str(len(employee))} ]')
            
            bill=len(os.listdir("D:\VS Studio Code\IMS\Bills"))
            self.lbl_sales.config(text=f'Total Sales\n[ {str(bill)} ]')
            
            time_=time.strftime('%I:%M:%S')    
            date_=time.strftime('%d:%m:%Y')
            self.lbl_clock.config(text=f" You are Heartly Welcomed by Prashant Kumar !!\t\t  Date: {str(date_)}\t\t Time:{str(time_)}")   
            self.lbl_clock.after(200,self.update_content)
            
        except Exception as ex:
                messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)    
        
    def logout(self):
        self.root.destroy()
        os.system("python IMS/login.py")
    
    
if  __name__=="__main__":
    root=Tk()
    obj=BMS(root)
    root.resizable(True,False)
    root.mainloop()