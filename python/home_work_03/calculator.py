from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.config import Config
from kivy.uix.image import Image
from math import pi
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle

Config.set("graphics", "resizable", "0")
Config.set("graphics", "width", "300")
Config.set("graphics", "height", "300")


class GeometricFigures:
    figure_area = 0

    def area(self, *args, name = "") -> float:
        """
        :param args: список аргументов для вычисления площади определенной фигуры
        :return: возвращается посчитанная площадь
        """
        if name == "Равносторонний Треугольник":
            self.figure_area = self.figure_area + (((args[0]**2)*(3**0.5)) / 4)
        else:
            self.figure_area = self.figure_area + (np.prod([i for i in args]))
        return self.figure_area

    def plot(self, *args, name="Круг"):
        # r = args[0]
        # define Matplotlib figure and axis
        cm = 1/2.54
        figure, axes = plt.subplots(figsize=(30*cm, 10*cm))
        axes.set_aspect(1)

        if name == "Круг":
            # add rectangle to plot
            axes.add_patch(Circle((0.5, 0.5), *args))
        elif name == "Квадрат" or name == "Прямоугольник":
            axes.add_patch(Rectangle((0.1, 0.1), *args))

        plt.title(f'{name}')
        plt.savefig('plot.png')


class GeometricCalculatorApp(App):

    def calculate(self, symbol):
        figure = GeometricFigures()
        global name
        if symbol.text == "Круг":
            self.result.text = "Введите радиус круга:"
            self.result2.text = ""
            name = symbol.text
        elif symbol.text == "Сфера":
            self.result.text = "Введите радиус сферы:"
            self.result2.text = ""
            name = symbol.text
        elif symbol.text == "Квадрат":
            self.result.text = "Введите сторону квадрата:"
            self.result2.text = ""
            name = symbol.text
        elif symbol.text == "Прямоугольник":
            self.result.text = "Введите стороны a и b через пробел:"
            self.result2.text = ""
            name = symbol.text
        elif symbol.text == "Разносторонний Треугольник":
            self.result.text = "Введите основание и высоту через пробел:"
            self.result2.text = ""
            name = symbol.text
        elif symbol.text == "Равносторонний Треугольник":
            self.result.text = "Введите длину стороны:"
            self.result2.text = ""
            name = symbol.text
        elif symbol.text == "Трапеция":
            self.result.text = "Введите основание a, основание b и высоту h через пробел:"
            self.result2.text = ""
            name = symbol.text
        elif symbol.text == "Ромб":
            self.result.text = "Введите основание a и высоту h через пробел:"
            self.result2.text = ""
            name = symbol.text

        else:
            try:
                if name == "Круг":
                    self.result2.text = str(figure.area(float(self.result2.text)**2, pi))
                    figure.plot(((float(self.result2.text)**0.5)/pi)/2.54, name="Круг")
                    self.image.source = 'plot.png'
                    self.image.reload()
                    self.result.text = "Площадь круга равна:"
                elif name == "Сфера":
                    self.result2.text = str(figure.area(float(self.result2.text)**2, pi, 4))
                    figure.plot((((float(self.result2.text)**0.5)/pi)/4)/2.54, name="Сфера")
                    self.image.source = 'b1.png'
                    self.image.reload()
                    self.result.text = "Площадь сферы равна:"
                elif name == "Квадрат":
                    self.result2.text = str(figure.area(float(self.result2.text)**2))
                    figure.plot((float(self.result2.text)**0.5)/2.54,
                                (float(self.result2.text)**0.5)/2.54, name="Квадрат")
                    self.image.source = 'plot.png'
                    self.image.reload()
                    self.result.text = "Площадь квадрата равна:"
                elif name == "Прямоугольник":
                    ab = self.result2.text.split()
                    if len(ab) == 2:
                        a = float(ab[0])
                        b = float(ab[1])
                        self.result2.text = str(figure.area(a, b))
                        figure.plot(a, b, name="Прямоугольник")
                        self.image.source = 'plot.png'
                        self.image.reload()
                        self.result.text = "Площадь прямоугольника равна:"
                elif name == "Разносторонний Треугольник":
                    self.result2.text = str(figure.area(*[float(i) for i in self.result2.text.split()], 0.5))
                    self.image.source = 'b1.jpg'
                    self.result.text = "Площадь треугольника равна:"
                elif name == "Равносторонний Треугольник":
                    self.result2.text = str(figure.area(float(self.result2.text), name="Равносторонний Треугольник"))
                    self.image.source = 'b1.jpg'
                    self.result.text = "Площадь треугольника равна:"
                elif name == "Трапеция":
                    abh = self.result2.text.split()
                    if len(abh) == 3:
                        a, b, h = float(abh[0]), float(abh[1]), float(abh[2])
                        self.result2.text = str(figure.area((a + b)/2, h))
                        self.image.source = 'b1.jpg'
                        self.result.text = "Площадь трапеции равна:"
                elif name == "Ромб":
                    ah = self.result2.text.split()
                    if len(ah) == 2:
                        a, h = float(ah[0]), float(ah[1])
                        self.result2.text = str(figure.area(a, h))
                        self.image.source = 'b1.jpg'
                        self.result.text = "Площадь ромба равна:"
            except ValueError:
                self.result2.text = ""

    def build(self):
        self.title = 'Геометрический Калькулятор'
        root = BoxLayout(orientation="vertical", padding=5)

        # цвет фона указывается в rgba
        self.result = TextInput(
                text="", readonly=True, font_size=25,
                size_hint=[1, .20], background_color=[1, 1, 1, .8])

        self.result2 = TextInput(
            text="Выберите фигуру: ", readonly=False, font_size=25,
            size_hint=[1, .20], background_color=[1, 1, 1, .8])

        self.image = Image(source="b1.jpg")

        root.add_widget(self.image)
        root.add_widget(self.result)
        root.add_widget(self.result2)

        all_buttons = GridLayout(cols=3)

        all_buttons.add_widget(Button(text="Круг", on_press=self.calculate))
        all_buttons.add_widget(Button(text="Сфера", on_press=self.calculate))
        all_buttons.add_widget(Button(text="Медиана", background_normal='',
                                      background_color=[.25, .53, .56, 1],
                                      on_press=self.calculate))

        all_buttons.add_widget(Button(text="Ромб", on_press=self.calculate))
        all_buttons.add_widget(Button(text="Конус", on_press=self.calculate))
        all_buttons.add_widget(Button(text="Площадь", background_normal='',
                                      background_color=[.25, .53, .56, 1], on_press=self.calculate))


        all_buttons.add_widget(Button(text="Разносторонний Треугольник", on_press=self.calculate))
        all_buttons.add_widget(Button(text="Равносторонний Треугольник", on_press=self.calculate))
        all_buttons.add_widget(Button(text="Пирамида", on_press=self.calculate))



        all_buttons.add_widget(Button(text="Квадрат", on_press=self.calculate))
        all_buttons.add_widget(Button(text="Куб", on_press=self.calculate))
        all_buttons.add_widget(Button(text="", on_press=self.calculate))


        all_buttons.add_widget(Button(text="Прямоугольник", on_press=self.calculate))
        all_buttons.add_widget(Button(text="Параллелепипед", on_press=self.calculate))
        all_buttons.add_widget(Button(text="", on_press=self.calculate))


        all_buttons.add_widget(Button(text="Трапеция", on_press=self.calculate))

        all_buttons.add_widget(Button(text="Цилиндр", on_press=self.calculate))
        all_buttons.add_widget(Button(text="", on_press=self.calculate))





        root.add_widget(all_buttons)
        return root


if __name__ == "__main__":
    GeometricCalculatorApp().run()
