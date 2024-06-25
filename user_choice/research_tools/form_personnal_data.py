import tkinter as tk
from tkinter import ttk
from user_choice.research_tools.osint import run_tools

def Form():
    global window, entries
    pseudo = entries["Pseudo"].get()
    email = entries["Adresse email"].get()

    run_tools(email, pseudo)

    # Ferme la fenêtre principale si tout s'est bien passé ou si aucune donnée n'a été fournie
    window.destroy()

# Fonction pour afficher le formulaire
def main_form_research():
    global window, entries

    # Création de la fenêtre principale
    window = tk.Tk()
    window.title("Formulaire")

    # Création des onglets (Notebook)
    notebook = ttk.Notebook(window)
    notebook.pack(fill='both', expand=True)

    # Création des cadres pour chaque onglet
    frames = {}
    for label_text in ["Pseudo", "Adresse email"]:
        frames[label_text] = ttk.Frame(notebook)
        notebook.add(frames[label_text], text=label_text)

    # Liste des champs du formulaire
    fields = [
        ("Pseudo", frames["Pseudo"]),
        ("Adresse email", frames["Adresse email"]),
    ]

    entries = {}

    # Création des champs du formulaire via une boucle
    for label_text, frame in fields:
        label = ttk.Label(frame, text=label_text + ":")
        label.grid(row=0, column=0, padx=10, pady=10)

        entry = ttk.Entry(frame)
        entry.grid(row=0, column=1, padx=10, pady=10)

        entries[label_text] = entry

    submit_button = ttk.Button(window, text="Soumettre", command=Form)
    submit_button.pack(pady=10)

    # Exécution de la boucle principale
    window.mainloop()


