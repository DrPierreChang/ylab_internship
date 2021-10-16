#!/usr/bin/env python3
from math import inf as infinity
from random import choice
import platform
# import time
from os import system
from tictactoe import *

"""
Игра "Обратные крестики нолики" с использованием алгоритма minimax
"""

# значения score для человека и компьютера
HUMAN = -1
COMP = +1

# указываем размерность игрового поля
num = 10
rule = 5

# указываем цвет сообщения при победе/проигрыше.
# функция вернет желтый цвет при передаче в функцию любого символа кроме x, o, end
win_loose_color = choose_color('yellow')
# функция вернет код ANSi для завершения предыдущего форматирования
end_color = choose_color('end')

# генерируем игровое поле с заданной размерностью
board = ([[0]*num for x in range(num)])

# Словарь. Ключ - номер клетки. Значение - ее координаты.
moves = valid_moves(num)


def evaluate(state):
    """
    Функция оценивает ход, приводит ли он к победе
    :param state: текущее состояние игрового поля
    :return: +1 если выигрывает человек; -1 если выигрывает компьютер; 0 при ничье
    """
    if wins(state, COMP, num, rule):
        score = -1
    elif wins(state, HUMAN, num, rule):
        score = +1
    else:
        score = 0

    return score


def game_over(state):
    """
    Проверяем, победил ли кто-то из игроков
    :param state: текущее состояние игрового поля
    :return: True - есть победитель False - нет победителя
    """

    return wins(state, HUMAN, num, rule) or wins(state, COMP, num, rule)


def empty_cells(state):
    """
    Каждая свободная клетка добавляется в список
    :param state: текущее состояние игрового поля
    :return: возвращается список свободных клеток
    """
    cells = []

    # идем по строкам и столбцам, проверяя свободная ли клетка
    for x, row in enumerate(state):
        for y, cell in enumerate(row):
            if cell == 0:
                cells.append([x, y])

    return cells


def valid_move(x, y):
    """
    Ход игрока возможен, если клетка с указанными координатами свободна
    :param x: X координата
    :param y: Y координата
    :return: Возвращается True, если клетка свободна False, если она занята
    """
    if [x, y] in empty_cells(board):
        return True
    else:
        return False


def set_move(x, y, player):
    """
    Функция принимает координаты и фиксирует ход игрока, если такая клетка свободна
    :param x: X координата
    :param y: Y координата
    :param player: игрок, который сейчас ходит
    """

    # проверяем, свободна ли клетка
    if valid_move(x, y):
        board[x][y] = player
        return True
    else:
        return False


