from tkinter import*
tk=Tk()
tk.title("Кликер")
tk.geometry("1000x500")
n=0
def n_plus():
    global n 
    n+=1
    label["text"]=str(n)+"P"

def n_sbros():
    global n 
    n=0
    label["text"]=str(n)+"P"

btn=Button(text="Клик", background="#000", foreground="#fff", 
           padx="20",pady="8",command=n_plus)
btn.pack()
label=Label(tk,text=str(n)+"P")
label.pack()
btn2=Button(text="Сброс", background="#000", foreground="#fff", 
           padx="20",pady="8",command=n_sbros)
btn2.pack()
mainloop()