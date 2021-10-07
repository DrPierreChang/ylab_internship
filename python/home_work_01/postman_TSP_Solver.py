import numpy as np
from python_tsp.exact import solve_tsp_dynamic_programming

# список городов
city_names = ["Начало", "Ул. Грибоедова, 104/25",
              "Ул. Бейкер стрит, 221б", "Ул. Большая Садовая, 302-бис",
              "Вечнозелёная Аллея, 742", "Конец"]

# словарь позиций городов
city_locations = {"Начало": (0, 2), "Ул. Грибоедова, 104/25": (2, 5),
                  "Ул. Бейкер стрит, 221б": (5, 2), "Ул. Большая Садовая, 302-бис": (6, 6),
                  "Вечнозелёная Аллея, 742": (8, 3), "Конец": (0, 2)}

# пустой список будет заполняться расчетами расстоний между городами
# как результат будет получен вложенный список/матрица всех расстояний
distance_matrix = []
# перебираем города по строкам
for i in city_names:
    # временный список будет обнуляться после добавления расчетов в основной список
    tmp = []
    # перебираем города по столбцам
    for j in city_names:
        # подсчет расстояний по данным точкам
        x1_y1 = city_locations[i]
        x2_y2 = city_locations[j]
        distance = ((x2_y2[0] - x1_y1[0])**2 + (x2_y2[1] - x1_y1[1])**2)**0.5
        tmp.append(distance)
    distance_matrix.append(tmp)

# переводим список в матрицу, чтобы использовать TSP solver
distance_matrix = np.matrix(distance_matrix)

# запускаем функцию
permutation, distance = solve_tsp_dynamic_programming(distance_matrix)

# формируем два списка: с позициями минимального моршрута и суммами

# переменная для промежуточной суммы
summ = 0
# список для добавляения накопительной суммы
sums = []
# список для добавления позиций минимального маршрута
positions = []
for i in permutation:
    positions.append(city_locations[city_names[i]])

# между каждыми двумя позициями считаем расстояние и накопительную сумму добавляем в список
for i in range(len(positions)):
    if i < len(positions)-1:
        x1_y1 = positions[i]
        x2_y2 = positions[i+1]
        distance = ((x2_y2[0] - x1_y1[0]) ** 2 + (x2_y2[1] - x1_y1[1]) ** 2) ** 0.5
        summ += distance
        sums.append(summ)

# выводим точку старта
print(positions[0], end=" -> ")

# выводим позиции и сумму расстояний по мере продвижения
print(*[str(i[0]) + '[' + str(i[1]) + ']' for i in zip(positions[1:], sums)], sep=" -> ", end=" = ")

# выводим конечну сумму
print(sums[-1])
