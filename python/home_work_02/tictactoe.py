import numpy as np


def choose_color(text: str):
    # функция принимает строку и возвращает цвет в зависимости от значения
    # на O возвращает зеленый
    # на X возвращает красный
    # на yellow возвращает желтый
    # во всех остальных случаях возвращает конец форматирования
    # Цвета в кодировке ANSI
    class Bcolors:
        # HEADER = '\033[95m'
        # OKBLUE = '\033[94m'
        # OKCYAN = '\033[96m'
        OKGREEN = '\033[92m'
        WARNING = '\033[93m'
        FAIL = '\033[91m'
        ENDC = '\033[0m'
        # BOLD = '\033[1m'
        # UNDERLINE = '\033[4m'
    # если принят символ O
    if (text.lower()) == 'o':
        color = Bcolors.OKGREEN
    # если принят символ X
    elif (text.lower()) == 'x':
        color = Bcolors.FAIL
    # если принята строка 'yellow'
    elif text == 'yellow':
        color = Bcolors.WARNING
    # во всех остальных случаях
    else:
        color = Bcolors.ENDC
    return color


# функция для выбора всех возможных "5 в ряд" в строке/столбце/диагонали
def split_ls(ls: list, rule) -> list:
    return [ls[i:i + rule] for i in range(len(ls) - 4)]


# функция проверяет на победу
def wins(state, player, num: int, rule: int) -> bool:
    """
    Эта функция проверяет проиграл ли игрок. Возможные случаи:
    * 5 в ряд по строке   [X X X X X] или [O O O O O]
    * 5 в ряд по столбцу [X X X X X] или [O O O O O]
    * 5 в ряд по любой диагонали [X X X X X] или [O O O O O]
    :param state: текущее состояние игрового поля
    :param player: человек или компьютер
    :param num: размерность игрового поля
    :param rule: правило - сколько необходимо символов в ряд
    :return: True если игрок проиграл
    """
    # Пример state для игрового поля 3 X 3:
    # win_state = [
    #     # горизонтальные ряды
    #     [state[0][0], state[0][1], state[0][2]],
    #     [state[1][0], state[1][1], state[1][2]],
    #     [state[2][0], state[2][1], state[2][2]],
    #     # вертикальные ряды
    #     [state[0][0], state[1][0], state[2][0]],
    #     [state[0][1], state[1][1], state[2][1]],
    #     [state[0][2], state[1][2], state[2][2]],
    #     # диагональные ряды
    #     [state[0][0], state[1][1], state[2][2]],
    #     [state[2][0], state[1][1], state[0][2]],
    # ]

    # этот список будет заполняться всеми горизонтальными пятерками
    horizontal = []
    # этот список будет заполняться всеми вертикальными пятерками
    vertical = []
    # перебираем все варианты
    for i in range(num):
        tmp1 = []
        tmp2 = []
        for j in range(num):
            tmp1.append(state[i][j])
            tmp2.append(state[j][i])
        # добавляем в список все возможные пять в ряд из текущей строки
        horizontal += split_ls(tmp1, rule)
        # добавляем в список все возможные пять в ряд из текущего столбца
        vertical += split_ls(tmp2, rule)

    # чтобы извлечь все диагонали нужно воспользоваться np.array
    test = np.array(state)
    tmp = []
    # получаем все диагонали
    diags = [test[::-1, :].diagonal(i) for i in range(-9, 10)]
    diags.extend(test.diagonal(i) for i in range(9, -10, -1))
    # перебираем полученные диагонали и оставляем только те, которые >= 5
    for i in diags:
        if len(i) >= 5:
            # из выбранной диагонали извлекаем все "5 в ряд"
            for j in (split_ls(i, rule)[0:]):
                tmp.append(list(j))

    # объединяем горизонтальные, вертикальные и диагональные "5 в ряд" в один список
    test2 = [*horizontal, *vertical, *tmp]

    # если любая пятерка будет полностью заполнена значениями одного из игроков (+1 или -1)
    # то этот игрок проигрывает
    if [player] * rule in test2:
        return True
    else:
        return False


def valid_moves(num: int) -> dict:
    # функция для определения доступных ходов
    # принимает размерность игрового поля
    # возвращает словарь в котором ключ - номер клетки, а значение - координаты клетки
    # пример для  игрового поля 3 x 3:
    # moves = {
    #     1: [0, 0], 2: [0, 1], 3: [0, 2],
    #     4: [1, 0], 5: [1, 1], 6: [1, 2],
    #     7: [2, 0], 8: [2, 1], 9: [2, 2],
    # }
    moves = dict()
    cnt = 1
    for i in range(num):
        for j in range(num):
            moves[cnt] = [i, j]
            cnt += 1
    return moves
