import unittest
from calculator import GeometricFigures, VolumetricFigures


class TestArea(unittest.TestCase):
    def test_area(self):
        with self.subTest():
            self.figure = GeometricFigures()
            self.assertEqual(self.figure.area(44, figure_name="Круг"),
                             6082.12337734984)
            self.figure = GeometricFigures()
            self.assertEqual(self.figure.area(4, figure_name="Сфера"),
                             201.06192982974676)
            self.figure = GeometricFigures()
            self.assertEqual(self.figure.area(7, figure_name="Квадрат"),
                             49)
            self.figure = GeometricFigures()
            self.assertEqual(self.figure.area(4, figure_name="Куб"),
                             96)
            self.figure = GeometricFigures()
            self.assertEqual(
                self.figure.area("3 15", figure_name="Прямоугольник"),
                45)
            self.figure = GeometricFigures()
            self.assertEqual(
                self.figure.area("1 2 3", figure_name="Параллелепипед"),
                22)
            self.figure = GeometricFigures()
            self.assertEqual(
                self.figure.area("10 13", figure_name="Треугольник"),
                65)
            self.figure = GeometricFigures()
            self.assertEqual(self.figure.area("3 6 5", figure_name="Пирамида"),
                             74.09511041531074)
            self.figure = GeometricFigures()
            self.assertEqual(self.figure.area("1 2 3", figure_name="Трапеция"),
                             4.5)
            self.figure = GeometricFigures()
            self.assertEqual(self.figure.area("5 6", figure_name="Цилиндр"),
                             345.5751918948772)
            self.figure = GeometricFigures()
            self.assertEqual(self.figure.area("10 20", figure_name="Ромб"),
                             200.0)
            self.figure = GeometricFigures()
            self.assertEqual(self.figure.area("5 10", figure_name="Конус"),
                             254.160184615763)


class TestVolume(unittest.TestCase):
    def test_volume(self):
        with self.subTest():
            self.figure = VolumetricFigures()
            self.assertEqual(self.figure.volume(2, figure_name="Сфера"),
                             33.510321638291124)
            self.figure = VolumetricFigures()
            self.assertEqual(self.figure.volume("10 20", figure_name="Пирамида"),
                             66.66666666666666)
            self.figure = VolumetricFigures()
            self.assertEqual(self.figure.volume(3, figure_name="Куб"),
                             27)
            self.figure = VolumetricFigures()
            self.assertEqual(self.figure.volume("1 2 3", figure_name="Параллелепипед"),
                             6)
            self.figure = VolumetricFigures()
            self.assertEqual(self.figure.volume("5 10", figure_name="Цилиндр"),
                             785.3981633974483)
            self.figure = VolumetricFigures()
            self.assertEqual(self.figure.volume("5 10", figure_name="Конус"),
                             261.79938779914943)


if __name__ == '__main__':
    unittest.main()
