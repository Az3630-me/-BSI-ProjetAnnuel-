import sqlite3
import networkx as nx
import matplotlib.pyplot as plt
from collections import defaultdict

# Chemin vers la base de données cookies.sqlite de Firefox
#firefox_cookies_db = '/home/kali/Documents/cookies.sqlite'

# Fonction pour créer et visualiser le graphe des cookies regroupés par cookie
def get_mozilla_cookies(firefox_cookies_db):
    conn = sqlite3.connect(firefox_cookies_db)
    cursor = conn.cursor()

    # Requête SQL pour récupérer les informations sur les cookies
    query = """
        SELECT
            host,
            name
        FROM
            moz_cookies
    """

    cursor.execute(query)
    cookies = cursor.fetchall()

    # Regrouper les sites par cookie
    cookie_sites = defaultdict(list)
    for host, name in cookies:
        cookie_sites[name].append(host)

    # Création d'un graphe non dirigé pour les cookies regroupés
    G = nx.Graph()

    for cookie, sites in cookie_sites.items():
        if len(sites) > 1:
            # Ajouter les cookies comme des nœuds avec la forme triangle (^)
            G.add_node(cookie, shape='^', color='green', node_type='cookie')
            # Ajouter des arêtes entre les sites et le cookie
            for site in sites:
                G.add_edge(cookie, site)

            # Ajouter les sites comme des nœuds avec la forme de cercle (o)
            for site in sites:
                G.add_node(site, shape='o', color='skyblue', node_type='site')

    # Définir les attributs des nœuds pour le dessin
    node_shapes = nx.get_node_attributes(G, 'shape')
    node_colors = nx.get_node_attributes(G, 'color')
    node_types = nx.get_node_attributes(G, 'node_type')

    # Définir la disposition du graphe
    pos = nx.spring_layout(G)

    # Affichage du graphe avec les étiquettes
    plt.figure(figsize=(12, 8))

    # Dessiner les nœuds selon leurs attributs définis
    for node, shape in node_shapes.items():
        if node_types[node] == 'cookie':
            nx.draw_networkx_nodes(G, pos, nodelist=[node], node_shape=shape, node_color=node_colors[node], node_size=1500)
        else:
            nx.draw_networkx_nodes(G, pos, nodelist=[node], node_shape=shape, node_color=node_colors[node], node_size=1000)

    # Dessiner les étiquettes des nœuds (cookies et sites)
    node_labels = {}
    for node in G.nodes():
        if node_types[node] == 'cookie':
            # Récupérer le nom du cookie à partir de node
            node_labels[node] = node
        else:
            # Récupérer le nom complet du site (host) à partir de node
            node_labels[node] = node

    nx.draw_networkx_labels(G, pos, labels=node_labels, font_size=10, font_color='black', font_weight='bold')

    # Dessiner les arêtes
    nx.draw_networkx_edges(G, pos, edgelist=G.edges(), edge_color='gray', arrows=False)

    # Afficher le graphe
    plt.title('Graphe des relations entre les sites via les cookies de Firefox (cookies en triangle, sites en cercle)')
    plt.tight_layout()
    plt.show()

    conn.close()


	
