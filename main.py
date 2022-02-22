#*************************RESTAURANT MANAGEMENT SYSTEM********************************
from tkinter import *



root=Tk()
root.geometry('1000x500')
root.title('Food Bill Management')
root.resizable(FALSE,False)


def Reset():
    entry_Idli.delete(0,END)
    entry_Dosa.delete(0,END)
    entry_Vada.delete(0,END)
    entry_Vadapav.delete(0,END)
    entry_maggi.delete(0,END)
    entry_Tea.delete(0,END)
    entry_coffee.delete(0,END)

def Total():
    try:a1=int(Idli.get())
    except:a1=0

    try:a2=int(Dosa.get())
    except:a2=0

    try:a3=int(Vada.get())
    except:a3=0

    try:a4=int(Vada_pav.get())
    except:a4=0

    try:a5=int(Maggi.get())
    except:a5=0

    try:a6=int(Tea.get())
    except:a6=0

    try:a7=int(Coffee.get())
    except:a7=0

    #price define
    b1=a1*40
    b2=a2*50
    b3=a3*45
    b4=a4*15
    b5=a5*50
    b6=a6*10
    b7=a7*100
    
    lbl_total=Label(f2,font=("aria",20,"bold"),text="Total",width=16,bg="white",fg="black")
    lbl_total.place(x=0,y=50)

    entry_total=Entry(f2,font=("aria",20,'bold'),textvariable=Total_bill,bd=6,width=15,bg='lightgreen')
    entry_total.place(x=20,y=100)

    total_cost=b1+b2+b3+b4+b5+b6+b7
    bill="Rs",str('%.2f'%total_cost)
    Total_bill.set(bill)
Label(text="Food Bill Management",bg='maroon',fg="white",font=("calibri",33),width="300",height="2").pack()


#menu card

f=Frame(root,bg="maroon",highlightbackground="black",highlightthickness=1,width=300,height=370)
f.place(x=10,y=120)

Label(f,text="Menu",font=("Gabriola",40,"bold"),fg="white",bg="maroon").place(x=80,y=0)

Label(f,font=("Lucida calligraphy",15,"bold"),text="Idli.........Rs.40/plate",fg="white",bg="maroon").place(x=10,y=80)
Label(f,font=("Lucida calligraphy",15,"bold"),text="Dosa.........Rs.50/plate",fg="white",bg="maroon").place(x=10,y=110)
Label(f,font=("Lucida calligraphy",15,"bold"),text="Vada.........Rs.45/plate",fg="white",bg="maroon").place(x=10,y=140)
Label(f,font=("Lucida calligraphy",15,"bold"),text="Vada pav.....Rs.15/plate",fg="white",bg="maroon").place(x=10,y=170)
Label(f,font=("Lucida calligraphy",15,"bold"),text="Maggi........Rs.50/plate",fg="white",bg="maroon").place(x=10,y=200)
Label(f,font=("Lucida calligraphy",15,"bold"),text="Tea..........Rs.10/cup",fg="white",bg="maroon").place(x=10,y=230)
Label(f,font=("Lucida calligraphy",15,"bold"),text="Coffee.......Rs.100/cup",fg="white",bg="maroon").place(x=10,y=260)

#bill
f2=Frame(root,bg="maroon",highlightbackground="black",highlightthickness=1,width=300,height=370)
f2.place(x=690,y=118)
bill=Label(f2,text="Bill",font=("Gabriola",20,"bold"),fg="white",bg="maroon")
bill.place(x=120,y=10)

#entry work
f1=Frame(root,bd=5,height=370,width=300,relief=RAISED)
f1.pack()

Idli=StringVar()
Dosa=StringVar()
Vada=StringVar()
Vada_pav=StringVar()
Maggi=StringVar()
Tea=StringVar()
Coffee=StringVar()
Total_bill=StringVar()

#label
lbl_Idli=Label(f1,font=("aria",20,"bold"),text="Idli",width=12,fg="maroon")
lbl_Dosa=Label(f1,font=("aria",20,"bold"),text="Dosa",width=12,fg="maroon")
lbl_Vada=Label(f1,font=("aria",20,"bold"),text="Vada",width=12,fg="maroon")
lbl_Vadapav=Label(f1,font=("aria",20,"bold"),text="Vadapav",width=12,fg="maroon")
lbl_maggi=Label(f1,font=("aria",20,"bold"),text="Maggi",width=12,fg="maroon")
lbl_Tea=Label(f1,font=("aria",20,"bold"),text="Tea",width=12,fg="maroon")
lbl_coffee=Label(f1,font=("aria",20,"bold"),text="Coffee",width=12,fg="maroon")
lbl_Idli.grid(row=1,column=0)
lbl_Dosa.grid(row=2,column=0)
lbl_Vada.grid(row=3,column=0)
lbl_Vadapav.grid(row=4,column=0)
lbl_maggi.grid(row=5,column=0)
lbl_Tea.grid(row=6,column=0)
lbl_coffee.grid(row=7,column=0)



#entry
entry_Idli=Entry(f1,font=("aria",20,"bold"),textvariable=Idli,bd=6,width=8,bg="red4",fg="white")
entry_Dosa=Entry(f1,font=("aria",20,"bold"),textvariable=Dosa,bd=6,width=8,bg="red4",fg="white")
entry_Vada=Entry(f1,font=("aria",20,"bold"),textvariable=Vada,bd=6,width=8,bg="red4",fg="white")
entry_Vadapav=Entry(f1,font=("aria",20,"bold"),textvariable=Vada_pav,bd=6,width=8,bg="red4",fg="white")
entry_maggi=Entry(f1,font=("aria",20,"bold"),textvariable=Maggi,bd=6,width=8,bg="red4",fg="white")
entry_Tea=Entry(f1,font=("aria",20,"bold"),textvariable=Tea,bd=6,width=8,bg="red4",fg="white")
entry_coffee=Entry(f1,font=("aria",20,"bold"),textvariable=Coffee,bd=6,width=8,bg="red4",fg="white")
entry_Idli.grid(row=1,column=1)
entry_Dosa.grid(row=2,column=1)
entry_Vada.grid(row=3,column=1)
entry_Vadapav.grid(row=4,column=1)
entry_maggi.grid(row=5,column=1)
entry_Tea.grid(row=6,column=1)
entry_coffee.grid(row=7,column=1)

#buttons
btn_reset=Button(f1,bd=5,fg="white",bg="maroon",font=('ariel',16,'bold'),width=10,text="Reset",command=Reset)
btn_reset.grid(row=8,column=0)

btn_total=Button(f1,bd=5,fg='white',bg='maroon',font=('ariel',16,'bold'),width=10,text='Total',command=Total)
btn_total.grid(row=8,column=1)






root.mainloop()