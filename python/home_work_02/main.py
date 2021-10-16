#!/usr/bin/env python3
from math import inf as infinity
from random import choice
import platform
import time
from os import system
from tictactoe import *

"""
An implementation of Minimax AI Algorithm in Tic Tac Toe,
using Python.
"""

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
    Function to heuristic evaluation of state.
    :param state: the state of the current board
    :return: +1 if the computer wins; -1 if the human wins; 0 draw
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
    This function test if the human or computer wins
    :param state: the state of the current board
    :return: True if the human or computer wins
    """
    return wins(state, HUMAN, num, rule) or wins(state, COMP, num, rule)


def empty_cells(state):
    """
    Each empty cell will be added into cells' list
    :param state: the state of the current board
    :return: a list of empty cells
    """
    cells = []

    for x, row in enumerate(state):
        for y, cell in enumerate(row):
            if cell == 0:
                cells.append([x, y])

    return cells



def valid_move(x, y):
    """
    A move is valid if the chosen cell is empty
    :param x: X coordinate
    :param y: Y coordinate
    :return: True if the board[x][y] is empty
    """
    if [x, y] in empty_cells(board):
        return True
    else:
        return False


def set_move(x, y, player):
    """
    Set the move on board, if the coordinates are valid
    :param x: X coordinate
    :param y: Y coordinate
    :param player: the current player
    """
    if valid_move(x, y):
        board[x][y] = player
        return True
    else:
        return False


def minimax(state, depth, player):
    """
    AI function that choice the best move
    :param state: current state of the board
    :param depth: node index in the tree (0 <= depth <= 9),
    but never nine in this case (see iaturn() function)
    :param player: an human or a computer
    :return: a list with [the best row, best col, best score]
    """
    if player == COMP:
        best = [-1, -1, -infinity]
    else:
        best = [-1, -1, +infinity]

    # if depth == 0 or game_over(state):
    #     score = evaluate(state)
    #     return [-1, -1, score]


    if depth == 0 or game_over(state):
        score = evaluate(state)
        return [-1, -1, score]

    for cell in empty_cells(state):
        x, y = cell[0], cell[1]
        state[x][y] = player
        score = minimax(state, depth - 1, -player)
        state[x][y] = 0
        score[0], score[1] = x, y

        if player == COMP:
            if score[2] > best[2]:
                best = score  # max value
        else:
            if score[2] < best[2]:
                best = score  # min value

    return best


def clean():
    """
    Clears the console
    """
    os_name = platform.system().lower()
    if 'windows' in os_name:
        system('cls')
    else:
        system('clear')


def render(state, c_choice, h_choice):
    """
    Print the board on console
    :param state: current state of the board
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
        print('You WIN!')
    else:
        clean()
        render(board, c_choice, h_choice)
        print('DRAW!')

    exit()


if __name__ == '__main__':
    main()
