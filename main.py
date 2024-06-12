import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from choice.forms_cookies import formulaire_cookies
from choice.forms_organisation import form_organisation

def show_prout():
    print("prout")

def main():
    root = tk.Tk()
    root.title("Datracker")

    # Configuration des couleurs des boutons
    bouton_bg_color = '#787878'  # Couleur de fond des boutons
    bouton_fg_color = '#787878'     # Couleur du texte des boutons

    # Configuration du style des boutons
    style = ttk.Style()
    style.configure('TButton', background=bouton_bg_color, foreground=bouton_fg_color, font=('Helvetica', 12), padding=10)

    # Création d'un cadre principal pour organiser les éléments de l'interface
    main_frame = ttk.Frame(root, padding=20)
    main_frame.grid(row=0, column=0, sticky="nsew")

    # Ajout d'un titre
    title_label = ttk.Label(main_frame, text="Bienvenue sur Datracker", font=('Helvetica', 18, 'bold'))
    title_label.grid(row=0, column=0, columnspan=2, pady=10)

    # Ajout des boutons dans une grille pour une meilleure disposition
    backend_button = ttk.Button(main_frame, text="Visualisez les connexions entre les différents sites web que vous visitez", command=formulaire_cookies)
    backend_button.grid(row=1, column=0, padx=10, pady=10, sticky="ew")

    form_button = ttk.Button(main_frame, text="Visualisez les informations que les organisations ont sur vous", command=form_organisation)
    form_button.grid(row=1, column=1, padx=10, pady=10, sticky="ew")

    # Ajout d'un effet de survol pour les boutons
    style.map('TButton',
              background=[('active', bouton_bg_color)],
              foreground=[('active', bouton_fg_color)])  # Couleur de survol des boutons

    # Redimensionnement automatique des colonnes et lignes
    main_frame.columnconfigure(0, weight=1)
    main_frame.columnconfigure(1, weight=1)
    main_frame.rowconfigure(0, weight=1)
    main_frame.rowconfigure(1, weight=1)

    # Centrage de la fenêtre sur l'écran
    window_width = root.winfo_reqwidth()
    window_height = root.winfo_reqheight()
    position_right = int(root.winfo_screenwidth() / 2 - window_width / 2)
    position_down = int(root.winfo_screenheight() / 2 - window_height / 2)
    root.geometry("+{}+{}".format(position_right, position_down))

    # Utilisation d'un logo personnalisé pour l'icône de la fenêtre
    root.iconbitmap('logo.ico')

    root.mainloop()

if __name__ == "__main__":
    main()
