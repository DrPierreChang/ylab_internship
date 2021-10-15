
### <p align="center">Логика работы</p>

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
~~~~
### <p align="center">tictactoe.py</p>
В файл tictactoe.py вынесены некоторые функции:

~~~~python
def choose_color(text: str): ...
~~~~~

Функция принимает строку и возвращает цвет в виде [ANSI escape code](https://en.wikipedia.org/wiki/ANSI_escape_code) в зависимости от принятого значения

Это необходимо, чтобы раскрасить X, O и другие элементы разными цветами при игре в консоли

<p align="center"><img src="images/choose_color.png" alt = "example of function return" width="450"></p>

### <p align="center">Источники информации</p>
Google:
- [Print Colors in Python terminal](https://www.geeksforgeeks.org/print-colors-python-terminal/)
- [ПРИНЦИП МАКСИМИНА (МИНИМАКСА)](http://www.math.mrsu.ru/text/courses/method/princip_maxmin_minmax.htm)
- [Минимакс и максимакс](https://math.semestr.ru/games/minimax.php)

Wiki:
- [ANSI escape code](https://en.wikipedia.org/wiki/ANSI_escape_code)

Stack Overflow:
- [What is wrong with my minimax algorithm for tictactoe](https://stackoverflow.com/questions/31617469/what-is-wrong-with-my-minimax-algorithm-for-tictactoe)

YouTube
- [Algorithms Explained – minimax and alpha-beta pruning](https://youtu.be/l-hh51ncgDI)
- [What is the Minimax Algorithm? - Artificial Intelligence](https://youtu.be/KU9Ch59-4vw)