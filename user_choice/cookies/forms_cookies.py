# -*- coding: utf-8 -*-
# 1) Importation des modules nécessaires

import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import user_choice.cookies.firefox_notrealtime as fr
import user_choice.cookies.chrome as ch 

def ouvrir_fichier(navigateur_selectionne):
    """Ouvre une fenêtre de dialogue pour sélectionner un fichier de cookies et traite le fichier."""
    fichier = filedialog.askopenfilename(
    title="Sélectionnez un fichier de cookies",
    filetypes=[("All Files", "*.*")]  # Autoriser tous les fichiers
    )
    if fichier:
        if navigateur_selectionne == "Firefox":
            # Lire les cookies du fichier sélectionné pour Firefox
            fr.get_mozilla_cookies(fichier)
           
        else:
                # Lire les cookies du fichier sélectionné pour Chrome
            ch.get_default_cookies(fichier) 
               
            

def formulaire_cookies():
    """Crée et affiche l'interface graphique."""
        
    def on_analyser_clicked():
        navigateur_selectionne = menu_deroulant.get()
        ouvrir_fichier(navigateur_selectionne)
        
    root = tk.Tk()
    root.title("Visualiser les liens entre les sites")
    root.geometry('300x200')

    # Création d'un label explicatif
    label_explicatif = tk.Label(root, text="Visualisez les liens entre les sites!")
    label_explicatif.pack(pady=10)

    # Création d'un menu déroulant pour choisir le navigateur
    liste_navigateurs = ["Chrome", "Firefox", "Edge"]  # Liste des navigateurs pris en charge
    menu_deroulant = ttk.Combobox(root, values=liste_navigateurs, state="readonly")
    menu_deroulant.current(0)  
    menu_deroulant.pack(pady=10)
    # Création d'un bouton pour ouvrir le fichier de cookies et lancer le traitement
    bouton_fichier = tk.Button(root, text="Sélectionner et analyser", command=on_analyser_clicked)
    bouton_fichier.pack(pady=5)

    root.mainloop()  # Démarrage de la boucle principale de l'interface
