import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt
import os

# Read Exel files
excel_file = "/Users/theronjoshua/Desktop/test2.xlsx"
df = pd.read_excel(excel_file, index_col=0)

# Créer un graphe
G = nx.Graph()

#Create Node
characters = df.index.tolist()  
G.add_nodes_from(characters)

# add type of relation to the DataFrame
for character1 in characters:
    for character2 in characters:
        relation_type = df.loc[character1, character2]  
        if pd.notna(relation_type):  
            G.add_edge(character1, character2, relation_type=relation_type)

# Define the dataframe
pos = nx.spring_layout(G, center=(0.5, 0.5), seed=42)
nx.draw_networkx_nodes(G, pos, node_size=700)
nx.draw_networkx_edges(G, pos, width=6)

# Name the nodes
node_labels = {node: node for node in G.nodes()}
nx.draw_networkx_labels(G, pos, labels=node_labels, font_size=20, font_family='sans-serif')

# Define color of emotion 
edge_colors = {'Couple': 'blue', 'Amitier': 'green', 'Animsoité': 'red', 'Crush': 'orange'}
edge_colors_list = []
for u, v in G.edges():
    if pd.notna(G[u][v]['relation_type']):
        edge_colors_list.append(edge_colors.get(G[u][v]['relation_type'], 'black'))
    else:
        edge_colors_list.append('black')
nx.draw_networkx_edges(G, pos, width=6, edge_color=edge_colors_list)

#Show Legende
legend_elements = []
for label, color in edge_colors.items():
    legend_elements.append(plt.Line2D([0], [0], marker='o', color='w', label=label, markerfacecolor=color, markersize=10))
plt.legend(handles=legend_elements, loc='upper left')

plt.axis('off')

#Save Png
desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
image_path = os.path.join(desktop_path, "friend_tree.png")
plt.savefig(image_path)

#Show graph
plt.show()
