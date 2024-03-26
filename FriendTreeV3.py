import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt
import os

# Lire le fichier Excel
excel_file = "/Users/theronjoshua/Desktop/test2.xlsx"
df = pd.read_excel(excel_file, index_col=0)  # Utilisez la première colonne comme index

# Créer un graphe
G = nx.Graph()

# Ajouter des nœuds (personnages) à partir des lignes et des colonnes du DataFrame
characters = df.index.tolist()  # Récupérez les noms des personnages
G.add_nodes_from(characters)

# Ajouter des arêtes (relations) à partir des données du DataFrame
for character1 in characters:
    for character2 in characters:
        relation_type = df.loc[character1, character2]  # Obtenez le type de relation entre les personnages
        if pd.notna(relation_type):  # Vérifie si la valeur de la relation n'est pas NaN
            G.add_edge(character1, character2, relation_type=relation_type)

# Dessiner le graphe
pos = nx.spring_layout(G, center=(0.5, 0.5), seed=42)  # positions for all nodes with rounding
nx.draw_networkx_nodes(G, pos, node_size=700)
nx.draw_networkx_edges(G, pos, width=6)

# Étiqueter les nœuds
node_labels = {node: node for node in G.nodes()}
nx.draw_networkx_labels(G, pos, labels=node_labels, font_size=20, font_family='sans-serif')

# Définir les couleurs des arêtes en fonction du type de relation
edge_colors = {'Couple': 'blue', 'Amitier': 'green', 'Animsoité': 'red', 'Crush': 'orange'}
edge_colors_list = []
for u, v in G.edges():
    if pd.notna(G[u][v]['relation_type']):  # Vérifie si la valeur de la relation n'est pas NaN
        edge_colors_list.append(edge_colors.get(G[u][v]['relation_type'], 'black'))  # Utilise 'black' si la relation n'est pas dans le dictionnaire
    else:
        edge_colors_list.append('black')  # Utilise 'black' si la valeur de la relation est NaN
nx.draw_networkx_edges(G, pos, width=6, edge_color=edge_colors_list)

# Afficher la légende
legend_elements = []
for label, color in edge_colors.items():
    legend_elements.append(plt.Line2D([0], [0], marker='o', color='w', label=label, markerfacecolor=color, markersize=10))
plt.legend(handles=legend_elements, loc='upper left')

# Afficher le graphe sans les axes
plt.axis('off')

# Enregistrer l'image PNG sur le bureau
desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
image_path = os.path.join(desktop_path, "friend_tree.png")
plt.savefig(image_path)

# Afficher le graphe
plt.show()
