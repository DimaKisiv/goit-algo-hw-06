import networkx as nx
import matplotlib.pyplot as plt

cities = ['Київ', 'Львів', 'Одеса', 'Харків', 'Дніпро', 'Запоріжжя']
edges_ukraine = [
    ('Київ', 'Львів', 2), ('Київ', 'Одеса', 4), ('Київ', 'Харків', 1), 
    ('Київ', 'Дніпро', 5), ('Київ', 'Запоріжжя', 7), 
    ('Львів', 'Одеса', 3), ('Харків', 'Дніпро', 2), ('Одеса', 'Запоріжжя', 1)
]

G_ukraine = nx.Graph()
G_ukraine.add_nodes_from(cities)
G_ukraine.add_weighted_edges_from(edges_ukraine)

plt.figure()
pos = nx.spring_layout(G_ukraine)
edge_labels = nx.get_edge_attributes(G_ukraine, 'weight')
nx.draw(G_ukraine, pos, with_labels=True)
nx.draw_networkx_edge_labels(G_ukraine, pos, edge_labels=edge_labels)
plt.title("міста України")
plt.show()

print(f"Кількість вершин: {G_ukraine.number_of_nodes()}")
print(f"Кількість ребер: {G_ukraine.number_of_edges()}")
print(f"Ступінь вершин: {G_ukraine.degree()}")
