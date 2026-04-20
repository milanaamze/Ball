import tkinter as tk

def win():
    d=a.get()
    s=entry.get()
    s=int(s)
    if d==1:
        label3.config(text=f"{s:x}")
    elif d==2:
        label3.config(text=f"{s:o}")
    elif d==3:
        label3.config(text=f"{s:b}")


root=tk.Tk()
root.title("True")
root.geometry("700x700")
root.config(bg="lightblue")

a=tk.IntVar()
bb=tk.Radiobutton(root,text="Hexadecimal",bg="lightblue",font=("Times New Roman",14),variable=a,value=1,command=win)
b1=tk.Radiobutton(root,text="Octal",bg="lightblue",font=("Times New Roman",14),variable=a,value=2,command=win)
b2=tk.Radiobutton(root,text="Binary",bg="lightblue",font=("Times New Roman",14),variable=a,value=3,command=win)
bb.grid(row=2,column=0,sticky="w")
b1.grid(row=3,column=0,sticky="w")
b2.grid(row=4,column=0,sticky="w")
label3=tk.Label(root,text="Calculation counting system",bg="lightblue",font=("Times New Roman",14))
label3.grid(row=0,column=0)
entry=tk.Entry(root,font=("Times New Roman",14),fg="Black")
entry.grid(row=1,column=0)
label3=tk.Label(root,text=" ",bg="lightblue",font=("Times New Roman",14))
label3.grid(row=2,column=1)


root.mainloop()