# функция принимает строку и возвращает цвет в зависимости от принятой строки
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
    diagonal1 = []
    diagonal2 = []
    cnt = 0
    cnt2 = num - 1
    for i in range(num):
        tmp1 = []
        tmp2 = []
        for j in range(num):
            tmp1.append(state[i][j])
            tmp2.append(state[j][i])
        # horizontal.append(tmp1)
        # vertical.append(tmp2)
        horizontal += split_ls(tmp1, rule)
        vertical += split_ls(tmp2, rule)
        diagonal1.append(tmp1[cnt])
        diagonal2.append(tmp2[cnt2])
        cnt += 1
        cnt2 -= 1

    diagonal1 = split_ls(diagonal1, rule)
    diagonal2 = split_ls(diagonal2, rule)

    win_state = [*horizontal, *vertical, *diagonal1, *diagonal2]

    if [player] * rule in win_state:
        return True
    else:
        return False


# функция для определения доступных ходов
# принимает размерность игрового поля
# возвращает словарь в котором ключ - номер клетки, а значение - координаты клетки
# пример для  игрового поля 3 Х 3
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
