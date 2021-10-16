# Игра "Обратные крестики-нолики"
<p align="center">
    <img src="images/win.png" alt="game example" width="700">
</p>

### <p align="center">Общая логика работы игры. Функция main</p>

1) Выбираем - играть за O или X:
    - переменные h_choice и c_choice хранят выбор человека и компьютера

2) Выбираем - начать первым или вторым:
    - переменная first - хранит выбор человека: Y или N
3) Запускается основной цикл, в котором человек и компьютер 
ходят по-очереди, пока есть пустые клетки и игра не закончена
~~~~python
while len(empty_cells(board)) > 0 and not game_over(board):
    if first == 'N':
        ai_turn(c_choice, h_choice)
        first = ''
      
    human_turn(c_choice, h_choice)
    ai_turn(c_choice, h_choice)
...
~~~~
4) Если игра закончилась, то проходит проверка того, кто выиграл,
и выводится соответствующее сообщение
~~~~python
if wins(board, HUMAN, num, rule):
    clean()
    print(f'Human turn [{h_choice}]')
    render(board, c_choice, h_choice)
    print(f"{win_loose_color}YOU WIN!{end_color}")
...
~~~~

<p align="center"><img src="images/main.png" alt = "main function" width="700"></p>

### <p align = "center">Как ходит человек</p>

Игра человека обеспечивается функцией
~~~~python
def human_turn(c_choice, h_choice):...
~~~~

Игрок выбирает из свободных клеток.

В цикле его просят ввести номер клетки
~~~~python
    while move < 1 or move > 100:
        try:
            move = int(input('Use numpad (1..100): '))
            coord = moves[move]
            can_move = set_move(coord[0], coord[1], HUMAN)
    ....
~~~~
Далее после проверок на валидность значение фиксируется на игровом поле.

### <p align="center">Как ходит компьютер</p>

Игра компьютера задается функцией
~~~~python
def ai_turn(c_choice: str, h_choice: str):
   ...
~~~~

- Первые десять ходов компьютер делает в случайном порядке
~~~~python
if empty_cells_amount > 80:
    # выбираем случайную строку
    x = choice(list(range(num)))
    # выбираем случайный столбец
    y = choice(list(range(num)))
~~~~
- Далее идет обращение к рекурсивной функции основанной на
  алгоритме minimax. Глубина рекурсии начинается с 2 и возрастает по мере
  уменьшения количества свободных клеток. Это значит, что сложность игры
  постепенно увеличивается, так как решения компьютера становятся все более
  взвешенными.
  
~~~~python
elif empty_cells_amount > 40:
    depth = 2
    move = minimax(board, depth, COMP)
    x, y = move[0], move[1]
elif empty_cells_amount > 30:
    depth = 3
    move = minimax(board, depth, COMP)
    x, y = move[0], move[1]
...
~~~~

- Когда функция minimax возвращает координаты наиболее выгодного хода,
то он фиксируется на игровом поле
~~~~python
  set_move(x, y, COMP)
~~~~

### <p align="center">Алгоритм Minimax</p>

Реализация алгоритма выглядит следующим образом:
~~~~python
def minimax(state, depth, player):
    """
    Функция возвращает координаты самого выгодного хода для компьютера
    :param state: текущее состояние игрового поля
    :param depth: глубина рекурсии
    :param player: Человек или Компьютер HUMAN or COMP
    :return: возвращается лист с [координатой лучшей строки, координатой лучшей колонки, лучшим результатом]
    """
    # при выборе выгодного хода компьютер использует параметр score - лучший результат
    # при правильном ходе score увеличивается, при ошибочном уменьшается
    # изначально он равен -infinity. И компьютеру необходимо максимизировать это значение
    if player == COMP:
        best = [-1, -1, -infinity]
    # изначальный score человека равен +infinity.
    # и человек должен минимизировать это значение, совершая правильные ходы
    else:
        best = [-1, -1, +infinity]
        
    # если в рекурсии достигнуто дно, то возвращается лучший результат
    if depth == 0 or game_over(state):
        score = evaluate(state)
        return [-1, -1, score]

    # перебираем в рекурсии свободные клетки,
    # на каждой итерации чередуя и моделируя ход компьютера и человека
    for cell in empty_cells(state):
        x, y = cell[0], cell[1]
        state[x][y] = player
        score = minimax(state, depth - 1, -player)
        state[x][y] = 0
        score[0], score[1] = x, y

        # сохраняем текущий лучший результат для компьютера
        if player == COMP:
            if score[2] > best[2]:
                best = score  # max value
        # сохраняем текущий лучший результат для человека
        else:
            if score[2] < best[2]:
                best = score  # min value

    return best
~~~~
Так выглядит пример визуализации дерева рекурсии
<p align="center">
    <img src="images/tree.png" width="600">
</p>

### <p align="center">tictactoe.py</p>


В файл tictactoe.py вынесены некоторые функции:

~~~~python
def choose_color(text: str): ...
~~~~~

Функция принимает строку и возвращает цвет в виде [ANSI escape code](https://en.wikipedia.org/wiki/ANSI_escape_code) в зависимости от принятого значения

Это необходимо, чтобы раскрасить X, O и другие элементы разными цветами при игре в консоли

<p align="center"><img src="images/loose.png" alt = "example of function return" width="450"></p>

### <p align="center">Источники информации</p>
Google:
- [Print Colors in Python terminal](https://www.geeksforgeeks.org/print-colors-python-terminal/)
- [ПРИНЦИП МАКСИМИНА (МИНИМАКСА)](http://www.math.mrsu.ru/text/courses/method/princip_maxmin_minmax.htm)
- [Минимакс и максимакс](https://math.semestr.ru/games/minimax.php)

Wiki:
- [ANSI escape code](https://en.wikipedia.org/wiki/ANSI_escape_code)

Stack Overflow:
- [Get all the diagonals in a matrix/list of lists in Python](https://stackoverflow.com/questions/6313308/get-all-the-diagonals-in-a-matrix-list-of-lists-in-python)
- [What is wrong with my minimax algorithm for tictactoe](https://stackoverflow.com/questions/31617469/what-is-wrong-with-my-minimax-algorithm-for-tictactoe)

YouTube
- [Algorithms Explained – minimax and alpha-beta pruning](https://youtu.be/l-hh51ncgDI)
- [What is the Minimax Algorithm? - Artificial Intelligence](https://youtu.be/KU9Ch59-4vw)
