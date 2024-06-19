import os
import sqlite3
import matplotlib.pyplot as plt
import networkx as nx

def get_mozilla_cookies(cookies_path):
    if not os.path.exists(cookies_path):
        print("Le chemin spécifié vers le fichier de cookies n'existe pas.")
        return []
    conn = sqlite3.connect(cookies_path)
    c = conn.cursor()
    c.execute("SELECT host, name, value FROM moz_cookies")
    cookies = c.fetchall()
    conn.close()
    cookie_sites = {}
    for site, cookie, value in cookies:
        if cookie not in cookie_sites:
            cookie_sites[cookie] = set()  # Permet de gérer la collecte unique de site web pour chaque cookie
        cookie_sites[cookie].add(site)

    # Ne garder que les cookies présents sur plusieurs sites différents
    filtered_cookies = [(site, cookie) for cookie, sites in cookie_sites.items() if len(sites) > 1 for site in sites]

    return filtered_cookies

def plot_cookie_network(cookies):
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

    nx.draw_networkx_labels(G, pos, labels={node: node for node in website_nodes}, font_size=10, font_family='sans-serif')
    nx.draw_networkx_labels(G, pos, labels={node: node for node in cookie_nodes}, font_size=10, font_family='sans-serif')

    plt.title('Graphe des liens entre cookies non essentiels et sites web visités')
    plt.axis('off')
    plt.show()