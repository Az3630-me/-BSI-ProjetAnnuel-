import tkinter as tk
from tkinter import scrolledtext, simpledialog, ttk

class SearchCriteriaManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Affichage des Résultats Simulés")
        self.root.geometry("900x800")
        self.root.configure(bg="#f0f0f0")

        self.style = ttk.Style()
        self.style.theme_use("clam")

        self.custom_font = ("Arial", 12)

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
        self.search_frame = ttk.Frame(self.root, padding=(10, 10, 10, 0))
        self.search_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        search_label = ttk.Label(self.search_frame, text="Entrez les critères de recherche ci-dessous :",
                                 font=("Helvetica", 14, "bold"))
        search_label.grid(row=0, column=0, pady=(0, 10), sticky="w")

        self.criteria_widgets = []

        for idx, (criteria_name, options_list) in enumerate(self.criteria.items(), start=1):
            criteria_frame = ttk.Frame(self.search_frame, padding=(10, 10, 10, 5), relief="raised", borderwidth=1)
            criteria_frame.grid(row=idx, column=0, pady=10, sticky="nsew")

            criteria_label = ttk.Label(criteria_frame, text=criteria_name + " :", font=("Arial", 12, "bold"))
            criteria_label.grid(row=0, column=0, sticky="w", pady=(10, 5))

            add_button = ttk.Button(criteria_frame, text="Ajouter", command=lambda name=criteria_name: self.add_option(name))
            add_button.grid(row=0, column=1, padx=(10, 0), pady=(10, 5))

            options_frame = ttk.Frame(criteria_frame)
            options_frame.grid(row=1, column=0, columnspan=2, sticky="w")

            num_columns = 5
            for i, option in enumerate(options_list):
                var = tk.BooleanVar(value=True)
                option_check = ttk.Checkbutton(options_frame, text=option, variable=var)
                option_check.grid(row=i // num_columns, column=i % num_columns, padx=5, pady=2, sticky="w")

            self.criteria_widgets.append((criteria_name, criteria_frame))

    def create_results_frame(self):
        self.results_frame = ttk.Frame(self.root, padding=(10, 10, 10, 0))
        self.results_frame.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

        ttk.Button(self.results_frame, text="Lancer la recherche", command=self.display_fake_results).grid(row=0,
                                                                                                           column=0,
                                                                                                           pady=(10, 20))

        ttk.Label(self.results_frame, text="Résultats de la Requête :", font=("Helvetica", 16, "bold")).grid(row=1,
                                                                                                             column=0,
                                                                                                             pady=(
                                                                                                             10, 20))

        self.text_area = scrolledtext.ScrolledText(self.results_frame, wrap=tk.WORD, width=80, height=15,
                                                   font=self.custom_font, bg="#f0f0f0", bd=0)
        self.text_area.grid(row=2, column=0, padx=10, pady=(0, 10), sticky="nsew")

    def add_option(self, criteria_name):
        option = simpledialog.askstring(f"Ajouter une option pour {criteria_name}",
                                        f"Entrez une nouvelle option pour {criteria_name} :")
        if option:
            self.criteria[criteria_name].append(option)
            self.refresh_search_frame()

    def refresh_search_frame(self):
        for widget in self.criteria_widgets:
            widget[1].destroy()

        self.criteria_widgets = []
        self.create_search_frame()

    def display_fake_results(self):
        self.text_area.delete("1.0", tk.END)
        self.text_area.insert(tk.END, "Placeholder: Fake results will be displayed here.\n")
        self.text_area.insert(tk.END, "Selected Criteria:\n")

        for criteria_name, options_list in self.criteria.items():
            selected_options = [option for option in options_list]  # Simply iterate through options_list
            self.text_area.insert(tk.END, f"{criteria_name}: {selected_options}\n")

        self.text_area.insert(tk.END, "\nActual display of results would go here.")


if __name__ == "__main__":
    root = tk.Tk()
    app = SearchCriteriaManager(root)
    root.mainloop()
