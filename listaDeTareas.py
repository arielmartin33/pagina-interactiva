import tkinter as tk
from tkinter import Toplevel


def mostrarLista(ventana):
#   ventana = tk.Tk()
    ventanaLista = Toplevel(ventana)
    ventanaLista.title('Lista de tareas')
    ventanaLista.geometry('250x300')
    
    ingreso_tarea = tk.Entry(ventanaLista)
    ingreso_tarea.pack(padx=10, pady=20)

    def agregar_tarea():
        tarea = ingreso_tarea.get()
        if tarea:
            lista_tareas.insert(tk.END, tarea)
            ingreso_tarea.delete(0, tk.END)

    boton_agregar = tk.Button(ventanaLista, text = 'Agregar tarea', command = agregar_tarea)
    boton_agregar.pack()

    marco = tk.Frame(ventanaLista)
    marco.pack(padx = 10, pady = 10)
    scrollbar = tk.Scrollbar (marco)
    scrollbar .pack(side = tk.RIGHT, fill =tk.Y)

    def eliminar_tarea():
        seleccion = lista_tareas.curselection()
        if seleccion:
            lista_tareas.delete(seleccion)

    boton_eliminar = tk.Button(ventanaLista, text = 'Eliminar tarea', command = eliminar_tarea)
    boton_eliminar.pack()
    lista_tareas = tk.Listbox(marco, yscrollcommand= scrollbar .set)
    lista_tareas.pack(side=tk.LEFT, fill=tk.BOTH)

    # ventana.mainloop()