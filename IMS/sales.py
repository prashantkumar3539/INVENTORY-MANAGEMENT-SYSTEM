from tkinter import *
from PIL import Image,ImageTk 
from tkinter import ttk,messagebox
import sqlite3
import os

class salesClass:
    def __init__(self,root):
        self.root=root
        self.root.title("Inventory Database Management   |   Developed By PRASHANT KUMAR  !!")
        self.root.geometry("1225x670+255+125")
        self.root.config(bg="#ecf8f9")
        self.root.focus_force()
        
        #  All variables========================
        self.var_invoice=StringVar()
        self.bill_list=[]
        self.var_searchtxt=StringVar()
        
        
        title=Label(self.root,text="View Customer Bills",font=("goudy old style" ,25,"bold"),bd=3,bg="#008080",fg="#f8f8ff",relief=RIDGE).pack(side=TOP,fill=X,padx=10,pady=20)
        
        lbl_invoice=Label(self.root,text="Invoice no.",font=("goudy old style" "bold",15 ,"bold"),bg="#ecf8f9",fg="#a52a2a").place(x=10,y=100)
        
        txt_invoice=Entry(self.root,textvariable=self.var_invoice,font=("Times New Roman",15,),bg="lightyellow",fg="#00008b").place(x=140,y=100)
        
        btn_search=Button(self.root,text="Search",command=self.search,cursor="hand2",font=("Times New Roman",18),bg="#4682b4",fg="white").place(x=350,y=100,width=100,height=28)
        
        btn_clear=Button(self.root,text="Clear",command=self.clear,cursor="hand2",font=("Times New Roman",18),bg="red",fg="white").place(x=460,y=100,width=120,height=28)
        
        # ======== Bill Lists============
        sales_Frame=Frame(self.root,bd=2,relief=RIDGE)
        sales_Frame.place(x=30,y=140,width=270,height=450)
        
        scrolly=Scrollbar(sales_Frame,orient=VERTICAL)
        self.Sales_List=Listbox(sales_Frame,font=("Times New Roman",15),bg="#f8f8ff",yscrollcommand=scrolly.set)
        scrolly.config(command=self.Sales_List.yview)
        self.Sales_List.pack(fill=BOTH,expand=1)
        
        self.Sales_List.bind("<ButtonRelease-1>",self.get_data)
        
        
        
        # ======== Bill Area============
        bill_Frame=Frame(self.root,bd=2,relief=RIDGE)
        bill_Frame.place(x=350,y=140,width=400,height=450)
        
        title2=Label(bill_Frame,text=" Customer Billing Area",font=("Times New Roman" ,18,"bold"),bd=1,bg="#ff69b4",fg="#f8f8ff",relief=RIDGE).pack(side=TOP,fill=X)

        
        scrolly2=Scrollbar(bill_Frame,orient=VERTICAL)
        self.bill_area=Text(bill_Frame,bg="#ffddf4",yscrollcommand=scrolly2.set)
        scrolly2.config(command=self.bill_area.yview)
        self.bill_area.pack(fill=BOTH,expand=1)
        
        # ======Images=====================================
        self.im1=Image.open("D:\VS Studio Code\IMS\image/web.png")
        self.im1=self.im1.resize((420,450))
        self.im1=ImageTk.PhotoImage(self.im1)
        
        self.lbl_im1=Label(self.root,image=self.im1,bd=0)
        self.lbl_im1.place(x=770,y=140)
        
        self.show()
        # ======Images=====================================
        # self.im2=Image.open("D:\VS Studio Code\IMS\image/bill.jpg")
        # self.im2=self.im2.resize((420,450))
        # self.im2=ImageTk.PhotoImage(self.im2)
        
        # self.lbl_im2=Label(self.root,image=self.im2,bd=0)
        # self.lbl_im2.place(x=770,y=140)
        
    def show(self):
        del self.bill_list[:]
        self.Sales_List.delete(0,END)
        for i in os.listdir("D:\VS Studio Code\IMS\Bills"):
            if i.split('.')[-1]=='txt':
                self.Sales_List.insert(END,i)
                self.bill_list.append(i.split('.')[0])

    def get_data(self,ev):
        index_=self.Sales_List.curselection()
        file_name=self.Sales_List.get(index_)
        self.bill_area.delete('1.0',END)
        fp=open(f"D:\VS Studio Code\IMS\Bills/{file_name}",'r')
        for i in fp:
            self.bill_area.insert(END,i)
        fp.close()
    def search(self):
        if self.var_invoice.get()=="":
            messagebox.showerror("Error","Invoice No. Must Be Required !!",parent=self.root)
        else:
            if self.var_invoice.get() in self.bill_list:
                fp=open(f"D:\VS Studio Code\IMS\Bills/{self.var_invoice.get()}.txt",'r')
                self.bill_area.delete('1.0',END)
                for i in fp:
                    self.bill_area.insert(END, i)
                fp.close()
            else:
                messagebox.showerror("Warning !!","Invalid Invoice No.",parent=self.root)
    def clear(self):
        self.show()
        self.bill_area.delete('1.0',END)        
            
if  __name__=="__main__":
    root=Tk()
    obj=salesClass(root)
    root.mainloop()