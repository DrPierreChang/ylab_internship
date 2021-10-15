
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
