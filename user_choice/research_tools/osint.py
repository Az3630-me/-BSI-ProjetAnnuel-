import os
import tkinter as tk
from tkinter import ttk
import time

time_time = time.strftime('%Y%m%d_%H')

def run_CLI_holehe(email:str):
    chemin_fichier_rapport = f"{os.getcwd()}/datracker/reports/report_{time_time}/holehe_email_report.txt"
    chemin_reports = os.path.dirname(chemin_fichier_rapport)
    os.makedirs(chemin_reports, exist_ok=True)
    commande_holehe = f"holehe {email} > {chemin_fichier_rapport} 2>&1"
    os.system(commande_holehe)

def run_CLI_blackbird_email(email: str):
    chemin_fichier_rapport = f"{os.getcwd()}/datracker/reports/report_{time_time}/blackbird_email_report.txt"
    chemin_reports = os.path.dirname(chemin_fichier_rapport)
    os.makedirs(chemin_reports, exist_ok=True)
    commande_blackbird = f"cd {os.getcwd()}/user_choice/research_tools/tools/blackbird && python3 blackbird.py --email {email} > {chemin_fichier_rapport} 2>&1"
    os.system(commande_blackbird)

def run_CLI_blackbird_pseudo(pseudo: str):
    chemin_fichier_rapport = f"{os.getcwd()}/datracker/reports/report_{time_time}/blackbird_pseudo_report.txt"
    chemin_reports = os.path.dirname(chemin_fichier_rapport)
    os.makedirs(chemin_reports, exist_ok=True)
    commande_blackbird = f"cd {os.getcwd()}/user_choice/research_tools/tools/blackbird && python3 blackbird.py -u {pseudo} > {chemin_fichier_rapport} 2>&1"
    os.system(commande_blackbird)

def run_CLI_sherlock(pseudo:str):
    active_directory = os.path.dirname(os.path.abspath(__file__))
    parent_directory = os.path.abspath(os.path.join(active_directory, os.pardir))
    parent_parent_directory = os.path.abspath(os.path.join(parent_directory, os.pardir))
    os.chdir(parent_parent_directory)
    path_datracker = os.path.join(parent_parent_directory, "datracker")
    chemin_reports = os.path.join(path_datracker, "reports", f"report_{time_time}")
    if not os.path.exists(chemin_reports):
        os.makedirs(chemin_reports)
    chemin_fichier_rapport = os.path.join(chemin_reports, "sherlock_pseudo_report.txt")
    commande_sherlock = f"sherlock {pseudo} > \"{chemin_fichier_rapport}\""
    os.system(commande_sherlock)

def run_tools(email: str, pseudo: str):
    report_dir = os.path.join("datracker", "reports", f"report_{time_time}")
    if not os.path.isdir(report_dir):
        os.makedirs(report_dir)

    # Création de la fenêtre principale tkinter
    root = tk.Tk()
    root.title("Progression des tâches")

    # Création d'un style ttk pour la barre de progression
    style = ttk.Style()
    style.theme_use('clam')  # Choisir un thème ttk

    # Personnalisation du style de la barre de progression
    style.configure("Custom.Horizontal.TProgressbar", troughcolor='#2E8B57', background='#3CB371', thickness=10)

    # Création de la barre de progression ttk
    progress_bar = ttk.Progressbar(root, style="Custom.Horizontal.TProgressbar", length=300, mode='determinate')
    progress_bar.pack(pady=20)

    # Déterminer le nombre total d'étapes en fonction des tâches à effectuer
    total_steps = 0
    if email:
        total_steps += 2  # Nombre de tâches pour l'email
    if pseudo:
        total_steps += 2  # Nombre de tâches pour le pseudo

    current_step = 0

    # Fonction pour avancer la barre de progression
    def advance_progress():
        nonlocal current_step
        current_step += 1
        progress_bar['value'] = (current_step / total_steps) * 100
        root.update_idletasks()  # Mettre à jour l'interface graphique
        time.sleep(1)  # Simuler une pause pour chaque étape

    # Exécuter les tâches
    if email:
        run_CLI_holehe(email)
        advance_progress()
        run_CLI_blackbird_email(email)
        advance_progress()

    if pseudo:
        run_CLI_blackbird_pseudo(pseudo)
        advance_progress()
        run_CLI_sherlock(pseudo)
        advance_progress()

    # Attendre la fin des tâches avant de fermer la fenêtre
    root.mainloop()
