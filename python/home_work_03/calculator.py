from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.config import Config
from kivy.uix.image import Image
from math import pi

Config.set("graphics", "resizable", "0")
Config.set("graphics", "width", "300")
Config.set("graphics", "height", "300")

saveImage = ""


class Circles:
    circle_area = 0
    radius = ""

    def area(self, radius: int):
        """
        :param radius: Радиус круга
        :return: Площадь круга
        """
        self.circle_area = self.circle_area + (pi * (float(radius)**2))
        return self.circle_area


class Squares:
    square_area = 0
    side = ""

    def area(self, side):
        self.square_area = self.square_area + float(side) ** 2
        return self.square_area


class CalculatorApp(App, Circles, Squares):

    def calculate_circles(self, symbol):
        c = Circles()
        if symbol.text == "Круг":
            self.result.text = "Введите радиус круга"
            self.result2.text = ""

        else:
            try:
                self.result2.text = str(c.area(self.result2.text))
                self.image.source = 'b1.jpg'
            except:
                self.result2.text = ""

    def calculate_squares(self, symbol):
        s = Squares()
        if symbol.text == "Квадрат":
            self.result.text = "Введите сторону квадрата"
            self.result2.text = ""
        else:
            try:
                self.result2.text = str(s.area(self.result2.text))
                self.image.source = 'b1.jpg'
            except:
                self.result2.text = ""

    def build(self):
        root = BoxLayout(orientation="vertical", padding=5)

        self.result = TextInput(
                text="", readonly=False, font_size=25,
                size_hint=[1, .20], background_color=[1, 1, 1, .8])

        self.result2 = TextInput(
            text="Выберите фигуру: ", readonly=False, font_size=25,
            size_hint=[1, .20], background_color=[1, 1, 1, .8])

        self.image = Image(source="b1.jpg")

        root.add_widget(self.image)
        root.add_widget(self.result)
        root.add_widget(self.result2)

        all_buttons = GridLayout(cols=2)

        all_buttons.add_widget(Button(text="Круг", on_press=self.calculate_circles))
        all_buttons.add_widget(Button(text="Площадь Круга", on_press=self.calculate_circles))
        all_buttons.add_widget(Button(text="Квадрат", on_press=self.calculate_squares))
        all_buttons.add_widget(Button(text="Площадь Квадрата", on_press=self.calculate_squares))

        root.add_widget(all_buttons)
        return root


if __name__ == "__main__":
    CalculatorApp().run()
