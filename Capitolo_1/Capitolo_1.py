import tkinter as tk
from functools import partial
import utility.variabile as v

def capitolo_1(window):
    # Chiudi la finestra corrente
    window.destroy()

    # Crea una nuova finestra
    capitolo_1 = tk.Tk()
    capitolo_1.title("Band")
    capitolo_1.geometry("500x600")
    capitolo_1.configure(background="#E1C699")

    testo = tk.Label(capitolo_1, text="CAPITOLO I\nil risveglio dell'eroe", font=("Helvetica", 20), background=v.bg, foreground=v.colore_titolo, pady=10)
    testo.pack(side=tk.TOP)