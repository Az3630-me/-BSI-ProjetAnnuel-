import re
import tkinter as tk
from tkinter import ttk
import webbrowser
import tldextract
from user_choice.research_tools.display_error_pseudo_email import *

# Fonction pour ouvrir des sites web pour une adresse email
def run_WEB_email_websites(email):
    webbrowser.open_new(f"https://www.hudsonrock.com/email-search?email={email}")
    webbrowser.open_new_tab(f"https://haveibeenpwned.com/")

# Fonction pour ouvrir des sites web pour un pseudo
def run_WEB_pseudo_websites(pseudo):
    webbrowser.open_new(f"http://www.skymem.info/srch?q={pseudo}&ss=srch")
    webbrowser.open_new_tab(f"https://whatsmyname.app/?q={pseudo}")

def extract_domain(url):
    """Extract the domain name from a URL."""
    ext = tldextract.extract(url)
    return f"{ext.domain}.{ext.suffix}"

def extract_sites_web(line):
    """Extract the pseudo from a line of text."""
    match = re.search(r'\] (.+)$', line)
    return match.group(1) if match else None

def check_symbol(line):
    """Check if the line contains [+] or [x]."""
    return '[+]' in line

def get_pseudos(file_path_1, file_path_2):
    """Read files and extract the pseudos."""
    pseudos = []
    with open(file_path_1, 'r', encoding='utf-8') as file:
        for line in file:
            pseudo = extract_sites_web(line.strip())
            if pseudo:
                pseudos.append(extract_domain(pseudo))
    pseudos.append("#####################################")
    pseudos.append("Site web trouvé par le deuxième outil")
    pseudos.append("#####################################")
    if file_path_2:
        with open(file_path_2, 'r', encoding='utf-8') as file:
            for line in file:
                pseudos.append(line.strip())
              
    return pseudos

def get_sites_webs_from_pseudo(listbox, file_path_1, file_path_2):
    """Read files and extract the pseudos."""
    if file_path_1 and file_path_2:  # Check if both file paths are not empty
        pseudos = get_pseudos(file_path_1, file_path_2)
       
        # Clear listbox
        listbox.delete(0, tk.END)
       
        # Check if there are pseudos to display
        if pseudos:
            for pseudo in pseudos:
               listbox.insert(tk.END, pseudo)
        else:
            # Optionally, you can insert a message indicating no pseudos found
            listbox.insert(tk.END, "Aucun pseudo trouvé")
    else:
        listbox.insert(tk.END, "Fichiers non spécifiés")

def remove_last_characters(chaine):
    return chaine[:-4]

def get_sites_webs_from_emails(listbox, file_path_3, file_path_4):
    """Read files and extract the sites web associated with emails."""
    if file_path_3:  # Check if both file paths are not empty
        web_sites = []

        # Read and process file_path_3 (assuming it contains email related sites)
        with open(file_path_3, 'r', encoding='utf-8') as file:
            for line in file:
                url = extract_sites_web(line.strip())
                web_sites.append(url)
       
        # Add separator and additional information
        web_sites.append("#####################################")
        web_sites.append("Site web trouvé par le deuxième outil")
        web_sites.append("#####################################")

        # Read and process file_path_4 (assuming it contains general web sites)
        with open(file_path_4, 'r', encoding='utf-8') as file:
            lines = file.readlines()[:-5]  # Read all lines except the last one
            for line in lines:
                if check_symbol(line):
                    url = remove_last_characters(line.strip())  # Remove trailing characters and strip whitespace
                    urls = extract_sites_web(url)
                    if url not in urls:
                       web_sites.append(urls)
       
        # Clear listbox
        listbox.delete(0, tk.END)
       
        # Check if there are web sites to display
        if web_sites:
            for site in web_sites:
                if site:  # Ensure not to insert None or empty strings
                    listbox.insert(tk.END, site)
        else:
            # Optionally, you can insert a message indicating no web sites found
            listbox.insert(tk.END, "Aucun site web trouvé")



def display_result_pseudo_email(report_path_1, report_path_2, report_path_3, report_path_4, pseudo, email):
    """Create and display the main window."""
    # Create the main window
    window = tk.Tk()
    window.title("Extraction de pseudos et d'emails")

    # Create the notebook (tabs)
    notebook = ttk.Notebook(window)
    notebook.pack(fill='both', expand=True)

    # Create the frame for Pseudos results
    frame_pseudo = ttk.Frame(notebook)
    notebook.add(frame_pseudo, text="Pseudos")

    # Label for displaying the custom text
    label_text = f"Pseudos trouvés correspondant à : {pseudo}"
    label = ttk.Label(frame_pseudo, text=label_text, wraplength=400, justify="left")
    label.pack(padx=10, pady=10)

    # Listbox for displaying the pseudos
    listbox_pseudo = tk.Listbox(frame_pseudo, width=50, height=20)
    listbox_pseudo.pack(padx=10, pady=10)

    # Create the frame for Email results
    frame_email = ttk.Frame(notebook)
    notebook.add(frame_email, text="Emails")

    # Label for displaying the custom text
    label_email_text = f"Sites web trouvés ayant un compte {email} :"
    label_email = ttk.Label(frame_email, text=label_email_text, wraplength=400, justify="left")
    label_email.pack(padx=10, pady=10)

    # Listbox for displaying the emails
    listbox_email = tk.Listbox(frame_email, width=50, height=20)
    listbox_email.pack(padx=10, pady=10)

    # Button to load the pseudos or display message if no pseudo
    if pseudo:
        load_button_pseudo = ttk.Button(frame_pseudo, text="Charger les pseudos",
                                        command=lambda: get_sites_webs_from_pseudo(listbox_pseudo, report_path_1, report_path_2))
        load_button_pseudo.pack(pady=10)
        # Add button to generate web searches for pseudos
        generate_button_pseudo = ttk.Button(frame_pseudo, text="Générer les recherches web",
                                            command=lambda: run_WEB_pseudo_websites(pseudo))
        generate_button_pseudo.pack(pady=10)
    else:
        load_button_pseudo = ttk.Button(frame_pseudo, text="Pas de pseudo",
                                        command=lambda: none_pseudo_or_error(listbox_pseudo))
        load_button_pseudo.pack(pady=10)

    # Button to load the emails or display message if no email
    if email:
        load_button_email = ttk.Button(frame_email, text="Charger les sites web trouvés",
                                       command=lambda: get_sites_webs_from_emails(listbox_email, report_path_3, report_path_4))
        load_button_email.pack(pady=10)
       
        # Add button to generate web searches for emails
        generate_button_email = ttk.Button(frame_email, text="Générer les recherches web",
                                           command=lambda: run_WEB_email_websites(email))
        generate_button_email.pack(pady=10)
    else:
        load_button_email = ttk.Button(frame_email, text="Pas d'email",
                                       command=lambda: none_email_or_error(listbox_email, "Il n'y avait pas d'e-mail en entrée"))
        load_button_email.pack(pady=10)

    # Start the Tkinter event loop
    window.mainloop()
