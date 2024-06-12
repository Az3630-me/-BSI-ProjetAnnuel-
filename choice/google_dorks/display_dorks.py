import tkinter as tk
from tkinter import scrolledtext
from tkinter import ttk
from ttkthemes import ThemedStyle

# Crée une fenêtre principale
root = tk.Tk()
root.title("Affichage des Résultats Simulés")
root.geometry("900x600")  # Taille de la fenêtre
root.configure(bg="#f0f0f0")  # Couleur de fond

# Applique un thème prédéfini pour un design professionnel
style = ThemedStyle(root)
style.set_theme("radiance")  # Choix du thème "radiance"

# Crée une police de texte personnalisée
custom_font = ("Arial", 12)

# Cadre pour un look plus stylé
frame = ttk.Frame(root, padding=(10, 10, 10, 0), style="My.TFrame")
frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

# Style pour le cadre
style.configure("My.TFrame", background="#ffffff", borderwidth=2, relief="groove", width=500, height=400)

# Ajoute une étiquette au cadre
label = ttk.Label(frame, text="Résultats de la Requête", font=("Helvetica", 16, "bold"), style="My.TLabel")
label.grid(row=0, column=0, pady=(10, 20))

# Style pour l'étiquette
style.configure("My.TLabel", foreground="#007acc")

# Crée une zone de texte avec défilement pour afficher les résultats
text_area = scrolledtext.ScrolledText(frame, wrap=tk.WORD, width=80, height=15, font=custom_font, bg="#f0f0f0", bd=0)
text_area.grid(row=1, column=0, padx=10, pady=(0, 10), sticky="nsew")

# Fonction pour afficher des résultats simulés avec animation
def display_fake_results():
    # Liste de résultats simulés
    results = [
        {"title": "Exemple de Résultat 1", "link": "https://example.com/1", "description": "Ceci est une description pour l'exemple de résultat 1."},
        {"title": "Exemple de Résultat 2", "link": "https://example.com/2", "description": "Ceci est une description pour l'exemple de résultat 2."},
        {"title": "Exemple de Résultat 3", "link": "https://example.com/3", "description": "Ceci est une description pour l'exemple de résultat 3."}
    ]
    
    # Efface le contenu actuel de la zone de texte
    text_area.config(state=tk.NORMAL)
    text_area.delete("1.0", tk.END)
    
    # Ajoute chaque résultat simulé dans la zone de texte avec animation
    for result in results:
        text_area.insert(tk.END, f"Titre: {result['title']}\n", "title")
        text_area.insert(tk.END, f"Lien: {result['link']}\n", "link")
        text_area.insert(tk.END, f"Description: {result['description']}\n\n", "description")
    
    text_area.config(state=tk.DISABLED)

# Configure les styles de texte
text_area.tag_configure("title", font=("Arial", 14, "bold"), foreground="#007acc")
text_area.tag_configure("link", font=("Arial", 12, "italic"), foreground="#009900")
text_area.tag_configure("description", font=("Arial", 12))

# Bouton pour actualiser les résultats
refresh_button = ttk.Button(frame, text="Actualiser", command=display_fake_results)
refresh_button.grid(row=2, column=0, pady=(0, 10))

# Appel de la fonction pour afficher les résultats avec animation au démarrage
display_fake_results()

# Lancement de l'application Tkinter
root.mainloop()
