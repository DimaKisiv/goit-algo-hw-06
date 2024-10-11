from algorithms import dijkstra
from task1 import G_ukraine
import pandas as pd

start_cities = ['Київ', 'Львів', 'Одеса', 'Харків', 'Дніпро', 'Запоріжжя']
all_paths = {}

for start_city in start_cities:
    distances = dijkstra(G_ukraine, start_city)
    all_paths[start_city] = distances

df_paths = pd.DataFrame(all_paths).T
print("\nТаблиця відстаней між всіма містами:")
print(df_paths)


