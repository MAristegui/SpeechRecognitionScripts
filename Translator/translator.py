import tkinter as tk

# Función que se ejecuta cuando se inicia la grabación
def start_recording():
    record_button.config(state=tk.DISABLED)
    print("Grabación iniciada")
    record_button.config(state=tk.NORMAL) 

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Traductor de audio")
ventana.config(bg="#F0F0F0")  

# Crear marco para menus desplegables
marco_menus = tk.Frame(ventana, bg="#F0F0F0")  
marco_menus.pack(side="top", pady=10)

# Menus desplegables 
opciones_1 = ["Opción 1", "Opción 2", "Opción 3"]
nombre_menu_1 = tk.Label(marco_menus, text="Idioma origen")
nombre_menu_1.pack(side="left", padx=10)
menu_1 = tk.OptionMenu(marco_menus, tk.StringVar(), *opciones_1)
menu_1.pack(side="left", padx=10)

opciones_2 = ["Opción A", "Opción B", "Opción C"]
nombre_menu_2 = tk.Label(marco_menus, text="Idioma destino")
nombre_menu_2.pack(side="right", padx=10)
menu_2 = tk.OptionMenu(marco_menus, tk.StringVar(), *opciones_2)
menu_2.pack(side="right", padx=10)

# Boton para iniciar grabación
record_button = tk.Button(ventana, text="Iniciar grabación", command=start_recording)
record_button.pack(pady=10)

# Tabla 
tabla = tk.Frame(ventana, bg="#FFFFFF")  # Fondo blanco
tabla.pack(padx=50, pady=20)

nombre_columna_1 = tk.Label(tabla, text="Idioma origen", bg="#FFFFFF", padx=10, pady=5)
nombre_columna_1.grid(row=0, column=0)
nombre_columna_2 = tk.Label(tabla, text="Idioma destino", bg="#FFFFFF", padx=10, pady=5)
nombre_columna_2.grid(row=0, column=1)



ventana.mainloop()
