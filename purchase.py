from tkinter import *
import tkinter as tk
from turtle import right
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
import mysql.connector

TABLE_NAME="PURCHASE"
ProdID="pid"
ProdName="pname"
category="category"
price="cost"
qty="Qty"
dept="dept"


class Purch:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1070x500+190+140")
        self.root.title("GIT INVENENTORY MANAGEMENT SYSTEM-Purchases")
        self.root.config(bg="white")
        self.root.focus_force()

        connection=mysql.connector.connect(host='localhost',
                        database='INVENTORY',
                        user='root',
                        password='prgsd1907!')
        cursor=connection.cursor()

        searchFrame=Label(self.root,text="PURCHASE DETAILS",font=("goudy old style",20, "bold"),bg="lightblue",)
        searchFrame.place(x=0,y=20,width=1100,height=70)

        prodId=tk.Label(self.root,text="Product ID").place(x=50,y=150)
        name=tk.Label(self.root,text="Product Name").place(x=50,y=200)
        category=tk.Label(self.root,text="Category").place(x=50,y=250)
        cost_lbl=tk.Label(self.root,text="Cost").place(x=50,y=300)
        Qtylbl=tk.Label(self.root,text="Quantity").place(x=50,y=350)
        Dept=tk.Label(self.root,text="Department Purchased By").place(x=50,y=400)

        global prodidtxt, nametxt, cattxt, costtxt, qtytxt,qty

        prodidtxt=tk.Entry(root)
        prodidtxt.place(x=250,y=150)
        nametxt=tk.Entry(root)
        nametxt.place(x=250,y=200)
        cattxt=tk.Entry(root)
        cattxt.place(x=250,y=250)
        costtxt=tk.Entry(root)
        costtxt.place(x=250,y=300)
        qtytxt=tk.Entry(root)
        qtytxt.place(x=250,y=350)
        depttxt=tk.Entry(root)
        depttxt.place(x=250,y=400)

        def Add():
            global list
            global TABLE_NAME, ProdID, ProdName, dept, price, category,modelName

            PID = prodidtxt.get()
            prodidtxt.delete(0, tk.END)
            pName = nametxt.get()
            nametxt.delete(0, tk.END)
            Dept= depttxt.get()
            depttxt.delete(0,tk.END)
            price= costtxt.get()
            costtxt.delete(0,tk.END)
            cat= cattxt.get()
            cattxt.delete(0, tk.END)
            qname=qtytxt.get()
            qtytxt.delete(0, tk.END)
            
            
            cursor.execute("INSERT INTO " + TABLE_NAME + " VALUES ( " + PID+ ", '"
                            + pName + "', '" + cat + "', '" +
                            Dept+ "', '"+qname+ "', '"+price+ "'); ")
            connection.commit()
            messagebox.showinfo("Success", "Data Saved Successfully.")

        def Clear():
            global list
            global TABLE_NAME, ProdID, ProdName, dept, price, category,modelName

            PID = prodidtxt.get()
            prodidtxt.delete(0, tk.END)
            pName = nametxt.get()
            nametxt.delete(0, tk.END)
            Dept= depttxt.get()
            depttxt.delete(0,tk.END)
            price= costtxt.get()
            costtxt.delete(0,tk.END)
            cat= cattxt.get()
            cattxt.delete(0, tk.END)
            qname=qtytxt.get()
            qtytxt.delete(0, tk.END)

        def Disp():
            self.purchTable=ttk.Treeview(purch_frame,columns=("pid","pname","category","dept","Qty","cost"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
            
            self.purchTable.heading("pid",text="Product ID")
            self.purchTable.heading("pname",text="Name")
            self.purchTable.heading("category",text="Category")
            self.purchTable.heading("dept",text="Purchased by")
            self.purchTable.heading("Qty",text="Quantity")
            self.purchTable.heading("cost",text="Amount")


            self.purchTable["show"]="headings"
            
            
            cursor.execute("SELECT * FROM " + TABLE_NAME + " ;")
            i = 0

            for row in cursor:
                self.purchTable.insert('', i,text =str(i+1),
                                    values=(row[0], row[1],
                                    row[2], row[3],
                                    row[4], row[5]))
                i = i + 1

            self.purchTable.pack(fill=BOTH,expand=1)

        

        btn_add=Button(self.root,text="SAVE",command=lambda:Add(),bg="#2196f3").place(x=50,y=450,width=60,height=20)
        #btn_update=Button(self.root,text="UPDATE",bg="#2196f3").place(x=330,y=300,width=60,height=20)
        btn_delete=Button(self.root,text="DISPLAY",command=lambda:Disp(),bg="#2196f3").place(x=130,y=450,width=60,height=20)        
        btn_clear=Button(self.root,text="CLEAR", command= lambda:Clear(),bg="#2196f3").place(x=210,y=450,width=60,height=20)

        purch_frame=Frame(self.root,bd=3, relief=RIDGE)
        purch_frame.place(x=450,y=120,width=600,height=300)

        scrolly=Scrollbar(purch_frame,orient=VERTICAL)
        scrollx=Scrollbar(purch_frame,orient=HORIZONTAL)




if __name__=='__main__':
    root=tk.Tk()
    obj=Purch(root)
    root.mainloop()