import tkinter as tk
from tkinter import ttk
from user_choice.google_dorks.form_dorks import form_main_dorks
from user_choice.research_tools.form_personnal_data import main_form_research


def form_organisation():
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
    title_label = ttk.Label(main_frame, text="Visualisez les données que les organisations ont sur vous", font=('Helvetica', 18, 'bold'))
    title_label.grid(row=0, column=0, columnspan=2, pady=10)

    # Ajout des boutons dans une grille pour une meilleure disposition
    backend_button = ttk.Button(main_frame, text="Recherches google avancées ", command=form_main_dorks)
    backend_button.grid(row=1, column=0, padx=10, pady=10, sticky="ew")

    form_button = ttk.Button(main_frame, text="Recherche sur vos données", command=main_form_research)
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


    root.mainloop()
