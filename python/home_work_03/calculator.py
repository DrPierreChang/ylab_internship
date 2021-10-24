from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.config import Config
from kivy.uix.image import Image
from area_volume import GeometricFigures, VolumetricFigures

Config.set("graphics", "resizable", "0")
Config.set("graphics", "width", "300")
Config.set("graphics", "height", "300")


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
            "Пирамида": "Для S введите a,n, h. Для V s и h через пробел",
            "Трапеция": "Для S введите a, b и h через пробел:",
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
                            f"Площадь {name.lower()}а равна:"
                    else:
                        self.box2.text = str(
                            figure.area(data, figure_name=f"{name}"))
                        self.image.source = 'instruction.png'
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
                    self.image.source = 'instruction.png'
                    if name == "Сфера" or name == "Пирамида":
                        self.box1.text = f"Объём {name[0:-1].lower()}ы равен:"
                    else:
                        self.box1.text = f"Объём {name.lower()}а равен:"
                except ValueError:
                    self.box2.text = ""

    def build(self):
        self.title = 'Геометрический Калькулятор'
        root = BoxLayout(orientation="vertical", padding=5)

        self.image = Image(source="instruction.png")

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
