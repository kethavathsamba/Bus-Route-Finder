import sqlite3
from tkinter import *
from tkinter import ttk,messagebox
from PIL import Image,ImageTk

def bus_route(number):
    if number=="":
        messagebox.showerror('ERROR','ENTER NUMBER NUMBER')
    
    else: 
        conn = sqlite3.connect('bus_routes.db')
        cursor = conn.cursor()  
        data=cursor.execute("select stops from buses where bus_number=?",(number,))
        res=""
        for i in data:
            res=i 
        if res=="":
            messagebox.showerror('ERROR','NO DATA FOUND')  
        else:
            newroot=Tk()
            newroot.geometry("600x500")
            newroot.config(bg="sky blue")
            TREE=ttk.Treeview(newroot,columns=("SI.NO","STOPS"),show="headings",height=400)
            TREE.heading("SI.NO",text="SI.NO")
            TREE.heading("STOPS",text="STOPS")
            TREE.column("STOPS", anchor="center")   
            TREE.column("SI.NO", anchor="center")   
            TREE.pack(fill=X)
            si=1
            cursor.execute("select stops from buses where bus_number=?",(number,))
            data=cursor.fetchall()
            for i in data:
                TREE.insert("","end",values=(si,i[0]))
                si=si+1
            conn.close()

   

def bus_number(s1,s2):
    if s1=="" or s2=="":
        messagebox.showerror("ERROE","ENTER BUS STOP NAMES")
    else:
        conn = sqlite3.connect('bus_routes.db')
        cursor = conn.cursor()
        cursor.execute("select bus_number from buses where stops=? and bus_number in (select bus_number from buses where stops=?) ",(s1,s2))
        data=cursor.fetchall()
        res=""
        for i in data:
            res=data
        if res=="":
            messagebox.showerror('ERROR','NO BUSES FOUND')
        else:
            newroot=Toplevel(root)
            newroot.geometry("200x150")
            cursor.execute("select bus_number from buses where stops=? and bus_number in (select bus_number from buses where stops=?) ",(s1,s2))
            data=cursor.fetchall()
            si=1
            Label(newroot,text="BUS NUMBERS",font=("bold",15)).pack()
            for i in data:
                Label(newroot,text=i,font=("bold",15)).pack()
            

root = Tk()
root.title("Bus Finder")
root.geometry("400x600")
imgf=Frame(root,bg="red",width=400,height=300).pack()
filename=Image.open('bus.png')
photo = ImageTk.PhotoImage(filename)
lab=Label(imgf,image=photo)
lab.place(x=0,y=0)
nume=Entry(root,width=15,font=(10),border=3)
filename=Image.open('search.png')
scan = ImageTk.PhotoImage(filename)
nume.place(x=140,y=260)
busf=Frame(root,bg="blue",width=400,height=300).pack()
nums=Button(root,image=scan,width=40,height=40,command=lambda:bus_route(nume.get()))
nums.place(x=180,y=310)


stop1=Entry(root,width=18,font=(8),border=2)
stop2=Entry(root,width=18,font=(8),border=2)
to=Label(root,text='TO')
stop1.place(x=100,y=400)
stop2.place(x=100,y=480)
to.place(x=180,y=440)
stops=Button(root,image=scan,width=40,height=40,command=lambda:bus_number(stop1.get(),stop2.get()))
stops.place(x=180,y=530)

root.mainloop()