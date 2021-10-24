from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.config import Config
from kivy.uix.image import Image
from area_volume import GeometricFigures, VolumetricFigures

# конфигурация окна kivy приложения
# параметры высоты, ширины окна
Config.set("graphics", "resizable", "0")
Config.set("graphics", "width", "300")
Config.set("graphics", "height", "300")


class GeometricCalculatorApp(App):
    """
    Данный класс содержит методы,
    которые конструируют приложение kivy и взаимодействуют с пользователем
    """
    # метод взаимодействующий с пользователем
    def calculate(self, button) -> None:
        """
        :param button: нажатая кнопка, которая хранит ее название
        """
        #  создается объект геометрическая фигура
        figure = GeometricFigures()
        # создается объект объемная фигура
        volumetric_figure = VolumetricFigures()
        # сообщение, которое выводится при выборе фигуры
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
        # при выборе фигуры выводится предложение ввести необходимые данные
        if button.text in welcome_message:
            # сохраняется имя выбранной фигуры
            name = button.text
            self.box1.text = welcome_message[name]
            # нижний текст бокс освобождается, чтобы пользователь ввел данные
            self.box2.text = ""
        else:
            # если нажата кнопка площади
            if button.text == "Площадь":
                # данные введенные в текстовом поле
                data = self.box2.text
                try:
                    # направляем данные в метод area
                    # вместе с названием фигуры, чтобы именно для нее
                    # подобрать формулу
                    if name == "Круг" or name == "Квадрат":
                        self.box2.text =\
                            str(figure.area(data, figure_name=f"{name}"))
                        # также данные направляются в метод plot
                        # чтобы показать визуализацию
                        # но только если фигура - квадрат или круг
                        figure.plot(data, figure_name=f"{name}")
                        # выводим визуализацию
                        self.image.source = 'plot.png'
                        # перезагружаем изображение,
                        # на случай если оно изменилось
                        self.image.reload()
                        # выводим результат расчета
                        self.box1.text =\
                            f"Площадь {name.lower()}а равна:"
                    else:
                        # информация введенная пользователем идет в метод area
                        # также туда идет название фигуры, чтобы посчитать
                        # для нее площадь
                        self.box2.text = str(
                            figure.area(data, figure_name=f"{name}"))
                        # изображение, которое показывается после подсчета
                        self.image.source = 'instruction.png'
                        # сообщение будет показано вместе с результатом
                        self.box1.text = "Площадь фигуры равна:"
                except ValueError:
                    # если введены некорректные данные
                    self.box2.text = ""
            # если нажата кнопка объём
            elif button.text == "Объём":
                # данные введенные в нижнее текстовое поле
                data = self.box2.text
                try:
                    # для расчета объема данные отправляются в метод volume
                    # вместе с именем выбранной фигуры
                    # чтобы именно для нее подобрать формулу
                    self.box2.text\
                        = str(volumetric_figure.volume(data,
                                                       figure_name=f"{name}"))
                    # после расчета на экране отображается инструкция
                    self.image.source = 'instruction.png'
                    # в зависимости от названия фигуры
                    # меняем окончание в ее названии, чтобы вывести результат
                    if name == "Сфера" or name == "Пирамида":
                        self.box1.text = f"Объём {name[0:-1].lower()}ы равен:"
                    else:
                        self.box1.text = f"Объём {name.lower()}а равен:"
                # если от пользователя пришли некорректны данные
                except ValueError:
                    self.box2.text = ""

    # метод конструирует приложение kivy
    def build(self):
        # название, которое отображается в окне приложения
        self.title = 'Геометрический Калькулятор'
        # создание главного окна
        root = BoxLayout(orientation="vertical", padding=5)

        # создание окна для показа изображения
        self.image = Image(source="instruction.png")

        # создание полей ввода текста
        # цвет фона указывается в rgba
        self.box1 = TextInput(
                text="", readonly=True, font_size=25,
                size_hint=[1, .20], background_color=[1, 1, 1, .8])
        self.box2 = TextInput(
            text="Выберите фигуру: ", readonly=False, font_size=25,
            size_hint=[1, .20], background_color=[1, 1, 1, .8])

        # создание элемента включающего кнопки
        # кнопки будут располагаться одна за одной в две колоны
        figure_buttons = GridLayout(cols=2)

        # в цикле добавляем в приложение все кнопки фигур
        figures_ls = [
            "Круг", "Сфера", "Треугольник", "Пирамида", "Квадрат",
            "Куб", "Прямоугольник", "Параллелепипед", "Трапеция",
            "Цилиндр", "Ромб", "Конус"]

        for i in figures_ls:
            figure_buttons.add_widget(
                Button(text=f"{i}", on_press=self.calculate))

        # создаются кнопки для расчетов
        action_buttons = GridLayout(cols=1, size_hint=[1, .30])
        for i in ["Площадь", "Объём"]:
            action_buttons.add_widget(Button(text=f"{i}",
                                             background_color=[.19, 1, 1, 1],

                                             on_press=self.calculate))
        # в главное окно добавляются все элемент
        root.add_widget(self.image)
        root.add_widget(self.box1)
        root.add_widget(self.box2)
        root.add_widget(figure_buttons)
        root.add_widget(action_buttons)
        return root


if __name__ == "__main__":
    GeometricCalculatorApp().run()
