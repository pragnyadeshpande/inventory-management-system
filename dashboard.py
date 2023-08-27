from tkinter import *
from PIL import Image, ImageTk
from department import Dept
from product import Prod
from purchase import Purch

class IMS:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.title("GIT INVENENTORY MANAGEMENT SYSTEM")
        self.root.config(bg="white")

        self.icontitle=PhotoImage(file="C:/Users/pragn/Desktop/images/logo.png")
        
        title=Label(self.root,text="GIT INVENTORY MANAGEMENT SYSTEM",image=self.icontitle,compound=LEFT,font=("verdana",25,"bold"),bg="blue",fg="white",anchor="w",padx=20).place(x=0,y=0,relwidth=1,height=70)

        logout=Button(self.root, text="Logout",font=("times new roman",15,"bold"),bg="light green",fg="white").place(x=1100,y=10,width=100,height=40)

        self.menuIcon=Image.open("C:/Users/pragn/Desktop/images/menuicon.png")
        self.menuIcon=self.menuIcon.resize((200,200),Image.ANTIALIAS)
        self.menuIcon=ImageTk.PhotoImage(self.menuIcon)
        

        leftMenu=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        leftMenu.place(x=0,y=102,width=200,height=565)

        lblMenuIcon=Label(leftMenu,image=self.menuIcon)
        lblMenuIcon.pack(side=TOP,fill=X)

        buttonMenu=Label(leftMenu, text="Menu",font=("times new roman",20),bg="#009688").pack(side=TOP,fill=X)
        btn1=Button(leftMenu,text="Staff",command=self.department,font=("times new roman",20,"bold"),bg="white",bd=3).pack(side=TOP,fill=X)
        btn2=Button(leftMenu,text="Product",command=self.product,font=("times new roman",20,"bold"),bg="white",bd=3).pack(side=TOP,fill=X)
        btn3=Button(leftMenu,text="Purchases",command=self.purchase,font=("times new roman",20,"bold"),bg="white",bd=3).pack(side=TOP,fill=X)
        #btn4=Button(leftMenu,text="Sales",font=("times new roman",20,"bold"),bg="white",bd=3).pack(side=TOP,fill=X)
        btn5=Button(leftMenu,text="Exit",command=self.close,font=("times new roman",20,"bold"),bg="white",bd=3).pack(side=TOP,fill=X)

        self.lblDept=Label(self.root,text="Total Department(s)\n[6]",bd=2,relief=RIDGE,bg="#33bbf9",fg="white",font=("verdana",15,"bold"))
        self.lblDept.place(x=300,y=120,height=150,width=300)

        self.lblProd=Label(self.root,text="Total Product(s)\n[0]",bd=2,relief=RIDGE,bg="#33bbf9",fg="white",font=("verdana",15,"bold"))
        self.lblProd.place(x=700,y=120,height=150,width=300)

        self.lblPurch=Label(self.root,text="Total Purchase(s)\n[0]",bd=2,relief=RIDGE,bg="#33bbf9",fg="white",font=("verdana",15,"bold"))
        self.lblPurch.place(x=500,y=350,height=150,width=300)

        #self.lblSale=Label(self.root,text="Total Sale(s)\n[0]",bd=2,relief=RIDGE,bg="#33bbf9",fg="white",font=("verdana",15,"bold"))
        #self.lblSale.place(x=700,y=350,height=150,width=300)

        

    def department(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=Dept(self.new_win)

    def product(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=Prod(self.new_win)

    def purchase(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=Purch(self.new_win)

    def close(self):
        self.root.destroy()
        


if __name__=='__main__':
    root=Tk()
    obj=IMS(root)
    root.mainloop()