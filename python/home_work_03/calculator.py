from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.config import Config
from kivy.uix.image import Image
from math import pi, tan, radians
import numpy as np
import matplotlib.pyplot as plt

Config.set("graphics", "resizable", "0")
Config.set("graphics", "width", "300")
Config.set("graphics", "height", "300")


class GeometricFigures:
    figure_area = 0

    def area(self, *args, figure_name="") -> float:
        """
        :param args: аргументов для вычисления площади определенной фигуры
        :param figure_name: имя фигуры для которой нужно посчитать площадь
        :return: возвращается посчитанная площадь
        """
        if figure_name == "Круг":
            self.figure_area += (float(*args)**2 * pi)
        elif figure_name == "Сфера":
            self.figure_area += (float(*args)**2 * pi * 4)
        elif figure_name == "Квадрат":
            self.figure_area += (float(*args)**2)
        elif figure_name == "Куб":
            self.figure_area += (float(*args)**2 * 6)
        elif figure_name == "Прямоугольник":
            self.figure_area += (np.prod([float(i) for i in args[0].split()]))
        elif figure_name == "Параллелепипед":
            abc = args[0].split()
            if len(abc) == 3:
                a, b, c = float(abc[0]), float(abc[1]), float(abc[2])
                self.figure_area += (2 * ((a * b) + (b * c) + (a * c)))
        elif figure_name == "Треугольник":
            bh = args[0].split()
            b, h = float(bh[0]), float(bh[1])
            self.figure_area += (0.5 * b * h)
        elif figure_name == "Пирамида":
            anh = args[0].split()
            a, n, h = float(anh[0]), float(anh[1]), float(anh[2])
            s = ((n * a)/2) * ((a/(2*tan(radians(180)/n))) +
                               (h**2 + (a/(2*tan(radians(180)/n)))**2)**0.5)
            self.figure_area += s
        elif figure_name == "Трапеция":
            abh = args[0].split()
            if len(abh) == 3:
                a, b, h = float(abh[0]), float(abh[1]), float(abh[2])
                self.figure_area += ((a + b)/2) * h
        elif figure_name == "Цилиндр":
            rh = args[0].split()
            if len(rh) == 2:
                r, h = float(rh[0]), float(rh[1])
                self.figure_area += ((2 * pi * r * h) + (2 * pi * r**2))
        elif figure_name == "Ромб":
            ah = args[0].split()
            if len(ah) == 2:
                a, h = float(ah[0]), float(ah[1])
                self.figure_area += a * h
        elif figure_name == "Конус":
            rh = args[0].split()
            if len(rh) == 2:
                r, h = float(rh[0]), float(rh[1])
                s = pi * r * (r + (r**2 + h**2)**0.5)
                self.figure_area += s
        return self.figure_area

    def plot(self, *args, figure_name=""):
        cm = 1/2.54

        # define Matplotlib figure and axis
        figure, axes = plt.subplots(figsize=(15*cm, 10*cm))
        axes.set_aspect(1)

        if figure_name == "Круг":
            circle = plt.Circle((0.5, 0.5), float(*args)*cm)
            axes.add_patch(circle)

        elif figure_name == "Квадрат":
            square =\
                plt.Rectangle((0.1, 0.1), float(*args)*cm, float(*args)*cm)
            axes.add_patch(square)

        plt.title(f'{name}')
        figure.savefig('plot.png')


class VolumetricFigures(GeometricFigures):
    figure_volume = 0

    def volume(self, *args, figure_name=""):
        if figure_name == "Сфера":
            self.figure_volume += (4/3 * pi * float(*args)**3)
        elif figure_name == "Пирамида":
            sh = args[0].split()
            if len(sh) == 2:
                s, h = float(sh[0]), float(sh[1])
                # v = 1/3Sh h - высота пирамиды S - площадь основания
                self.figure_volume += (1/3) * s * h
        elif figure_name == "Куб":
            self.figure_volume += (float(*args)**3)
        elif figure_name == "Параллелепипед":
            #  a - длина b ширина h высота
            abh = args[0].split()
            if len(abh) == 3:
                a, b, h = float(abh[0]), float(abh[1]), float(abh[2])
                self.figure_volume += (a * b * h)
        elif figure_name == "Цилиндр":
            # из полученных данных создаем список с радиусом и высотой
            rh = args[0].split()
            # если введены два параметра, как нужно для расчета
            if len(rh) == 2:
                # радиус первый элемент, высота второй элемент
                r, h = float(rh[0]), float(rh[1])
                # формула объема цилиндра v = pi * r **2 * h
                self.figure_volume += (pi * r**2 * h)
        elif figure_name == "Конус":
            # из полученных данных создаем список с радиусом и высотой
            rh = args[0].split()
            # если введены два параметра, как нужно для расчета
            if len(rh) == 2:
                # радиус первый элемент, высота второй элемент
                r, h = float(rh[0]), float(rh[1])
                # формула объема конуса v = 1/3 * pi * r**2 * h
                self.figure_volume += (1/3 * pi * r**2 * h)
        else:
            self.figure_volume += (np.prod([i for i in args]))
        return self.figure_volume


