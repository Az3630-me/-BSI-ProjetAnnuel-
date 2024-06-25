import os
import webbrowser
import threading
import time

from user_choice.research_tools.display_result import display_result_pseudo_email

time_time = time.strftime('%Y%m%d_%H')

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
    thread_WP = threading.Thread(target=run_WEB_pseudo_websites, args=(pseudo,))
    thread_WP.start()

def run_tools(email: str, pseudo: str):
    report_dir = os.path.join("datatracker", "reports", f"report_{time_time}")

    if not os.path.isdir(report_dir):
        os.makedirs(report_dir)
        
    # Exécuter les fonctions liées à l'email et au pseudo dans des threads
    threading_email_function(email)
    threading_pseudo_function(pseudo)
    
    # Chemins vers les rapports
    report_blackbird_pseudo = os.path.join(report_dir, "blackbird_pseudo_report.txt")
    report_sherlock_pseudo = os.path.join(report_dir, "sherlock_pseudo_report.txt")
    report_blackbird_email = os.path.join(report_dir, "blackbird_email_report.txt")
    report_holehe_email = os.path.join(report_dir, "holehe_email_report.txt")
    display_result_pseudo_email(report_blackbird_pseudo, report_sherlock_pseudo, report_blackbird_email, report_holehe_email, pseudo, email)

# Test des fonctions
#run_tools("test.test@yopmail.com", "test.test")
