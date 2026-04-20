import tkinter as tk

def win(*event):
    a=entry.get()
    b=entry1.get()
    c=entry2.get()
    if ((a.isdigit() or (a[0]=='-' and a[1:].isdigit())) and
            (b.isdigit() or (b[0]=='-' and b[1:].isdigit())) and
            (c.isdigit() or (c[0]=='-' and c[1:].isdigit()))):
        a=int(a)
        b=int(b)
        c=int(c)
        if a+b>c and a+c>b and b+c>a:
            p=(a+b+c)/2
            s=(p*(p-a)*(p-b)*(p-c))**0.5
            ss=round(s,2)
            label3.config(text=ss)
        else:
            label3.config(text="Үшбұрыш бола алмайды!")
    elif a<"0" or b<"0" or c<"0":
        label3.config(text="Теріс сан енгізуге болмайды!")
    else:
        label3.config(text="Мәтін енгізуге болмайды!")

root=tk.Tk()
root.title("Triangle")
root.geometry("700x700")
root.config(bg="#FFFF99")

label=tk.Label(root,text="A",width=6,font=("Times New Roman",14))
label.grid(row=0,column=0)
label1=tk.Label(root,text="B",width=6,font=("Times New Roman",14))
label1.grid(row=1,column=0)
label2=tk.Label(root,text="C",width=6,font=("Times New Roman",14))
label2.grid(row=2,column=0)
label3=tk.Label(root,text=" ",bg="Orange",font=("Times New Roman",14))
label3.grid(row=5,column=0,columnspan=2,sticky="NSWE")

entry=tk.Entry(root,font=("Times New Roman",14),fg="Black")
entry.grid(row=0,column=1)
entry1=tk.Entry(root,font=("Times New Roman",14),fg="Black")
entry1.grid(row=1,column=1)
entry2=tk.Entry(root,font=("Times New Roman",14),fg="Black")
entry2.grid(row=2,column=1)

button=tk.Button(root,text="ANSWER",bg="Green",font=("Times New Roman",14),command=win)
button.grid(row=4,column=0,columnspan=2,sticky="NSWE")
root.bind("<Return>",win)

root.mainloop()
