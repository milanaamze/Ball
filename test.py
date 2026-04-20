import tkinter as tk
def arrange():
    i=0
    s=int(a.get())
    s1=int(b.get())
    s2=c.get()
    s3=o.get()
    s4=m.get()
    s5=z.get()
    s6=q.get()
    s7=w.get()
    s8=e.get()
    s9=r.get()

    if s==2 and s1==4:
        i+=2
        l.config(text=f"Жинаған ұпайыңыз:{i}/6")
    elif s==2 or s1==4:
        i+=1
        l.config(text=f"Жинаған ұпайыңыз:{i}/6")
    else:
        i=0
        l.config(text=f"Жинаған ұпайыңыз:{i}/6")
    if s3 and s4 and s6 and s8:
        i+=4
        l.config(text=f"Жинаған ұпайыңыз:{i}/6")
    elif (s3 and s4 and s6) or (s4 and s6 and s8) or (s3 and s6 and s8) or (s3 and s4 and  s8):
        i+=3
        l.config(text=f"Жинаған ұпайыңыз:{i}/6")
    elif (s3 and s4) or (s6 and s8) or (s3 and s6) or (s4 and s8) or (s3 and s8) or (s4 and s6):
        i+=2
        l.config(text=f"Жинаған ұпайыңыз:{i}/6")
    elif s3 or s4 or s6 or s8:
        i+=1
        l.config(text=f"Жинаған ұпайыңыз:{i}/6")
    else:
        i+=0
        l.config(text=f"Жинаған ұпайыңыз:{i}/6")
root=tk.Tk()
root.geometry("800x800")
root.title("Test")
root.config(bg="Lightgreen")


l=tk.Label(root,text="Тест сұрақтары",anchor="center",font=("Bookman old style",18,"bold"))
l.grid(row=0,column=0)

a=tk.IntVar()
l1=tk.Label(root,text="1.МКТ-ның неше қағидасы бар?",bg="#FFFF99",font=("Bookman old style",16,"underline"))
l1.grid(row=1,column=0,sticky="w")
b=tk.Radiobutton(root,text="2",font=("Bookman old style",14),variable=a,value=1)
b.grid(row=2,column=0,sticky="w")
b1=tk.Radiobutton(root,text="3",font=("Bookman old style",14),variable=a,value=2)
b1.grid(row=3,column=0,sticky="w")
b2=tk.Radiobutton(root,text="4",font=("Bookman old style",14),variable=a,value=3)
b2.grid(row=4,column=0,sticky="w")

b=tk.IntVar()
l2=tk.Label(root,text="2.c^2=a^2+b^2?",bg="#FFFF99",font=("Bookman old style",16,"underline"))
l2.grid(row=5,column=0,sticky="w")
b3=tk.Radiobutton(root,text="Пифагор теоремасы",font=("Bookman old style",14),variable=b,value=4)
b3.grid(row=6,column=0,sticky="w")
b4=tk.Radiobutton(root,text="Герон формуласы",font=("Bookman old style",14),variable=b,value=5)
b4.grid(row=7,column=0,sticky="w")
b5=tk.Radiobutton(root,text="Дискриминант табу",font=("Bookman old style",14),variable=b,value=6)
b5.grid(row=8,column=0,sticky="w")

c=tk.IntVar()
o=tk.IntVar()
m=tk.IntVar()
z=tk.IntVar()
l3=tk.Label(root,text="3.Пайтондағы класста әдістердің қандай түрлері бар?",bg="#FFFF99",font=("Bookman old style",16,"underline"))
l3.grid(row=9,column=0,sticky="w")
b6=tk.Checkbutton(root,text="getattr, setattr, delattr, hasattr",font=("Bookman old style",14),variable=c)
b6.grid(row=10,column=0,sticky="w")
b7=tk.Checkbutton(root,text="__init__,__str__,__len__",font=("Bookman old style",14),variable=o)
b7.grid(row=11,column=0,sticky="w")
b8=tk.Checkbutton(root,text="Жәй, class, static",font=("Bookman old style",14),variable=m)
b8.grid(row=12,column=0,sticky="w")
b8=tk.Checkbutton(root,text="I don't know",font=("Bookman old style",14),variable=z)
b8.grid(row=13,column=0,sticky="w")
q=tk.IntVar()
w=tk.IntVar()
e=tk.IntVar()
r=tk.IntVar()
l4=tk.Label(root,text="4.Қазақстанда ең төменгі нүкте-Қарақия ойысы, ал ең жоғарғы нүкте-Хан Тәңірі шыңы. Олардың ұзындықтары қанша?",bg="#FFFF99",font=("Bookman old style",16,"underline"))
l4.grid(row=14,column=0,sticky="w")
b6=tk.Checkbutton(root,text="Теңіз деңгейінен 132м тереңдікте",font=("Bookman old style",14),variable=q)
b6.grid(row=15,column=0,sticky="w")
b7=tk.Checkbutton(root,text="Теңіз деңгейінен 323м тереңдікте",font=("Bookman old style",14),variable=w)
b7.grid(row=16,column=0,sticky="w")
b8=tk.Checkbutton(root,text="6995м",font=("Bookman old style",14),variable=e)
b8.grid(row=17,column=0,sticky="w")
b8=tk.Checkbutton(root,text="7695м",font=("Bookman old style",14),variable=r)
b8.grid(row=18,column=0,sticky="w")

bq=tk.Button(root,text="Нәтижені көру",bg="green",font=("Bookman old style",16,"bold"),command=arrange)
bq.grid(row=20,column=0,sticky="we")
l=tk.Label(root,text=" ",width=10,font=("Bookman old style",18,"bold"))
l.grid(row=21,column=0,sticky="we")

root.mainloop()