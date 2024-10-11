import networkx as nx
import matplotlib.pyplot as plt

cities = ['Київ', 'Львів', 'Одеса', 'Харків', 'Дніпро', 'Запоріжжя']
edges_ukraine = [('Київ', 'Львів'), ('Київ', 'Одеса'), ('Київ', 'Харків'), 
                 ('Київ', 'Дніпро'), ('Київ', 'Запоріжжя'), 
                 ('Львів', 'Одеса'), ('Харків', 'Дніпро'), ('Одеса', 'Запоріжжя')]

G_ukraine = nx.Graph()
G_ukraine.add_nodes_from(cities)
G_ukraine.add_edges_from(edges_ukraine)

plt.figure()
pos = nx.spring_layout(G_ukraine)
nx.draw(G_ukraine, pos, with_labels=True)
plt.title("міста України")
plt.show()

print(f"Кількість вершин: {G_ukraine.number_of_nodes()}")
print(f"Кількість ребер: {G_ukraine.number_of_edges()}")
print(f"Ступінь вершин: {G_ukraine.degree()}")
