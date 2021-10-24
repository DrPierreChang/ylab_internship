import unittest
from calculator import GeometricFigures, VolumetricFigures


class TestArea(unittest.TestCase):
    def setUp(self):
        self.figure = GeometricFigures()

    def test_area_circle(self):
        self.assertEqual(self.figure.area(44, figure_name="Круг"),
                         6082.12337734984)

    def test_area_sphere(self):
        self.assertEqual(self.figure.area(4, figure_name="Сфера"),
                         201.06192982974676)

    def test_area_square(self):
        self.assertEqual(self.figure.area(7, figure_name="Квадрат"),
                         49)

    def test_area_cube(self):
        self.assertEqual(self.figure.area(4, figure_name="Куб"),
                         96)

    def test_area_rectangle(self):
        self.assertEqual(self.figure.area("3 15", figure_name="Прямоугольник"),
                         45)

    def test_area_parallelepiped(self):
        self.assertEqual(self.figure.area("1 2 3", figure_name="Параллелепипед"),
                         22)

    def test_area_triangle(self):
        self.assertEqual(self.figure.area("10 13", figure_name="Треугольник"),
                         65)

    def test_area_pyramid(self):
        self.assertEqual(self.figure.area("3 6 5", figure_name="Пирамида"),
                         74.09511041531074)

    def test_area_trapezoid(self):
        self.assertEqual(self.figure.area("1 2 3", figure_name="Трапеция"),
                         4.5)

    def test_area_cylinder(self):
        self.assertEqual(self.figure.area("5 6", figure_name="Цилиндр"),
                         345.5751918948772)

    def test_area_rhombus(self):
        self.assertEqual(self.figure.area("10 20", figure_name="Ромб"),
                         200.0)

    def test_area_cone(self):
        self.assertEqual(self.figure.area("5 10", figure_name="Конус"),
                         254.160184615763)


class TestVolume(unittest.TestCase):
    def setUp(self):
        self.figure = VolumetricFigures()

    def test_volume_sphere(self):
        self.assertEqual(self.figure.volume(2, figure_name="Сфера"),
                         33.510321638291124)

    def test_volume_pyramid(self):
        self.assertEqual(self.figure.volume("10 20", figure_name="Пирамида"),
                         66.66666666666666)

    def test_volume_cube(self):
        self.assertEqual(self.figure.volume(3, figure_name="Куб"),
                         27)

    def test_volume_parallelepiped(self):
        self.assertEqual(self.figure.volume("1 2 3", figure_name="Параллелепипед"),
                         6)

    def test_volume_cylinder(self):
        self.assertEqual(self.figure.volume("5 10", figure_name="Цилиндр"),
                         785.3981633974483)

    def test_volume_cone(self):
        self.assertEqual(self.figure.volume("5 10", figure_name="Конус"),
                         261.79938779914943)


if __name__ == '__main__':
    unittest.main()