class GeometricCalculatorApp(App):
    def calculate(self, button):
        figure = GeometricFigures()
        volumetric_figure = VolumetricFigures()
        global welcome_message
        welcome_message = {
            "Круг": "Введите радиус круга:",
            "Сфера": "Введите радиус сферы:",
            "Квадрат": "Введите сторону квадрата:",
            "Куб": "Введите сторону куба:",
            "Прямоугольник": "Введите стороны a и b через пробел:",
            "Параллелепипед": "Введите стороны a, b и c через пробел:",
            "Треугольник": "Введите основание и высоту через пробел:",
            "Пирамида": "Введите основание a, число сторон основания n и высоту h:",
            "Трапеция": "Введите основание a, основание b и высоту h через пробел:",
            "Цилиндр": "Введите радиус r и высоту h цилиндра:",
            "Ромб": "Введите основание a и высоту h через пробел:",
            "Конус": "Введите радиус основания r и высоту h через пробел:"
        }
        global name
        if button.text in welcome_message:
            name = button.text
            self.box1.text = welcome_message[name]
            self.box2.text = ""
        else:
            if button.text == "Площадь":
                data = self.box2.text
                try:
                    if name == "Круг" or name == "Квадрат":
                        self.box2.text =\
                            str(figure.area(data, figure_name=f"{name}"))
                        figure.plot(data, figure_name=f"{name}")
                        self.image.source = 'plot.png'
                        self.image.reload()
                        self.box1.text =\
                            f"Площадь {name[0:-1].lower()}а равна:"
                    else:
                        self.box2.text = str(
                            figure.area(data, figure_name=f"{name}"))
                        self.image.source = 'instruction2.png'
                        self.box1.text = "Площадь фигуры равна:"
                except ValueError:
                    self.box2.text = ""
            # если нажата кнопка объём
            elif button.text == "Объём":
                data = self.box2.text
                try:
                    self.box2.text\
                        = str(volumetric_figure.volume(data,
                                                       figure_name=f"{name}"))
                    self.image.source = 'instruction2.png'
                    if name == "Сфера" or name == "Пирамида":
                        self.box1.text = f"Объём {name[0:-1].lower()}ы равен:"
                    else:
                        self.box1.text = f"Объём {name.lower()}а равен:"
                except ValueError:
                    self.box2.text = ""
    def build(self):
        self.title = 'Геометрический Калькулятор'
        root = BoxLayout(orientation="vertical", padding=5)

        self.image = Image(source="instruction2.png")

        # цвет фона указывается в rgba
        self.box1 = TextInput(
                text="", readonly=True, font_size=25,
                size_hint=[1, .20], background_color=[1, 1, 1, .8])

        self.box2 = TextInput(
            text="Выберите фигуру: ", readonly=False, font_size=25,
            size_hint=[1, .20], background_color=[1, 1, 1, .8])

        figure_buttons = GridLayout(cols=2)

        figures_ls = [
            "Круг", "Сфера", "Треугольник", "Пирамида", "Квадрат",
            "Куб", "Прямоугольник", "Параллелепипед", "Трапеция",
            "Цилиндр", "Ромб", "Конус"]

        for i in figures_ls:
            figure_buttons.add_widget(
                Button(text=f"{i}", on_press=self.calculate))

        action_buttons = GridLayout(cols=1, size_hint=[1, .30])
        for i in ["Площадь", "Объём"]:
            action_buttons.add_widget(Button(text=f"{i}",
                                             background_color=[.19, 1, 1, 1],
                                             on_press=self.calculate))

        root.add_widget(self.image)
        root.add_widget(self.box1)
        root.add_widget(self.box2)
        root.add_widget(figure_buttons)
        root.add_widget(action_buttons)
        return root


if __name__ == "__main__":
    GeometricCalculatorApp().run()
