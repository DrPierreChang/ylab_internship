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

global saveInput2
saveInput2 = ""

class Build_app(App):

    global result2
    result2 = TextInput(
        text="Выберите фигуру: ", readonly=False, font_size=25,
        size_hint=[1, .20], background_color=[1, 1, 1, .8])

    global result

    result = TextInput(
        text="", readonly=False, font_size=25,
        size_hint=[1, .20], background_color=[1, 1, 1, .8])


    def build(self):
        root = BoxLayout(orientation="vertical", padding=5)

        self.image = Image(source = 'b1.jpg')

        root.add_widget(self.image)
        root.add_widget(result)
        root.add_widget(result2)

        allButtons = GridLayout(cols = 2)


        allButtons.add_widget(Button(text = 'Круг ', on_press = self.calculate_circles))
        allButtons.add_widget(Button(text="Площадь Круга", on_press=self.calculate_circles))
        allButtons.add_widget(Button(text='Квадрат ', on_press=self.calculate_squares))
        allButtons.add_widget(Button(text="Площадь Квадрата", on_press=self.calculate_squares))

        root.add_widget(allButtons)


        return root


class Circles(Build_app):
    circle_area = 0
    radius = ""

    def area(self, radius: int):
        """
        :param radius: Радиус круга
        :return: Площадь круга
        """
        self.circle_area = (self.circle_area) + (pi * (int(radius)**2))
        return self.circle_area


class Squares(Build_app):
    square_area = 0
    side = ""

    def area(self, side):
        self.square_area = (self.square_area) + int(side) ** 2
        return self.square_area


class CalculatorApp(Circles, Squares):

    def calculate_circles(self, symbol):
        if symbol.text == "Круг ":
            global c
            c = Circles()
            result.text = "Введите радиус круга"
            result2.text = ""

        else:
            try:
                result2.text = str(c.area(result2.text))
                self.image.source = 'b1.jpg'
                # result2.text = "Выберите фигуру: "
            except:
                result.text = ""

    def calculate_squares(self, symbol):
        if symbol.text == "Квадрат ":
            global s
            s = Squares()
            result.text = "Введите сторону квадрата"
            result2.text = ""
        else:
            try:
                result2.text = str(s.area(result2.text))
                self.image.source = 'b1.jpg'
            except:
                result.text = ""


if __name__ == "__main__":
    CalculatorApp().run()