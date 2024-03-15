#FUNZIONI
def start(): 
    print("Benvenuto avventuriero")
    info_pg["nome"] = input("Come ti chiami?: ")
    print()
    print("Ciao "+ info_pg["nome"])
    print("Queste sono le classi possibili:")
    for classi in lista_classi:
        print(classi+": ",end="")
        print(lista_classi[classi])

    flag = 1
    while flag == 1:
        info_pg["classe"] = input("Quale scegli?: ")
        for classi in lista_classi:
            if info_pg["classe"] == classi:
                flag = 0

        if flag == 1:
            print("errore inserimento riprova")

    addStatClasse(info_pg["classe"])

def inizio():
    print("Ti svegli nella tua camera è un nuovo giorno e il sole splende")
    print("Cosa fai?")
    print("1 - prendo il mio equipaggiamento")
    print("2 - guardo fuori dalla finestra")
    print("3 - esco dalla stanza")
    print("4 - dormi")
    print("M - per aprire il menu")
    scelta = input("")
    match scelta:
        case "1":
            prendiEquipaggiamento(inizio)
        case "2":
            guardaDallaFinestra()
        case "3":
            esciDallaCamera()
        case "4":
            dormi(inizio)
        case "M":
            menu(inizio)

def prendiEquipaggiamento(funzione_precedente):
    if len(inventario) == 0:
        print("Recuperi gli oggetti importanti")
        if info_pg["classe"] == "Guerriero":
            inventario["Spada arruginita"] = all_item["Spada arruginita"]
        elif info_pg["classe"] == "Mago":
            inventario["Focus arcano"] = all_item["Focus arcano"]    
        elif info_pg["classe"] == "Bardo":
            inventario["Cappello fascinoso"] = all_item["Cappello fascinoso"]
    else:
        print("Hai gia preso gli oggetti non ti sembra di esagerare?")
    funzione_precedente()

def guardaDallaFinestra():
    print("È una bella giornata, perfetta per andare all'avventura magari c'è qualche missione nella bacheca in piazza")
    print("Cosa fai?")
    print("1 - prendo il mio equipaggiamento")
    print("2 - esco dalla stanza")
    print("3 - dormi")
    print("M - per aprire il menu")
    scelta = input("")
    match scelta:
        case "1":
            prendiEquipaggiamento(guardaDallaFinestra)
        case "2":
            esciDallaCamera()
        case "3":
            dormi(guardaDallaFinestra)
        case "M":
            menu(guardaDallaFinestra)

def esciDallaCamera():#TO DO
    print("Sei uscito dalla stanza")
    print("Cosa fai?")
    print("1 - Vado in cucina")
    print("2 - Vado alla libreria")
    print("3 - Esco di casa")
    scelta = input("")
    match scelta:
        case "1":
            cucina(esciDallaCamera)
        case "2":
            libreria()
        case "3":
            fuoriCasa()
        case "M":
            menu(esciDallaCamera)

def cucina(funzione_precedente):
    if "panino" in inventario:
        print("La cucina è vuota :(")
    else:
        print("Toh guarda un panino, meglio portarselo dietro non si sa mai")
        inventario["panino"] = "un panino di qualità"
    funzione_precedente()

def libreria():#TO DO
    print()

def fuoriCasa():#TO DO
    print()

def dormi(funzione_precedente):
    print("L'avventura non aspetta i dormiglioni ma almeno recuperi gli hp")
    info_pg["hp_attuali"] = info_pg["hp_massimi"]
    print()
    funzione_precedente()

def menu(funzione_precedente):
    print()
    print("MENU")
    print("Pg - Stampa le info del pg")
    print("Stat - Stampa le statistiche")
    print("Inv - Stampa l'inventario")
    print("Mappa - Stampa la mappa")
    print("X - chiudi il menu")
    scelta = input("")
    match scelta:
        case "Pg":
            stampInfoPg(funzione_precedente)
        case "Stat":
            stampStat(funzione_precedente)
        case "Inv":
            stampInventario(funzione_precedente)
        case "Mappa":
            mappe(funzione_precedente)
        case "X":
            funzione_precedente()

def mappe(funzione_precedente):
    print()
    print("1 - mappa del villaggio Veipor")
    print("X - chiudi il menu mappe")
    print()
    scelta = input("")
    match scelta:#.lower (per togliere case sansitive)
        case "1":
            mappaVeipor()
            mappe(funzione_precedente)
        case "X":
            menu(funzione_precedente)

def mappaVeipor():
    print()
    print("|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
    print("|                         {VILLAGGIO VEIPOR}                          |")
    print("|                                                                     |")
    print("|                                               [torre del mago]      |")
    print("|                                                                     |")
    print("|       [fabbro]                                                      |")
    print("|                                                                     |")
    print("|                                           [taverna]                 |")
    print("|                                                                     |")
    print("|                                                                     |")
    print("|                            [piazza]                                 |")
    print("|                                                                     |")
    print("|                                                                     |")
    print("|                                                                     |")
    print("|                                                  [strada per        |")
    print("|                                                          foresta]   |")
    print("|     [casa]                                                          |")
    print("|                                                                     |")
    print("|                                                                     |")
    print("|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
    print()

    

def stampInfoPg(funzione_precedente):
    print()
    for info in info_pg:
        print(info+": ",end="")
        print(info_pg[info])
    print()
    menu(funzione_precedente)

def stampStat(funzione_precedente):
    print()
    for stat in stat_pg:
        print(stat+": ",end="")
        print(stat_pg[stat])
    print()
    menu(funzione_precedente)

def stampInventario(funzione_precedente):
    print()
    for oggetto in inventario:
        print(oggetto+": ",end="")
        print(inventario[oggetto])
    print()
    menu(funzione_precedente)

def addStatClasse (classe):
    if classe == "Guerriero":
        stat_pg["Forza"] += 4
        stat_pg["Inteligenza"] += 2
        stat_pg["Carisma"] += 1
    elif classe == "Mago":
        stat_pg["Forza"] += 1
        stat_pg["Inteligenza"] += 4
        stat_pg["Carisma"] += 2
    elif classe == "Bardo":
        stat_pg["Forza"] += 2
        stat_pg["Inteligenza"] += 1
        stat_pg["Carisma"] += 4

def removeStatClasse (classe):
    if classe == "Guerriero":
        stat_pg["Forza"] -= 4
        stat_pg["Inteligenza"] -= 2
        stat_pg["Carisma"] -= 1
    elif classe == "Mago":
        stat_pg["Forza"] -= 1
        stat_pg["Inteligenza"] -= 4
        stat_pg["Carisma"] -= 2
    elif classe == "Bardo":
        stat_pg["Forza"] -= 2
        stat_pg["Inteligenza"] -= 1
        stat_pg["Carisma"] -= 4 

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

#CODICE
while conferma_pg != "Y":
    start()

    print()
    print("[INFO DEL PG]")
    for info in info_pg:
        print(info+": ",end="")
        print(info_pg[info])
    print()
    print("[STATISTICHE DEL PG]")
    for stat in stat_pg:
        print(stat+": ",end="")
        print(stat_pg[stat])
    print()

    conferma_pg = input("Questo è il tuo pg, è corretto? (Y/N): ")
    if conferma_pg == "N":
        removeStatClasse(info_pg["classe"])

inizio()

