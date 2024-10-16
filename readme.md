# Результати пошуку шляхів у графі

## Основна інформація про граф

- **Кількість вершин**: 6
- **Кількість ребер**: 8
- **Ступінь вершин**:
  - Київ: 5
  - Львів: 2
  - Одеса: 3
  - Харків: 2
  - Дніпро: 2
  - Запоріжжя: 2

## Порівняння шляхів для DFS та BFS

### Результати пошуку шляху з Києва до Запоріжжя

- **Рекурсивний DFS**: `['Київ', 'Львів', 'Одеса', 'Запоріжжя']`
- **Ітеративний DFS**: `['Київ', 'Львів', 'Одеса', 'Запоріжжя']`
- **Рекурсивний BFS**: `['Київ', 'Запоріжжя']`
- **Ітеративний BFS**: `['Київ', 'Запоріжжя']`

Оскільки рекурсивний та ітеративний варіанти DFS і BFS дають однакові результати, порівнюємо результати **DFS** та **BFS**.

## Різниця між шляхами

- **DFS обрав шлях**: `['Київ', 'Львів', 'Одеса', 'Запоріжжя']`
- **BFS обрав шлях**: `['Київ', 'Запоріжжя']`

### Пояснення

- **DFS (глибина-перший пошук)** може знайти довший шлях, оскільки він намагається заглибитися в граф, вибираючи одну гілку перш ніж перевіряти інші сусідні вершини.
  
- **BFS (ширина-перший пошук)** завжди знаходить найкоротший шлях, оскільки він спочатку досліджує всі найближчі вузли, перш ніж заглиблюватись далі в граф.

### Висновок

**DFS** часто обирає глибші шляхи, що може призводити до довших маршрутів, тоді як **BFS** забезпечує найкоротший шлях, особливо корисний у графах без ваги, де відстань між вершинами мінімальна.
