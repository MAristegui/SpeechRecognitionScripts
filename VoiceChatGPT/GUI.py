import tkinter as tk
from tkinter import ttk
import speech_recognition as sr
import translator as tr
import pyaudio
import pyttsx3

listener = sr.Recognizer()
engine = pyttsx3.init()
engine.setProperty('rate',150)

def start_recording():
    record_button.config(state=tk.DISABLED)
    with sr.Microphone() as micro:
            sonido = listener.listen(micro)
            text, resp = tr.translateText(sonido)
    table.insert('','end',values=[text,resp]) 
    engine.say(resp)
    engine.runAndWait()
    record_button.config(state=tk.NORMAL) 

# Crear gui principal
gui = tk.Tk()
gui.title("Traductor de audio")
gui.config(bg="#F0F0F0")  

# Crear marco para menus desplegables
marco_menus = tk.Frame(gui, bg="#F0F0F0")  
marco_menus.pack(side="top", pady=10)

# Boton grabacion
record_button = tk.Button(gui, text="Iniciar grabación", command=start_recording)
record_button.pack(pady=10)

# Tabla
table = ttk.Treeview(columns=('Peticion','Respuesta'),show='headings')
table.heading('Peticion', text='Peticion')
table.heading('Respuesta', text='Respuesta')
table.column(0, width=500,anchor='center')
table.column(1, width=500,anchor='center')
table.pack()

gui.mainloop()
