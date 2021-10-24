from math import pi, tan, radians
import numpy as np
import matplotlib.pyplot as plt


class GeometricFigures:
    """
    Данный класс содержит методы,
    которые доступны могут иметь все фигуры - площадь, визуализация
    Визуализация пока доступна только для круга и квадрата
    """

    # Класс имеет свойство площадь.
    # Она будет считаться и возвращаться пользователю
    figure_area = 0

    def area(self, data: str, figure_name="") -> float:
        """
        В методе считается площадь для всех фигур
        Данные от пользователя приходят в виде строки
        :param data: аргументы для вычисления площади определенной фигуры
        :param figure_name: имя фигуры для которой нужно посчитать площадь
        :return: возвращается посчитанная площадь
        """
        # в зависимости от имени фигуры, подбираем формулу
        if figure_name == "Круг":
            self.figure_area += (float(data)**2 * pi)
        elif figure_name == "Сфера":
            self.figure_area += (float(data)**2 * pi * 4)
        elif figure_name == "Квадрат":
            self.figure_area += (float(data)**2)
        elif figure_name == "Куб":
            self.figure_area += (float(data)**2 * 6)
        elif figure_name == "Прямоугольник":
            self.figure_area += (np.prod([float(i) for i in data.split()]))
        elif figure_name == "Параллелепипед":
            abc = data.split()
            if len(abc) == 3:
                a, b, c = float(abc[0]), float(abc[1]), float(abc[2])
                self.figure_area += (2 * ((a * b) + (b * c) + (a * c)))
        elif figure_name == "Треугольник":
            bh = data.split()
            b, h = float(bh[0]), float(bh[1])
            self.figure_area += (0.5 * b * h)
        # по названию нажатой кнопки подбирается необходимая формула
        elif figure_name == "Пирамида":
            # a - длина стороны n - количество сторон  h - высота пирамиды
            anh = data.split()
            # данные от пользователя приходят строкой,
            # поэтому они преобразуются для дальнейших вычислений
            a, n, h = float(anh[0]), float(anh[1]), float(anh[2])
            # считается площадь
            s = ((n * a)/2) * ((a/(2*tan(radians(180)/n))) +
                               (h**2 + (a/(2*tan(radians(180)/n)))**2)**0.5)
            self.figure_area += s
        elif figure_name == "Трапеция":
            abh = data.split()
            if len(abh) == 3:
                a, b, h = float(abh[0]), float(abh[1]), float(abh[2])
                self.figure_area += ((a + b)/2) * h
        elif figure_name == "Цилиндр":
            rh = data.split()
            if len(rh) == 2:
                r, h = float(rh[0]), float(rh[1])
                self.figure_area += ((2 * pi * r * h) + (2 * pi * r**2))
        elif figure_name == "Ромб":
            ah = data.split()
            if len(ah) == 2:
                a, h = float(ah[0]), float(ah[1])
                self.figure_area += a * h
        elif figure_name == "Конус":
            rh = data.split()
            if len(rh) == 2:
                r, h = float(rh[0]), float(rh[1])
                s = pi * r * (r + (r**2 + h**2)**0.5)
                self.figure_area += s
        # результат возвращается пользователю
        return self.figure_area

    def plot(self, data: str, figure_name=""):
        """
        Метод предназначен для визуализации фигур
        :param data: данные, которые пользователь ввел для расчета площади
        :param figure_name: имя фигуры, для которой производится расчет
        :return: метод ничего не возвращает. Он сохраняет plot в файл
        """
        cm = 1/2.54

        # задаем плоскость для визуализации
        # по умолчанию matplotlib использует inch,
        # но можно использовать сантиметры, если пользоваться переводом
        figure, axes = plt.subplots(figsize=(20*cm, 10*cm))
        axes.set_aspect(1)

        # если фигура круг
        if figure_name == "Круг":
            # строим круг с ориентацией по x,y 0.5
            circle = plt.Circle((0.5, 0.5), float(data)*cm)
            axes.add_patch(circle)

        # если фигура квадрат, то он строится с началом по x, y 0.1
        elif figure_name == "Квадрат":
            square =\
                plt.Rectangle((0.1, 0.1), float(data)*cm, float(data)*cm)
            axes.add_patch(square)

        # добавляем название фигуры на график
        plt.title(f"{figure_name}")
        # сохраняем график в файл
        # это файл будет загружаться калькулятором и отображаться
        figure.savefig('plot.png')


class VolumetricFigures(GeometricFigures):
    """
    Класс содержит методы объемных фигур
    """

    # основное свойство объемных фигур - объем.
    # он считается и возвращается пользователю
    figure_volume = 0

    def volume(self, data: str, figure_name="") -> float:
        """
        Метод считает объем для объемных фигур
        :param data: данные, введенные пользователем
        :param figure_name: название фигуры
        :return: метода возвращает посчитанный объем
        """
        # если выбрана сфера
        if figure_name == "Сфера":
            # используем формулу
            self.figure_volume += (4/3 * pi * float(data)**3)
        # если пользователь выбрал пирамиду
        elif figure_name == "Пирамида":
            # так как данные приходят строкой
            # то мы дополнительно их обрабатываем и проверяем
            sh = data.split()
            if len(sh) == 2:
                s, h = float(sh[0]), float(sh[1])
                # v = 1/3Sh h - высота пирамиды S - площадь основания
                self.figure_volume += (1/3) * s * h
        # если выбран куб считаем по формуле
        elif figure_name == "Куб":
            self.figure_volume += (float(data)**3)
        elif figure_name == "Параллелепипед":
            #  a - длина b ширина h высота
            abh = data.split()
            if len(abh) == 3:
                # формула для объема параллелепипеда
                a, b, h = float(abh[0]), float(abh[1]), float(abh[2])
                self.figure_volume += (a * b * h)
        elif figure_name == "Цилиндр":
            # из полученных данных создаем список с радиусом и высотой
            rh = data.split()
            # если введены два параметра, как нужно для расчета
            if len(rh) == 2:
                # радиус первый элемент, высота второй элемент
                r, h = float(rh[0]), float(rh[1])
                # формула объема цилиндра v = pi * r **2 * h
                self.figure_volume += (pi * r**2 * h)
        elif figure_name == "Конус":
            # из полученных данных создаем список с радиусом и высотой
            rh = data.split()
            # если введены два параметра, как нужно для расчета
            if len(rh) == 2:
                # радиус первый элемент, высота второй элемент
                r, h = float(rh[0]), float(rh[1])
                # формула объема конуса v = 1/3 * pi * r**2 * h
                self.figure_volume += (1/3 * pi * r**2 * h)
        return self.figure_volume
