import time

# Heure actuelle et heure de réveil
heure_actuelle = (16, 29, 55)
heure_reveil = (16, 30, 00)
choix_stop = (16, 30, 5)
def afficher_heure(heure):
    h, m, s = heure
    while True:
        # Affichage de l'heure
        
        # Mise à jour de l'heure
        s += 1
        if s == 60:
            s = 0
            m += 1
            if m == 60:
                m = 0
                h += 1
                if h == 24:
                    h = 0
        
        # Attente d'une seconde
        time.sleep(1)
        
        # Mise à jour de l'heure actuelle
        heure_actuelle = (h, m, s)
        
        # Vérification de l'alarme
        alarme(heure_actuelle)
        
        # Affichage de l'heure au format 12 heures
        affichage(h, m, s,format_choisi)
        stop(h, m, s, choix_stop)
format_choisi = input("Choisissez le format (24h ou am/pm): ")
        
# Fonction pour vérifier si c'est l'heure du réveil
def alarme(heure):
    if heure == heure_reveil:
        print("\nC'est l'heure du réveil")

# Fonction pour afficher l'heure au format 12 heures avec AM/PM
def affichage(h, m, s,format_choisi):
    if format_choisi.lower()=="24h":
        print(f"{h:02d}:{m:02d}:{s:02d}")
    elif format_choisi.lower() == "am/pm":    
        suffixe = "AM"
        if h >= 12:
            suffixe = 'PM'
        if h > 12:
            h -= 12
        elif h == 0:
            h = 12
    
        print(f'{h:02d}:{m:02d}:{s:02d} {suffixe}')
    else:
        print("Format non reconnu. Veuillez choisir entre '24h' ou 'am/pm'.")
def stop(h, m, s, choix_stop):
    if choix_stop == (h, m, s):
        pause_reponse = input("L'horloge est mise en pause. Voulez vous continuer ? (oui/non): ")
        if pause_reponse.lower() == "oui":
            pass
        elif pause_reponse.lower() == "non":
            print("Horloge stop. Veuillez écrire 'reprendre' pour continuer.")
            while True:
                reprise = input("Attente de reprise : ")
                if reprise.lower() == "reprendre":
                    print("Horloge reprise.")
                    break
                else:
                    print("Commande non reconnue.")        

# Fonction pour afficher l'heure en continu avec une mise à jour chaque seconde

# Appel de la fonction pour afficher l'heure
afficher_heure(heure_actuelle)