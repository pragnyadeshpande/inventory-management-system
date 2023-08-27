from tkinter import *
import tkinter as tk
from turtle import right
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
import mysql.connector

TABLE_NAME="PRODUCT"
ProdID="ProdID"
ProdName="name"
modelName="model"
price="cost"
ProdType="type"
dept="dept"

class Prod:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1070x500+190+140")
        self.root.title("GIT INVENENTORY MANAGEMENT SYSTEM-Product Repository")
        self.root.config(bg="white")
        self.root.focus_force()

        connection=mysql.connector.connect(host='localhost',
                        database='INVENTORY',
                        user='root',
                        password='prgsd1907!')
        cursor=connection.cursor()

        searchFrame=Label(self.root,text="PRODUCT DETAILS",font=("goudy old style",20, "bold"),bg="lightblue",)
        searchFrame.place(x=0,y=20,width=1100,height=70)

        prodId=tk.Label(self.root,text="Product ID").place(x=50,y=150)
        name=tk.Label(self.root,text="Product Name").place(x=50,y=200)
        model=tk.Label(self.root,text="Model").place(x=50,y=250)
        cost_lbl=tk.Label(self.root,text="Cost").place(x=50,y=300)
        type=tk.Label(self.root,text="Type").place(x=50,y=350)
        Dept=tk.Label(self.root,text="Department").place(x=50,y=400)

        global prodidtxt, nametxt, modeltxt, costtxt, typetxt,depttxt

        prodidtxt=tk.Entry(root)
        prodidtxt.place(x=150,y=150)
        nametxt=tk.Entry(root)
        nametxt.place(x=150,y=200)
        modeltxt=tk.Entry(root)
        modeltxt.place(x=150,y=250)
        costtxt=tk.Entry(root)
        costtxt.place(x=150,y=300)
        typetxt=tk.Entry(root)
        typetxt.place(x=150,y=350)
        depttxt=tk.Entry(root)
        depttxt.place(x=150,y=400)


        def Add():
            global list
            global TABLE_NAME, ProdID, ProdName, dept, price, ProdType,modelName

            PID = prodidtxt.get()
            prodidtxt.delete(0, tk.END)
            pName = nametxt.get()
            nametxt.delete(0, tk.END)
            Dept= depttxt.get()
            depttxt.delete(0,tk.END)
            price= costtxt.get()
            costtxt.delete(0,tk.END)
            typet = typetxt.get()
            typetxt.delete(0, tk.END)
            mname=modeltxt.get()
            modeltxt.delete(0, tk.END)
            
            
            cursor.execute("INSERT INTO " + TABLE_NAME + " VALUES ( " + PID+ ", '"
                            + pName + "', '" + mname + "', '" +
                            typet+ "', '"+price+ "', '"+Dept+ "'); ")
            connection.commit()
            messagebox.showinfo("Success", "Data Saved Successfully.")

        def Clear():
            global list
            global TABLE_NAME, ProdID, ProdName, dept, price, ProdType,modelName

            PID = prodidtxt.get()
            prodidtxt.delete(0, tk.END)
            pName = nametxt.get()
            nametxt.delete(0, tk.END)
            Dept= depttxt.get()
            depttxt.delete(0,tk.END)
            price= costtxt.get()
            costtxt.delete(0,tk.END)
            typet = typetxt.get()
            typetxt.delete(0, tk.END)
            mname=modeltxt.get()
            modeltxt.delete(0, tk.END)

        def Disp():
            self.prodTable=ttk.Treeview(prod_frame,columns=("PID","name","model","type","cost","deptName"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
            
            self.prodTable.heading("PID",text="Product ID")
            self.prodTable.heading("name",text="Name")
            self.prodTable.heading("model",text="Model")
            self.prodTable.heading("type",text="Quantity")
            self.prodTable.heading("cost",text="Cost")
            self.prodTable.heading("deptName",text="Department")


            self.prodTable["show"]="headings"
            
            
            cursor.execute("SELECT * FROM " + TABLE_NAME + " ;")
            i = 0

            for row in cursor:
                self.prodTable.insert('', i,text =str(i+1),
                                    values=(row[0], row[1],
                                    row[2], row[3],
                                    row[4], row[5]))
                i = i + 1

            self.prodTable.pack(fill=BOTH,expand=1)



        btn_add=Button(self.root,text="SAVE",command=lambda:Add(),bg="#2196f3").place(x=50,y=450,width=60,height=20)
        #btn_update=Button(self.root,text="UPDATE",bg="#2196f3").place(x=330,y=300,width=60,height=20)
        btn_delete=Button(self.root,text="DISPLAY",command=lambda:Disp(),bg="#2196f3").place(x=130,y=450,width=60,height=20)        
        btn_clear=Button(self.root,text="CLEAR", command= lambda:Clear(),bg="#2196f3").place(x=210,y=450,width=60,height=20)


        prod_frame=Frame(self.root,bd=3, relief=RIDGE)
        prod_frame.place(x=350,y=120,width=600,height=300)

        scrolly=Scrollbar(prod_frame,orient=VERTICAL)
        scrollx=Scrollbar(prod_frame,orient=HORIZONTAL)



if __name__=='__main__':
    root=tk.Tk()
    obj=Prod(root)
    root.mainloop()
