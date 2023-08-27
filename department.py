from tkinter import *
import tkinter as tk
from turtle import right
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
import mysql.connector

TABLE_NAME="EMPLOYEE"
ID="eid"
Name="name"
deptN="deptName"
pos="post"
Type="utype"




class Dept:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1070x500+200+140")
        self.root.title("GIT INVENENTORY MANAGEMENT SYSTEM-Employee Information")
        self.root.config(bg="white")
        self.root.focus_force()

        connection=mysql.connector.connect(host='localhost',
                        database='INVENTORY',
                        user='root',
                        password='prgsd1907!')
        cursor=connection.cursor()
        
        self.var_searchby=StringVar()
        self.var_searchtxt=StringVar()

        #self.var_empID=StringVar()
        #self.var_Name=StringVar()
        #self.var_deptName=StringVar()
        #self.var_Post=StringVar()
        #self.var_utype=StringVar()


        searchFrame=LabelFrame(self.root,text="Search",font=("goudy old style",12, "bold"),bg="white")
        searchFrame.place(x=250,y=20,width=600,height=70)


        cmb_search=ttk.Combobox(searchFrame,textvariable=self.var_searchby,values=("Select","Name",),state='readonly',justify=CENTER)
        cmb_search.place(x=10,y=10,width=180)
        cmb_search.current(0)

        txt_search=Entry(searchFrame,textvariable=self.var_searchtxt,bg="lightyellow").place(x=200,y=10)

        btn_search=Button(searchFrame,text="Search",bg="#4caf50").place(x=330,y=9,width=150,height=20)

        title=Label(self.root,text="Department Details").place(x=50,y=100,width=1000)
        
        EmpId=tk.Label(self.root,text="Employee ID").place(x=50,y=150)
        name=tk.Label(self.root,text="Employee Name").place(x=50,y=200)
        deptName=tk.Label(self.root,text="Department").place(x=50,y=250)
        Post=tk.Label(self.root,text="Designation").place(x=450,y=150)
        utype=tk.Label(self.root,text="User Type").place(x=450,y=200)

        global EmpIdtxt, nametxt, depttxt, posttxt, utypetxt

        EmpIdtxt=tk.Entry(root)
        EmpIdtxt.place(x=150,y=150)
        nametxt=tk.Entry(root)
        nametxt.place(x=150,y=200)
        depttxt=tk.Entry(root)
        depttxt.place(x=150,y=250)
        posttxt=tk.Entry(root)
        posttxt.place(x=600,y=150)
        utypetxt=tk.Entry(root)
        utypetxt.place(x=600,y=200)

        

        
        def Add():
            
            
            global list
            global TABLE_NAME, ID, Name, deptN, pos, Type

            eID = EmpIdtxt.get()
            EmpIdtxt.delete(0, tk.END)
            EName = nametxt.get()
            nametxt.delete(0, tk.END)
            Dept= depttxt.get()
            depttxt.delete(0,tk.END)
            post= posttxt.get()
            posttxt.delete(0,tk.END)
            utypet = utypetxt.get()
            utypetxt.delete(0, tk.END)
            
            
            cursor.execute("INSERT INTO " + TABLE_NAME + " VALUES ( " + eID+ ", '"
                            + EName + "', '" + Dept + "', '" +
                            post+ "', '"+utypet+ "'); ")
            connection.commit()
            messagebox.showinfo("Success", "Data Saved Successfully.")

        def Clear():
            global list
            global TABLE_NAME, ID, Name, deptN, pos, Type

            eID = EmpIdtxt.get()
            EmpIdtxt.delete(0, tk.END)
            EName = nametxt.get()
            nametxt.delete(0, tk.END)
            Dept= depttxt.get()
            depttxt.delete(0,tk.END)
            post= posttxt.get()
            posttxt.delete(0,tk.END)
            utypet = utypetxt.get()
            utypetxt.delete(0, tk.END)

        def Disp():
            self.deptTable=ttk.Treeview(dept_frame,columns=("eid","name","dept","post","utype"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
            
            self.deptTable.heading("eid",text="Employee ID")
            self.deptTable.heading("name",text="Name")
            self.deptTable.heading("dept",text="Department")
            self.deptTable.heading("post",text="Designation")
            self.deptTable.heading("utype",text="User Type")

            self.deptTable["show"]="headings"
            
            
            cursor.execute("SELECT * FROM " + TABLE_NAME + " ;")
            i = 0

            for row in cursor:
                self.deptTable.insert('', i,text =str(i+1),
                                    values=(row[0], row[1],
                                    row[2], row[3],
                                    row[4]))
                i = i + 1

            self.deptTable.pack(fill=BOTH,expand=1)

            

        btn_add=Button(root,text="SAVE",command=lambda:Add(),bg="#2196f3").place(x=250,y=300,width=60,height=20)
        #btn_update=Button(self.root,text="UPDATE",bg="#2196f3").place(x=330,y=300,width=60,height=20)
        btn_delete=Button(self.root,text="DISPLAY",command=lambda:Disp(),bg="#2196f3").place(x=370,y=300,width=60,height=20)        
        btn_clear=Button(self.root,text="CLEAR", command= lambda:Clear(),bg="#2196f3").place(x=490,y=300,width=60,height=20)

        dept_frame=Frame(self.root,bd=3, relief=RIDGE)
        dept_frame.place(x=0,y=350,relwidth=1,height=150)

        scrolly=Scrollbar(dept_frame,orient=VERTICAL)
        scrollx=Scrollbar(dept_frame,orient=HORIZONTAL)

            



if __name__=='__main__':
    root=tk.Tk()
    obj=Dept(root)
    root.mainloop()
    