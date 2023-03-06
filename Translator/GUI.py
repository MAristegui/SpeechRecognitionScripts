import tkinter as tk
from tkinter import ttk
import speech_recognition as sr
import translator as tr

listener = sr.Recognizer()

def start_recording():
    record_button.config(state=tk.DISABLED)
    origin = var_menu_origin.get()
    dest = var_menu_dest.get()
    with sr.Microphone() as micro:
            sonido = listener.listen(micro)
            origin_text, dest_text = tr.translateText(origin, dest, sonido)
    table.insert('','end',values=[origin,origin_text,dest,dest_text]) 
    record_button.config(state=tk.NORMAL) 

# Crear gui principal
gui = tk.Tk()
gui.title("Traductor de audio")
gui.config(bg="#F0F0F0")  

# Crear marco para menus desplegables
marco_menus = tk.Frame(gui, bg="#F0F0F0")  
marco_menus.pack(side="top", pady=10)

# Menus desplegables 
opciones = list(tr.getOptions())
opciones.sort()#["Opción 1", "Opción 2", "Opción 3"]
var_menu_origin = tk.StringVar()
var_menu_origin.set(opciones[1])
nombre_menu_1 = tk.Label(marco_menus, text="Idioma origen")
nombre_menu_1.pack(side="left", padx=10)
menu_1 = tk.OptionMenu(marco_menus, var_menu_origin, *opciones)
menu_1.pack(side="left", padx=10)

var_menu_dest = tk.StringVar()
var_menu_dest.set(opciones[0])
nombre_menu_2 = tk.Label(marco_menus, text="Idioma destino")
nombre_menu_2.pack(side="right", padx=10)
menu_2 = tk.OptionMenu(marco_menus, var_menu_dest, *opciones)
menu_2.pack(side="right", padx=10)

# Boton grabacion
record_button = tk.Button(gui, text="Iniciar grabación", command=start_recording)
record_button.pack(pady=10)

# Tabla
table = ttk.Treeview(columns=('Idioma origen','Texto_origin','Idioma destino','Texto_dest'),show='headings')
table.heading('Idioma origen', text='Idioma origen')
table.heading('Texto_origin', text='Texto')
table.heading('Idioma destino', text='Idioma destino')
table.heading('Texto_dest', text='Texto')
table.column(0, width=100,anchor='center')
table.column(1, width=500,anchor='center')
table.column(2, width=100,anchor='center')
table.column(3, width=500,anchor='center')
table.pack()

gui.mainloop()
