import os
import sqlite3
import matplotlib.pyplot as plt
import networkx as nx

def get_chrome_cookies(cookies_path):
    """
    Récupère les cookies non essentiels d'un fichier de cookies Chrome et ne garde que ceux qui apparaissent sur plusieurs sites.
    Args:
        cookies_path (str): Le chemin d'accès au fichier de cookies Chrome.
    Returns:
        list: Une liste de tuples contenant (site web, nom du cookie).
    """
    if not os.path.exists(cookies_path):
        print("Le chemin spécifié vers le fichier de cookies n'existe pas.")
        return []

    try:
        conn = sqlite3.connect(cookies_path)
        c = conn.cursor()
        c.execute("SELECT host_key, name FROM cookies")  # Filtre les cookies non essentiels
        cookies = c.fetchall()
        conn.close()

        cookie_sites = {}
        for site, cookie in cookies:
            if cookie not in cookie_sites:
                cookie_sites[cookie] = set() #Permet de gérer la collecte unique de site web pour chaque cookie
            cookie_sites[cookie].add(site)

        # Ne garder que les cookies présents sur plusieurs sites différents
        filtered_cookies = [(site, cookie) for cookie, sites in cookie_sites.items() if len(sites) > 1 for site in sites]

        return filtered_cookies
    except sqlite3.Error as e:
        print(f"Erreur lors de la lecture des cookies : {e}")
        return []

def plot_cookie_network(cookies):
    """
    Crée un graphe des liens entre les cookies non essentiels et les sites web visités.
    Args:
        cookies (list): Une liste de tuples contenant (site web, nom du cookie).
    """
    G = nx.Graph()
    for cookie in cookies:
        website = cookie[0]
        cookie_name = cookie[1]
        G.add_node(cookie_name, type='cookie')
        G.add_node(website, type='website')
        G.add_edge(website, cookie_name)

    pos = nx.spring_layout(G)

    cookie_nodes = [node for node, attr in G.nodes(data=True) if attr['type'] == 'cookie']
    website_nodes = [node for node, attr in G.nodes(data=True) if attr['type'] == 'website']

    nx.draw_networkx_nodes(G, pos, nodelist=cookie_nodes, node_size=500, node_color='lightblue', alpha=0.8, node_shape='s')
    nx.draw_networkx_nodes(G, pos, nodelist=website_nodes, node_size=500, node_color='lightgreen', alpha=0.8)
    nx.draw_networkx_edges(G, pos, width=1.0, alpha=0.5)

    for website in website_nodes:
        nx.draw_networkx_nodes(G, pos, nodelist=[website], node_size=0)
        nx.draw_networkx_labels(G, pos, labels={website: website}, font_size=10, font_family='sans-serif')

    for cookie_node in cookie_nodes:
        if "essential" not in cookie_node.lower():  # Vérifier si le cookie est essentiel
            nx.draw_networkx_labels(G, pos, labels={cookie_node: cookie_node}, font_size=10, font_family='sans-serif')

    plt.title('Graphe des liens entre cookies non essentiels et sites web visités')
    plt.axis('off')
    plt.show()


