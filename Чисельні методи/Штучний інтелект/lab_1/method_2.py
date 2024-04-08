def solve_queens(board_size):
    # Функція для перевірки чи можна розмістити ферзя у клітинку (row, col)
    def is_safe(row, col, solution):
        # Перевірка чи немає загрози на одній вертикалі або діагоналі
        for r, c in solution:
            if c == col or abs(row - r) == abs(col - c):
                return False
        return True

    # Функція для рекурсивного розміщення ферзів
    def place_queens(row, solution):
        # Якщо досягнуто кінця дошки, додати розв'язок до списку розв'язків
        if row == board_size:
            solutions.append(solution)
            return
        # Проходження через кожну колонку у поточному рядку
        for col in range(board_size):
            # Перевірка чи можна розмістити ферзя у дану клітинку
            if is_safe(row, col, solution):
                # Рекурсивний виклик для розміщення ферзя у наступному рядку
                place_queens(row + 1, solution + [(row, col)])

    # Створення порожнього списку для зберігання розв'язків
    solutions = []
    # Почати рекурсивний пошук з першого рядку та порожнього розв'язку
    place_queens(0, [])
    return solutions

# Розмір шахової дошки
N = 8

# Знайти розв'язки
solutions = solve_queens(N)

# Вивести кількість знайдених розв'язків
print(f"Знайдено {len(solutions)} розв'язків для шахової дошки розміром {N}x{N}.")

# Вивести розв'язки
for i, solution in enumerate(solutions):
    print(f"Розв'язок {i + 1}:")
    for row, col in solution:
        line = ['.'] * N
        line[col] = 'Q'
        print(' '.join(line))
    print()
