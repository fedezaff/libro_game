import tkinter as tk
from functools import partial
import utility.variabile as v
import Capitolo_1.Capitolo_1 as Capitolo1


def salva_valore(pagina_nome_pg, entry):
    v.info_pg["nome"] = entry.get()  # Ottieni il valore inserito nell'Entry
    #print("Valore inserito:", v.info_pg["nome"])
    # Qui puoi fare qualsiasi cosa desideri con il valore, come salvarlo in una variabile globale o fare un'operazione con esso
    pagina_selezione_classe(pagina_nome_pg)


def pagina_selezione_classe(window):
    # Chiudi la finestra corrente
    window.destroy()

    # Crea una nuova finestra
    pagina_selezione_classe = tk.Tk()
    pagina_selezione_classe.title("Band")
    pagina_selezione_classe.geometry("500x600")
    pagina_selezione_classe.configure(background="#E1C699")

    testo = tk.Label(pagina_selezione_classe,  text="Ciao "+ v.info_pg["nome"] + ". Queste sono le classi possibili:" , font=("Helvetica", 16), background=v.bg)
    testo.pack(side=tk.TOP)

    for classi in v.lista_classi:
        button = tk.Button(text=classi + ": " + v.lista_classi[classi], command=partial(addStatClasse, classi, pagina_selezione_classe), background=v.bg, foreground=v.colore_titolo,)
        button.pack()



def addStatClasse (classe, window):
    if classe == "Guerriero":
        v.stat_pg["Forza"] += 4
        v.stat_pg["Inteligenza"] += 2
        v.stat_pg["Carisma"] += 1
        #print(v.stat_pg)
    elif classe == "Mago":
        v.stat_pg["Forza"] += 1
        v.stat_pg["Inteligenza"] += 4
        v.stat_pg["Carisma"] += 2
        #print(v.stat_pg)
    elif classe == "Bardo":
        v.stat_pg["Forza"] += 2
        v.stat_pg["Inteligenza"] += 1
        v.stat_pg["Carisma"] += 4
        #print(v.stat_pg)

    Capitolo1.capitolo_1(window)

def pagina_nome_pg(window):

    window.destroy()
    
    pagina_nome_pg = tk.Tk()
    pagina_nome_pg.geometry("500x600")
    pagina_nome_pg.title("Band")
    pagina_nome_pg.configure(background="#E1C699")

    titolo = tk.Label(pagina_nome_pg, text="Creazione personaggio", font=("Helvetica", 20), background=v.bg, foreground=v.colore_titolo, pady=10)
    titolo.pack(side=tk.TOP)

    testo = tk.Label(pagina_nome_pg,  text="Benvenuto avventuriero, Come posso chiamarti?", font=("Helvetica", 16), background=v.bg)
    testo.pack(side=tk.TOP)

    # Creazione dell'Entry per l'inserimento di testo
    entry = tk.Entry(background=v.bg)
    entry.pack(pady=20)

    # Creazione del pulsante di conferma
    button = tk.Button(text="CONFERMA", command=partial(salva_valore, pagina_nome_pg, entry), background=v.bg, foreground=v.colore_titolo,)
    button.pack()
