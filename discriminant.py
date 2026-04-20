import tkinter as tk
import math as tm
def gold():
    a=entry.get()
    b=entry1.get()
    c=entry2.get()
    if ((a.isdigit() or (a[0]=='-' and a[1:].isdigit())) and
            (b.isdigit() or (b[0]=='-' and b[1:].isdigit())) and
            (c.isdigit() or (c[0]=='-' and c[1:].isdigit()))):
        a=int(a)
        b=int(b)
        c=int(c)
        d=b**2-(4*a*c)
        if a==0:
            x4=-c/b
            label3.config(text=f"x={x4}")
        elif b==0 and a==0:
            label3.config(text=f"Жауабы жоқ")
        if d>0:
            x1=int((-b)-tm.sqrt(d)/(2*a))
            x2=int((-b)+tm.sqrt(d)/(2*a))
            label3.config(text=f"x1={x1}{"\n"}x2={x2}",font=("Times New Roman",14,"bold"),fg="green")
        elif d==0:
            x=int((-b)/(2*a))
            label3.config(text=f"x={x}")
        else:
            label3.config(text="Түбірлері жоқ!",font=("Times New Roman",14,"italic"),fg="grey")
    else:
        label3.config(text="Тек сандарды қабылдайды!",font=("Times New Roman",14,"bold"),fg="red")
root = tk.Tk()
root.title("Квадратттық теңдеулер")
root.geometry("700x700")
root.config(bg="#FFFF66")

label = tk.Label(root, text="A", width=6, font=("Times New Roman", 14))
label.grid(row=0, column=0)
label1 = tk.Label(root, text="B", width=6, font=("Times New Roman", 14))
label1.grid(row=1, column=0)
label2 = tk.Label(root, text="C", width=6, font=("Times New Roman", 14))
label2.grid(row=2, column=0)
label3 = tk.Label(root, text=" ",bg="Orange", font=("Times New Roman", 14))
label3.grid(row=5, column=0, columnspan=2, sticky="NSWE")

entry = tk.Entry(root, font=("Times New Roman", 14), fg="Black")
entry.grid(row=0, column=1)
entry1 = tk.Entry(root, font=("Times New Roman", 14), fg="Black")
entry1.grid(row=1, column=1)
entry2 = tk.Entry(root, font=("Times New Roman", 14), fg="Black")
entry2.grid(row=2, column=1)

button = tk.Button(root, text="ANSWER", bg="Green", font=("Times New Roman", 14),command=gold)
button.grid(row=4, column=0, columnspan=2, sticky="NSWE")

root.mainloop()