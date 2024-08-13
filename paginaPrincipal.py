import tkinter as tk

from tkinter import messagebox, PhotoImage, Label
from reloj import *
from listaDeTareas import *


def version():
    messagebox.showinfo("Integrantes", message="Aldo Saravia, Celeste Vilar, Diego Torres, Fabrizio")

ventana = tk.Tk()
ventana.title('Pagina Interactiva')
ventana.geometry('650x500')
ventana.resizable(0,0)

imagen = PhotoImage(file="fondo.png")
background = Label(image=imagen)
background.place(x=0, y=0, relheight=1, relwidth=1)

barra_menu = tk.Menu(ventana)
ventana.config(menu=barra_menu)

menu_principal = tk.Menu(barra_menu, tearoff=0)
menu_about = tk.Menu(barra_menu, tearoff=0)
barra_menu.add_cascade(label ='Principal', menu=menu_principal)
barra_menu.add_command(label="Acerca de", command=version)
submenu = tk.Menu(menu_principal, tearoff=0)
menu_principal.add_cascade(label ='Mini Proyectos', menu=submenu)
submenu.add_command(label = 'Lista de Tareas', command=lambda: mostrarLista(ventana))
submenu.add_command(label = 'Reloj', command=lambda: mostrar_ventana_reloj(ventana))

ventana.mainloop()