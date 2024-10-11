from algorithms import dfs_recursive, dfs_iterative, bfs_recursive, bfs_iterative
from task1 import G_ukraine

dfs_path_recursive = dfs_recursive(G_ukraine, "Київ", 'Запоріжжя')
dfs_path_iterative = dfs_iterative(G_ukraine, "Київ", 'Запоріжжя')
bfs_path_recursive = bfs_recursive(G_ukraine, "Київ", 'Запоріжжя')
bfs_path_iterative = bfs_iterative(G_ukraine, "Київ", 'Запоріжжя')

print(f"Шлях з Києва до Запоріжжя за допомогою рекурсивного DFS: {dfs_path_recursive}")
print(f"Шлях з Києва до Запоріжжя за допомогою ітеративного DFS: {dfs_path_iterative}")
print(f"Шлях з Києва до Запоріжжя за допомогою рекурсивного BFS: {bfs_path_recursive}")
print(f"Шлях з Києва до Запоріжжя за допомогою ітеративного BFS: {bfs_path_iterative}")

print(f"Оскільки рекурсивний та ітеративний дають одинакові результати, порівнюємо будь який з результатів DFS та BFS")

if dfs_path_recursive == bfs_path_iterative:
    print("\nDFS та BFS знайшли однаковий шлях.")
else:
    print("\nРізниця між шляхами:")
    print(f"DFS обрав шлях: {dfs_path_recursive}")
    print(f"BFS обрав шлях: {bfs_path_iterative}")
    print("DFS може знайти довший шлях, тому що він намагається заглибитися в граф перш ніж перевіряти інші сусідні вершини.")
    print("BFS завжди знаходить найкоротший шлях, оскільки він спочатку досліджує всі найближчі вузли.")


