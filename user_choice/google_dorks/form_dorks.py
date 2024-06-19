import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import simpledialog, scrolledtext

class SearchCriteriaManager(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack(fill=BOTH, expand=YES, padx=20, pady=20)
        
        # Style
        self.master.style.theme_use('darkly')  # Choix du thème 'darkly'

        self.criteria = {
            "Site": [],
            "Mot-clé dans l'URL": [],
            "Mot clé dans le titre": [],
            "Type de fichier": [],
            "Recherche générale": []
        }

        self.create_search_frame()
        self.create_results_frame()

    def create_search_frame(self):
        self.search_frame = ttk.Frame(self, padding=10, relief='solid', borderwidth=1, style='SearchFrame.TFrame')  # Style personnalisé pour le cadre de recherche
        self.search_frame.pack(fill=X, pady=10)

        search_label = ttk.Label(self.search_frame, text="Entrez les critères de recherche ci-dessous :", font=("Helvetica", 16, "bold"), style='SearchLabel.TLabel')  # Style personnalisé pour le label de recherche
        search_label.pack(fill=X, pady=5)

        self.criteria_widgets = []

        for criteria_name, options_list in self.criteria.items():
            self.create_criteria_frame(criteria_name, options_list)

    def create_criteria_frame(self, criteria_name, options_list):
        criteria_frame = ttk.Frame(self.search_frame, padding=(10, 10, 10, 5), relief="solid", borderwidth=1, style='CriteriaFrame.TFrame')  # Style personnalisé pour chaque cadre de critère
        criteria_frame.pack(fill=X, pady=5)

        criteria_label = ttk.Label(criteria_frame, text=criteria_name + " :", font=("Arial", 12, "bold"), style='CriteriaLabel.TLabel')  # Style personnalisé pour chaque label de critère
        criteria_label.pack(side=LEFT, pady=5)

        add_button = ttk.Button(criteria_frame, text="Ajouter", style='Primary.TButton', command=lambda name=criteria_name: self.add_option(name))  # Style personnalisé pour le bouton Ajouter
        add_button.pack(side=LEFT, padx=10, pady=5)

        options_frame = ttk.Frame(criteria_frame, style='OptionsFrame.TFrame')  # Style personnalisé pour le cadre des options
        options_frame.pack(fill=X)

        num_columns = 5
        for i, option in enumerate(options_list):
            var = ttk.BooleanVar(value=True)
            option_check = ttk.Checkbutton(options_frame, text=option, variable=var, style='OptionCheck.TCheckbutton')  # Style personnalisé pour les cases à cocher des options
            option_check.grid(row=i // num_columns, column=i % num_columns, padx=5, pady=2, sticky="w")

        self.criteria_widgets.append((criteria_name, criteria_frame))

    def create_results_frame(self):
        self.results_frame = ttk.Frame(self, padding=10, relief='solid', borderwidth=1)
        self.results_frame.pack(fill=BOTH, pady=10, expand=YES)

        ttk.Button(self.results_frame, text="Lancer la recherche", style='Success.TButton', command=self.display_fake_results).pack(pady=5)

        ttk.Label(self.results_frame, text="Résultats de la Requête :", font=("Helvetica", 16, "bold")).pack(pady=5)

        self.text_area = scrolledtext.ScrolledText(self.results_frame, wrap="word", width=80, height=15, font=("Helvetica", 12))
        self.text_area.pack(fill=BOTH, expand=YES, padx=10, pady=10)

    def add_option(self, criteria_name):
        option = simpledialog.askstring(f"Ajouter une option pour {criteria_name}", f"Entrez une nouvelle option pour {criteria_name} :")
        if option:
            self.criteria[criteria_name].append(option)
            self.refresh_search_frame()

    def refresh_search_frame(self):
        for widget in self.criteria_widgets:
            widget[1].destroy()

        self.criteria_widgets = []
        self.create_search_frame()

    def display_fake_results(self):
        self.text_area.delete("1.0", "end")
        self.text_area.insert("end", "Placeholder: Fake results will be displayed here.\n")
        self.text_area.insert("end", "Selected Criteria:\n")

        for criteria_name, options_list in self.criteria.items():
            selected_options = [option for option in options_list]
            self.text_area.insert("end", f"{criteria_name}: {selected_options}\n")

        self.text_area.insert("end", "\nActual display of results would go here.")

def form_main_dorks():
    app = ttk.Window("Dorks Forms", "darkly", resizable=(True, True))  # Utilisation du thème 'darkly'
    SearchCriteriaManager(app)
    app.mainloop()
