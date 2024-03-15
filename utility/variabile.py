#VARIABILI
info_pg = {
    "nome": "Merrik",
    "classe": "Mago",
    "livello": 1,
    "hp_attuali": 10,
    "hp_massimi":10,
    "monete": 10
}

stat_pg = {
    "Forza": 0,
    "Inteligenza": 0,
    "Carisma": 0,
}

abilità_pg = {
    "colpo": "effettua un attacco fisico base (Arma + forza)"
}

lista_classi = {
    "Guerriero": "un abile combattente la sua stat principale è forza",
    "Mago": "uno studioso dell'arcano la sua stat principale è intelligenza",
    "Bardo": "un festaiolo abile nella persuasione e dell'inganno la stat principale è carisma"
}

inventario = {}

all_item = {
    "Spada arruginita" : {
        "Descrizione" : "una vecchia spada che fa ancora il suo dovere (+3 danni fisici)",
        "Bonus danni fisici" : 3
    },
    "Focus arcano" : {
        "Descrizione" : "un focus donato ad ogni apprendista (+3 danni magici)",
        "Bonus danni magici" : 3
    },
    "Cappello fascinoso" : {
        "Descrizione" : "proprio un bel cappello (+3 carisma)",
        "Bonus stat carisma" : 3
    }
}

conferma_pg = "N"
scelta = 0
bg = "#E1C699"
colore_titolo = "#8f0609"
