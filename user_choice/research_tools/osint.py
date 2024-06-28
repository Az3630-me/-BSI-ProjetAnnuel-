import os
import webbrowser
import threading
import time
import re

from user_choice.research_tools.display_result import display_result_pseudo_email

time_time = time.strftime('%Y%m%d_%H')
#def run_CLI_holehe(email:str):
#	with open(f"datracker/reports/report_{f"time_time"}/holehe_report.txt", "a", encoding="UTF-8") as H_report:
#		H_report.write(f"\n\n\n\n{time.strftime('%Y/%m/%d-%H:%M:%S')}")
#	os.system(f"holehe {email} > datatracker/reports/report_{f"time_time"}/holehe_report.txt")


def run_CLI_blackbird_email(email: str):
    # Chemin complet du fichier de rapport Blackbird
    chemin_fichier_rapport = f"{os.getcwd()}/datracker/reports/report_{time_time}/blackbird_email_report.txt"

    # Créer le dossier de rapport s'il n'existe pas déjà
    chemin_reports = os.path.dirname(chemin_fichier_rapport)
    os.makedirs(chemin_reports, exist_ok=True)

    # Commande Blackbird avec redirection vers le fichier de rapport
    commande_blackbird = f"cd {os.getcwd()}/user_choice/research_tools/tools/blackbird && python3 blackbird.py --email {email} > {chemin_fichier_rapport} 2>&1"

    # Exécution de la commande Blackbird sans afficher le résultat dans le terminal
    os.system(commande_blackbird)

    # Vérifier si le fichier a été créé
    if os.path.exists(chemin_fichier_rapport):
        print(f"Le fichier de rapport a été créé : {chemin_fichier_rapport}")
       
        # Supprimer les 17 premières lignes du fichier
        with open(chemin_fichier_rapport, 'r') as file:
            lines = file.readlines()
       
        with open(chemin_fichier_rapport, 'w') as file:
            file.writelines(lines[17:])
            
            
def run_CLI_blackbird_pseudo(pseudo: str):
    # Chemin complet du fichier de rapport Blackbird
    chemin_fichier_rapport = f"{os.getcwd()}/datracker/reports/report_{time_time}/blackbird_pseudo_report.txt"

    # Créer le dossier de rapport s'il n'existe pas déjà
    chemin_reports = os.path.dirname(chemin_fichier_rapport)
    os.makedirs(chemin_reports, exist_ok=True)

    # Commande Blackbird avec redirection vers le fichier de rapport
    commande_blackbird = f"cd {os.getcwd()}/user_choice/research_tools/tools/blackbird && python3 blackbird.py -u {pseudo} > {chemin_fichier_rapport} 2>&1"

    # Exécution de la commande Blackbird sans afficher le résultat dans le terminal
    os.system(commande_blackbird)

    # Vérifier si le fichier a été créé
    if os.path.exists(chemin_fichier_rapport):
        print(f"Le fichier de rapport a été créé : {chemin_fichier_rapport}")
       
        # Supprimer les 17 premières lignes du fichier
        with open(chemin_fichier_rapport, 'r') as file:
            lines = file.readlines()
       
        with open(chemin_fichier_rapport, 'w') as file:
            file.writelines(lines[17:])

       



    


def run_CLI_sherlock(pseudo:str):
    # Récupérer le répertoire parent du répertoire courant (main.py)
    active_directory = os.path.dirname(os.path.abspath(__file__))
    parent_directory = os.path.abspath(os.path.join(active_directory, os.pardir))
    parent_parent_directory = os.path.abspath(os.path.join(parent_directory, os.pardir)) # Aller deux niveaux vers le répertoire parent

    # Aller dans le dossier datracker
    os.chdir(parent_parent_directory)
    path_datracker = os.path.join(parent_parent_directory, "datracker")


    chemin_reports = os.path.join(path_datracker, "reports", f"report_{time_time}")

    # Créer le dossier de rapport s'il n'existe pas déjà
    if not os.path.exists(chemin_reports):
        os.makedirs(chemin_reports)

    # Chemin complet du fichier de rapport Sherlock
    chemin_fichier_rapport = os.path.join(chemin_reports, "sherlock_pseudo_report.txt")

    # Commande Sherlock avec redirection vers le fichier de rapport
    commande_sherlock = f"sherlock {pseudo} > \"{chemin_fichier_rapport}\""

    # Exécuter la commande Sherlock
    os.system(commande_sherlock)



	

	


# Fonction pour ouvrir des sites web pour une adresse email
def run_WEB_email_websites(email):
    webbrowser.open_new(f"https://www.hudsonrock.com/email-search?email={email}")
    webbrowser.open_new_tab(f"https://haveibeenpwned.com/")

# Fonction pour ouvrir des sites web pour un pseudo
def run_WEB_pseudo_websites(pseudo):
    webbrowser.open_new(f"http://www.skymem.info/srch?q={pseudo}&ss=srch")
    webbrowser.open_new_tab(f"https://whatsmyname.app/?q={pseudo}")

# Fonction pour exécuter les outils pour les emails dans des threads
def threading_email_function(email: str):
    thread_WE = threading.Thread(target=run_WEB_email_websites, args=(email,))
    thread_WE.start()

# Fonction pour exécuter les outils pour les pseudos dans des threads
def threading_pseudo_function(pseudo: str):
    #thread_WP = threading.Thread(target=run_WEB_pseudo_websites, args=(pseudo,))
    thread_WP = threading.Thread(target=run_CLI_sherlock, args=(pseudo,))
    thread_WP.start()

    thread_WP.start()

def run_tools(email: str, pseudo: str):
    report_dir = os.path.join("datracker", "reports", f"report_{time_time}")

    if not os.path.isdir(report_dir):
        os.makedirs(report_dir)
        
    # Exécuter les fonctions liées à l'email et au pseudo dans des threads
    #threading_email_function(email)
    #threading_pseudo_function(pseudo)
    run_CLI_sherlock(pseudo)
    run_CLI_blackbird_pseudo(pseudo)
    run_CLI_blackbird_email(email)
    # Chemins vers les rapports
    report_blackbird_pseudo = os.path.join(report_dir, "blackbird_pseudo_report.txt")
    report_sherlock_pseudo = os.path.join(report_dir, "sherlock_pseudo_report.txt")
    report_blackbird_email = os.path.join(report_dir, "blackbird_email_report.txt")
    #report_holehe_email = os.path.join(report_dir, "holehe_email_report.txt")
    display_result_pseudo_email(report_sherlock_pseudo, report_blackbird_pseudo, report_blackbird_email, pseudo, email)#, report_blackbird_pseudo, report_sherlock_pseudo, report_blackbird_email, report_holehe_email, pseudo, email)

# Test des fonctions
#run_tools("test.test@yopmail.com", "test.test")
