import tkinter as tk
from tkinter import messagebox
from reloj import *
from listaDeTareas import *


def version():
    messagebox.showinfo("Integrantes", message="Aldo Saravia, Celeste Vilar, Diego Torres, Fabrizio")

ventana = tk.Tk()
ventana.title('Menú desplegable')
ventana.geometry('400x200')

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