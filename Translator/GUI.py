import tkinter as tk
from tkinter import ttk
import speech_recognition as sr
import translator as tr

listener = sr.Recognizer()
# Función que se ejecuta cuando se inicia la grabación
def start_recording():
    record_button.config(state=tk.DISABLED)
    origin = var_menu_1.get()
    dest = var_menu_2.get()
    with sr.Microphone() as micro:
            sonido = listener.listen(micro)
            origin_text, dest_text = tr.translateText(origin, dest, sonido)
    table.insert('','end',values=[origin_text,dest_text]) 
    record_button.config(state=tk.NORMAL) 

# Crear gui principal
gui = tk.Tk()
gui.title("Traductor de audio")
gui.config(bg="#F0F0F0")  

# Crear marco para menus desplegables
marco_menus = tk.Frame(gui, bg="#F0F0F0")  
marco_menus.pack(side="top", pady=10)

# Menus desplegables 
opciones = tr.getOptions()#["Opción 1", "Opción 2", "Opción 3"]
var_menu_1 = tk.StringVar()
var_menu_1.set(opciones[1])
nombre_menu_1 = tk.Label(marco_menus, text="Idioma origen")
nombre_menu_1.pack(side="left", padx=10)
menu_1 = tk.OptionMenu(marco_menus, var_menu_1, *opciones)
menu_1.pack(side="left", padx=10)

#opciones_2 = tr.getOptions()#["Opción A", "Opción B", "Opción C"]
var_menu_2 = tk.StringVar()
var_menu_2.set(opciones[0])
nombre_menu_2 = tk.Label(marco_menus, text="Idioma destino")
nombre_menu_2.pack(side="right", padx=10)
menu_2 = tk.OptionMenu(marco_menus, var_menu_2, *opciones)
menu_2.pack(side="right", padx=10)

# Boton para iniciar grabación
record_button = tk.Button(gui, text="Iniciar grabación", command=start_recording)
record_button.pack(pady=10)

# Tabla 
table = ttk.Treeview(columns=('Origen','Destino'),show='headings')
table.heading('Origen', text='Origen')
table.heading('Destino', text='Destino')
table.pack()

#nombre_columna_1 = tk.Label(table, text="Idioma origen", bg="#FFFFFF", padx=10, pady=5)
#nombre_columna_1.grid(row=0, column=0)
#nombre_columna_2 = tk.Label(tabla, text="Idioma destino", bg="#FFFFFF", padx=10, pady=5)
#nombre_columna_2.grid(row=0, column=1)



gui.mainloop()
