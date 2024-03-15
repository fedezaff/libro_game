import tkinter as tk
from functools import partial
import utility.variabile as v
import utility.creazione_pg as creazione_pg


pagina_iniziale = tk.Tk()

pagina_iniziale.geometry("500x600")
pagina_iniziale.title("Band")
pagina_iniziale.configure(background="#E1C699")

titolo = tk.Label(pagina_iniziale, text="BAND\nil libro-game", font=("Helvetica", 20), background=v.bg, foreground=v.colore_titolo, pady=10)
titolo.pack(side=tk.TOP)

button = tk.Button(text="AVVIA", command=partial(creazione_pg.pagina_nome_pg, pagina_iniziale), background=v.bg, foreground=v.colore_titolo,)
button.pack()

if __name__ == "__main__":    
    pagina_iniziale.mainloop()
