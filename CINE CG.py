import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from tkinter import PhotoImage

ventana = tk.Tk()
ventana.title('CINEPLUS')
ventana.geometry("500x500")
ventana.config(bd=10)

titulo = tk.Label(ventana, text="CINE CG",fg="#FFD400",font=("Arial",40,"bold"),pady =10,bg="#CA0000")
titulo.pack()

label_etq = tk.Label(ventana,text="Bienvenido",font=("Arial",20),width=34,padx=5,pady=20,fg="black")
label_etq.pack()

marco = tk.LabelFrame(ventana, text="Completa tu registro", font=("Arial",10,"bold"),fg="#272727")
marco.config(bd=10,fg="RED")
marco.pack()

label_N = tk.Label(marco,text='Nombre: ',font=("Arial",10,"bold"),fg="BLACK")
label_N.grid(row=0,column=0,padx=10,pady=0)
entry_N = tk.Entry(marco,width=25)
entry_N.grid(row=0,column=1,padx=10,pady=10)



ventana.mainloop()