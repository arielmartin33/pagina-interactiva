import tkinter as tk
from tkinter import Toplevel
import time


def mostrar_ventana_reloj(ventana):
    ventana_secundaria = Toplevel(ventana)
    ventana_secundaria.title('Reloj simple')
    ventana_secundaria.geometry('400x200')
    reloj = tk.Label(ventana_secundaria, font =('Arial', 60), bg = 'blue', fg = 'white')
                              
# ventana = tk.Tk()

    def hora():
        tiempo_actual = time.strftime('%H:%M:%S')
        reloj.config(text = tiempo_actual)
        ventana_secundaria.after(1000, hora)

    reloj.pack(anchor = 'center')
    hora()
# ventana.mainloop()