def minimax(state, depth, player):
    """
    Функция возвращает координаты самого выгодного хода для компьютер
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

    # перебираем в рекурсии свободные клетки на каждой итерации моделируя ход компьютера и человека
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


def clean():
    """
    Функция очищает консоль
    """
    os_name = platform.system().lower()
    if 'windows' in os_name:
        system('cls')
    else:
        system('clear')


def render(state, c_choice, h_choice):
    """
    Функцию выводит в консоль текущее состояние игрового поля
    :param state: текущее состояние игрового поля
    """

    chars = {
        -1: h_choice,
        +1: c_choice,
        0: ' '
    }
    # линия определяет границы игрового поля
    str_line = '----------------------------------------------------------------------'

    print('\n' + str_line)
    cnt = 1

    # в этом цикле рисуется игровое поле и определяется цвет X и O
    for row in state:
        for cell in row:
            symbol = chars[cell]
            start_color = choose_color(symbol)
            if cnt < 10:
                print(f" {cnt}| {start_color}{symbol}{end_color} |", end="")
            elif cnt == 100:
                print(f"{cnt}|{start_color}{symbol}{end_color} |", end="")
            else:
                print(f"{cnt}| {start_color}{symbol}{end_color} |", end="")
            cnt += 1
        print('\n' + str_line)


def ai_turn(c_choice, h_choice):
    """
    Первые 10 шагов компьютер делает в случайном порядке.
    Далее идет обращение к рекурсивной функции основанной на алгоритме minimax
    Глубина рекурсии начинается с 2 и возрастает по мере увеличения свободных клеток.
    Это значит, сложность игры постепенно возрастает, так как решения компьютера становятся все более взвешенными.
    :param c_choice: за кого играет компьютер X or O
    :param h_choice: за кого играет человек X or O
    """
    # количество пустых клеток
    empty_cells_amount = len(empty_cells(board))

    # выход из функции если игра закончилась
    if empty_cells_amount == 0 or game_over(board):
        return

    clean()
    print(f'Computer turn [{c_choice}]')
    render(board, c_choice, h_choice)

    # первые десять ходов компьютер делает в случайном порядке
    if empty_cells_amount > 80:
        # выбираем случайную строку
        x = choice(list(range(num)))
        # выбираем случайный столбец
        y = choice(list(range(num)))
    # с этого момента компьютер принимает решения на основе алгоритма minimax
    elif empty_cells_amount > 40:
        depth = 2
        move = minimax(board, depth, COMP)
        x, y = move[0], move[1]
    elif empty_cells_amount > 30:
        depth = 3
        move = minimax(board, depth, COMP)
        x, y = move[0], move[1]
    elif empty_cells_amount > 20:
        depth = 4
        move = minimax(board, depth, COMP)
        x, y = move[0], move[1]
    elif empty_cells_amount > 10:
        depth = 5
        move = minimax(board, depth, COMP)
        x, y = move[0], move[1]
    else:
        depth = 7
        move = minimax(board, depth, COMP)
        x, y = move[0], move[1]

    # фиксируем ход на игровом поле
    set_move(x, y, COMP)
    # time.sleep(1)


def human_turn(c_choice: str, h_choice: str):
    """
    Человек ходит исходя из свободных клеток
    :param c_choice: X или O
    :param h_choice: X или O
    """

    # проверяем оставшееся количество свободных клеток
    empty_cells_amount = len(empty_cells(board))
    if empty_cells_amount == 0 or game_over(board):
        return

    move = -1
    clean()
    print(f'Human turn [{h_choice}]')
    render(board, c_choice, h_choice)

    # просим игрока ввести номер клетки для своего хода
    while move < 1 or move > 100:
        try:
            move = int(input('Use numpad (1..100): '))
            coord = moves[move]
            # если клетка доступна для хода и введено корректный номер
            can_move = set_move(coord[0], coord[1], HUMAN)

            # если клетка не доступна для хода или введено некорректное значение
            if not can_move:
                print('Bad move')
                move = -1
        except (EOFError, KeyboardInterrupt):
            print('Bye')
            exit()
        except (KeyError, ValueError):
            print('Bad choice')


def main():
    """
    Главная функция, которая вызывает все остальные функции
    """
    clean()
    h_choice = ''  # выбор человека: играть за X или O
    # c_choice = ''  # выбор компьютера: играть за X или O
    first = ''  # человек ходит первым или нет

    # Ждем пока человек не выберет X или O для начала игры
    while h_choice != 'O' and h_choice != 'X':
        try:
            print('')
            h_choice = input('Choose X or O\nChosen: ').upper()
        except (EOFError, KeyboardInterrupt):
            print('Bye')
            exit()
        except (KeyError, ValueError):
            print('Bad choice')

    # Когда человек выбрал X или O, оставшийся вариант достается компьютеру
    if h_choice == 'X':
        c_choice = 'O'
    else:
        c_choice = 'X'

    # Ждем, пока человек выберет: играть первым или вторым
    clean()
    while first != 'Y' and first != 'N':
        try:
            first = input('First to start?[y/n]: ').upper()
        except (EOFError, KeyboardInterrupt):
            print('Bye')
            exit()
        except (KeyError, ValueError):
            print('Bad choice')

    # Основной цикл. Пока есть пустые клетки и игра не закончена, человек и компьютер ходят по-очереди
    while len(empty_cells(board)) > 0 and not game_over(board):
        if first == 'N':
            ai_turn(c_choice, h_choice)
            first = ''

        human_turn(c_choice, h_choice)
        ai_turn(c_choice, h_choice)

    # Если игра закончилась, то происходит проверка того, кто выиграл и выводится сообщение о победе/проигрыше
    if wins(board, HUMAN, num, rule):
        clean()
        print(f'Human turn [{h_choice}]')
        render(board, c_choice, h_choice)
        print(f"{win_loose_color}YOU LOOSE!{end_color}")
    elif wins(board, COMP, num, rule):
        clean()
        print(f'Computer turn [{c_choice}]')
        render(board, c_choice, h_choice)
        print(f"{win_loose_color}YOU WIN!{end_color}")
    else:
        clean()
        render(board, c_choice, h_choice)
        print(f"{win_loose_color}DRAW!{end_color}")

    exit()


if __name__ == '__main__':
    main()
