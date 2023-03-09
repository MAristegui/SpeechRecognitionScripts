import tkinter as tk
from tkinter import ttk
import pyaudio
import speech_recognition as sr
import pyttsx3
from googletrans import Translator
import sqlite3
import StringManipulation as sm

engine = pyttsx3.init()
engine.setProperty('rate',125)

listener = sr.Recognizer()
translator = Translator()

connection=sqlite3.connect('db_Emotions.db',check_same_thread=False)
cursor=connection.cursor()

class App:
    def __init__(self, master):
        self.master = master
        master.title("Recognize emotions in speech (English)")
        self.master.geometry("1500x500")

        # Start recording button
        self.record_button = tk.Button(master, text="Iniciar grabación", command=self.start_recording)
        self.record_button.pack()


        # Create table
        self.table = ttk.Treeview(master, columns=('Text','Positive', 'Negative', 'Anger', 'Anticipation', 'Disgust', 'Fear', 'Joy', 'Sadness', 'Surprise', 'Trust'),show='headings')
        self.table.heading('Text', text='Text')
        self.table.heading('Positive', text='Positive (%)')
        self.table.heading('Negative', text='Negative (%)')
        self.table.heading('Anger', text='Anger (%)')
        self.table.heading('Anticipation', text='Anticipation (%)')
        self.table.heading('Disgust', text='Disgust (%)')
        self.table.heading('Fear', text='Fear (%)')
        self.table.heading('Joy', text='Joy (%)')
        self.table.heading('Sadness', text='Sadness (%)')
        self.table.heading('Surprise', text='Surprise (%)')
        self.table.heading('Trust', text='Trust (%)')

        self.table.column(0, width=500,anchor='center')
        self.table.column(1, width=100,anchor='center')
        self.table.column(2, width=100,anchor='center')
        self.table.column(3, width=100,anchor='center')
        self.table.column(4, width=100,anchor='center')
        self.table.column(5, width=100,anchor='center')
        self.table.column(6, width=100,anchor='center')
        self.table.column(7, width=100,anchor='center')
        self.table.column(8, width=100,anchor='center')
        self.table.column(9, width=100,anchor='center')
        self.table.column(10, width=100,anchor='center')
        
        self.table.pack()

    def start_recording(self):
        
        self.record_button.config(state=tk.DISABLED)
        
        with sr.Microphone() as micro:
            sonido = listener.listen(micro)
            texto = listener.recognize_google(sonido, language="EN")
            translate_text = texto

        lista = list(sm.emotionPercentages(sm.getEmotions(cursor,translate_text)))
        lista.insert(0,translate_text)
        self.table.insert('','end',values=lista) 
        self.record_button.config(state=tk.NORMAL)   
    

root = tk.Tk()
app = App(root)
root.mainloop()