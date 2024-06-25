import tkinter as tk
from tkinter import scrolledtext, simpledialog, ttk
from tkcalendar import DateEntry
from user_choice.google_dorks.research_dorks import research

class SearchCriteriaManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Affichage des Résultats Simulés")
        self.root.geometry("900x800")
        self.root.configure(bg="#d3d3d3")

        self.style = ttk.Style()
        self.style.theme_use("clam")

        self.custom_font = ("Arial", 12)

        self.criteria = {
            "Site": [],
            "Mot-clé dans l'URL": [],
            "Mot clé dans le titre": [],
            "Mot clé dans le texte": [],
            "Type de fichier": [],
            "Plage de dates": {"Avant": "", "Après": ""},
            "Cache": []
        }

        self.criteria_vars = {
            "Site": {},
            "Mot-clé dans l'URL": {},
            "Mot clé dans le titre": {},
            "Mot clé dans le texte": {},
            "Type de fichier": {},
            "Cache": {}
        }

        self.create_scrollable_frame()
        self.create_search_frame()
        self.create_results_frame()

    def create_scrollable_frame(self):
        self.canvas = tk.Canvas(self.root, bg="#d3d3d3")
        self.scrollbar = ttk.Scrollbar(self.root, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = ttk.Frame(self.canvas, style="TFrame")

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(
                scrollregion=self.canvas.bbox("all")
            )
        )

        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")

    def create_search_frame(self):
        self.search_frame = ttk.Frame(self.scrollable_frame, padding=(10, 10, 10, 0), style="TFrame")
        self.search_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        search_label = ttk.Label(self.search_frame, text="Entrez les critères de recherche ci-dessous :",
                                 font=("Helvetica", 14, "bold"), background="#d3d3d3")
        search_label.grid(row=0, column=0, pady=(0, 10), sticky="w")

        self.criteria_widgets = []

        for idx, (criteria_name, options_list) in enumerate(self.criteria.items(), start=1):
            criteria_frame = ttk.Frame(self.search_frame, padding=(10, 10, 10, 5), relief="raised", borderwidth=1, style="TFrame")
            criteria_frame.grid(row=idx, column=0, pady=10, sticky="nsew")

            criteria_label = ttk.Label(criteria_frame, text=criteria_name + " :", font=("Arial", 12, "bold"), background="#d3d3d3")
            criteria_label.grid(row=0, column=0, sticky="w", pady=(10, 5))

            add_button = ttk.Button(criteria_frame, text="Ajouter", command=lambda name=criteria_name: self.add_option(name))
            add_button.grid(row=0, column=1, padx=(10, 0), pady=(10, 5))

            options_frame = ttk.Frame(criteria_frame, style="TFrame")
            options_frame.grid(row=1, column=0, columnspan=2, sticky="w")

            if criteria_name == "Plage de dates":
                self.before_date_entry = DateEntry(options_frame, width=12, background='darkblue', foreground='white', borderwidth=2)
                self.before_date_entry.grid(row=0, column=0, padx=10, pady=5)
                self.after_date_entry = DateEntry(options_frame, width=12, background='darkblue', foreground='white', borderwidth=2)
                self.after_date_entry.grid(row=0, column=1, padx=10, pady=5)
            else:
                num_columns = 5
                for i, option in enumerate(options_list):
                    var = self.criteria_vars[criteria_name].setdefault(option, tk.BooleanVar(value=True))
                    option_check = ttk.Checkbutton(options_frame, text=option, variable=var, command=self.update_criteria, style="TCheckbutton")
                    option_check.grid(row=i // num_columns, column=i % num_columns, padx=5, pady=2, sticky="w")

            self.criteria_widgets.append((criteria_name, criteria_frame))

    def update_criteria(self):
        for criteria_name, options_list in self.criteria.items():
            if criteria_name in self.criteria_vars:
                self.criteria[criteria_name] = [option for option, var in self.criteria_vars[criteria_name].items() if var.get()]

    def create_results_frame(self):
        self.results_frame = ttk.Frame(self.scrollable_frame, padding=(10, 10, 10, 0), style="TFrame")
        self.results_frame.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

        ttk.Button(self.results_frame, text="Lancer la recherche", command=self.research_dorks).grid(row=0, column=0, pady=(10, 20))

        # ttk.Label(self.results_frame, text="Résultats de la Requête :", font=("Helvetica", 16, "bold"), background="#d3d3d3").grid(row=1, column=0, pady=(10, 20))

        # self.text_area = scrolledtext.ScrolledText(self.results_frame, wrap=tk.WORD, width=80, height=15, font=self.custom_font, bg="#d3d3d3", bd=0)
    #     self.text_area.grid(row=2, column=0, padx=10, pady=(0, 10), sticky="nsew")

    def add_option(self, criteria_name):
        if criteria_name == "Plage de dates":
            before_date = self.before_date_entry.get_date()
            after_date = self.after_date_entry.get_date()
            self.criteria[criteria_name]["Avant"] = before_date
            self.criteria[criteria_name]["Après"] = after_date
        else:
            option = simpledialog.askstring(f"Ajouter une option pour {criteria_name}",
                                            f"Entrez une nouvelle option pour {criteria_name} :")
            if option:
                self.criteria[criteria_name].append(option)
                self.criteria_vars[criteria_name][option] = tk.BooleanVar(value=True)
        self.refresh_search_frame()

    def refresh_search_frame(self):
        for widget in self.criteria_widgets:
            widget[1].destroy()

        self.criteria_widgets = []
        self.create_search_frame()
    
    def research_dorks(self):
        self.update_criteria()
        research(self.criteria)

        
    # def display_results(self):
    #     self.update_criteria()
    #     self.text_area.delete("1.0", tk.END)
    #     self.text_area.insert(tk.END, "Placeholder: Fake results will be displayed here.\n")
    #     self.text_area.insert(tk.END, "Selected Criteria:\n")
    #     result_research = research(self)
    #     for criteria_name, options_list in result_research
    #         if criteria_name == "Plage de dates":
    #             before_date = self.criteria[criteria_name]["Avant"]
    #             after_date = self.criteria[criteria_name]["Après"]
    #             if before_date or after_date:
    #                 self.text_area.insert(tk.END, f"{criteria_name} - Avant: {before_date}, Après: {after_date}\n")
    #         else:
    #             if options_list:
    #                 self.text_area.insert(tk.END, f"{criteria_name}: {options_list}\n")

    #     self.text_area.insert(tk.END, "\nActual display of results would go here.")

def form_main_dorks():
    root = tk.Tk()
    SearchCriteriaManager(root)
    root.mainloop()
