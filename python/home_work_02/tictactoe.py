import numpy as np


# функция принимает строку и возвращает цвет в зависимости от значения
# на O возвращает зеленый
# на X возвращает красный
# на '' возвращает конец форматирования
# во всех остальных случаях возвращает желтый
def choose_color(symbol):
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
    if (symbol.lower()) == 'o':
        color = Bcolors.OKGREEN
    elif (symbol.lower()) == 'x':
        color = Bcolors.FAIL
    elif symbol == '':
        color = Bcolors.ENDC
    else:
        color = Bcolors.WARNING
    return color


# функция для выбора всех возможных "5 в ряд" в строке/столбце/диагонали
def split_ls(ls: list, rule) -> list:
    return [ls[i:i + rule] for i in range(len(ls) - 4)]


# функция проверяет на победу
def wins(state, player, num: int, rule: int) -> bool:
    """
    This function tests if a specific player wins. Possibilities:
    * Three rows    [X X X] or [O O O]
    * Three cols    [X X X] or [O O O]
    * Two diagonals [X X X] or [O O O]
    :param state: the state of the current board
    :param player: a human or a computer
    :param num: размерность игрового поля
    :param rule: правило - сколько необходимо символов в ряд
    :return: True if the player wins
    """
    # Example for 3 X 3:
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

    horizontal = []
    vertical = []
    for i in range(num):
        tmp1 = []
        tmp2 = []
        for j in range(num):
            tmp1.append(state[i][j])
            tmp2.append(state[j][i])
        horizontal += split_ls(tmp1, rule)
        vertical += split_ls(tmp2, rule)

    test = np.array(state)
    tmp = []

    diags = [test[::-1, :].diagonal(i) for i in range(-9, 10)]
    diags.extend(test.diagonal(i) for i in range(9, -10, -1))
    for i in diags:
        if len(i) >= 5:
            for j in (split_ls(i, rule)[0:]):
                tmp.append(list(j))

    test2 = [*horizontal, *vertical, *tmp]

    if [player] * rule in test2:
        return True
    else:
        return False


# функция для определения доступных ходов
# принимает размерность игрового поля
# возвращает словарь в котором ключ - номер клетки, а значение - координаты клетки
# пример для  игрового поля 3 x 3:
# moves = {
#     1: [0, 0], 2: [0, 1], 3: [0, 2],
#     4: [1, 0], 5: [1, 1], 6: [1, 2],
#     7: [2, 0], 8: [2, 1], 9: [2, 2],
# }
def valid_moves(num: int) -> dict:
    moves = dict()
    cnt = 1
    for i in range(num):
        for j in range(num):
            moves[cnt] = [i, j]
            cnt += 1
    return moves