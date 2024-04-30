
#But du Projet Annuel BSI : savoir si les données qu'on nous a fourni on été utilisé et par qui

# à implémenter dans ce code formulaire :
# - faire en sorte que mail doit contenir obliger un "@" & "."
# - essayer les graphique avec MatplotLib

# - Avancer rapport de projet


# Début du code
import tkinter as tk
from tkinter import ttk

def Form():
    global window, entries
    pseudo = entries["Pseudo"].get()
    email = entries["Adresse email"].get()
    phone = entries["Numéro de téléphone"].get()

    # Vérification du numéro de téléphone
    if not phone.isdigit() or len(phone) != 10:
        print(
            "Erreur : Attention le numéro de téléphone ne doit être composé que de chiffres et avec 10 caractères!!!")
        return

    print("Pseudo:", pseudo)
    print("Adresse email:", email)
    print("Numéro de téléphone:", phone)
    window.destroy()


# Fonction pour afficher le formulaire
def show_form():
    global window, entries
    intro_window.destroy()
    # Création de la fenêtre principale
    window = tk.Tk()
    window.title("Formulaire")

    # Création des onglets (Notebook)
    notebook = ttk.Notebook(window)
    notebook.pack(fill='both', expand=True)

    # Création des cadres pour chaque onglet
    frames = {}
    for label_text in ["Pseudo", "Adresse email", "Numéro de téléphone"]:
        frames[label_text] = ttk.Frame(notebook)
        notebook.add(frames[label_text], text=label_text)


    # Liste des champs du formulaire
    fields = [
        ("Pseudo", frames["Pseudo"]),
        ("Adresse email", frames["Adresse email"]),
        ("Numéro de téléphone", frames["Numéro de téléphone"])
    ]

    entries = {}

    # Création des champs du formulaire via une boucle
    for label_text, frame in fields:
        label = ttk.Label(frame, text=label_text + ":")
        label.grid(row=0, column=0, padx=10, pady=10)

        entry = ttk.Entry(frame)
        entry.grid(row=0, column=1, padx=10, pady=10)

        entries[label_text] = entry

        # Assignation dynamique des variables -> exemple si label_text = "Pseudo" alors une nouvl variable globale nommée
        # pseudo_entry est créée et assignée à entry, qui est un champ de saisie pour le pseudo -> (ttk.Entry)
        globals()[label_text.lower().replace(" ", "_") + "_entry"] = entry

    submit_button = ttk.Button(window, text="Soumettre", command=Form)
    submit_button.pack(pady=10)

    # Exécution de la boucle principale
    window.mainloop()

# Création de la fenêtre d'introduction
intro_window = tk.Tk()
intro_window.title("Introduction")

# Texte d'introduction
intro_label = ttk.Label(intro_window, text="Bienvenue ! Ceci est un formulaire. Veuillez remplir les informations suivantes :")
intro_label.pack(pady=10)

# Bouton pour afficher le formulaire
show_form_button = ttk.Button(intro_window, text="Commencer", command=show_form)
show_form_button.pack(pady=10)

# Exécution de la boucle principale
intro_window.mainloop()
