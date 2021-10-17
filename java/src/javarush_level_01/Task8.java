package javarush_level_01;

import java.util.Scanner;

public class Task8 {
    public static void main(String[] args) {
        int a, b, c;
        String s1, s2;
        s2 = "Слава Роботам! Убить всех человеков!";
//        System.out.println("Введите два числа:");
//        a = new Scanner(System.in).nextInt();
//        b = new Scanner(System.in).nextInt();
//        c = a + b;
//        System.out.println("Сумма ваших чисел равна " + c);
//        sqr(2);

        doubleWrite(s2);

//        System.out.println("Nothing personal, it's just business.");

    }

    public static void sqr(int a) {               // функция с типом возвращаемого элемента int
        System.out.println(a * a);
    }

    public static void doubleWrite(String s) {
        for(int i = 0; i < 16; i++) {
            System.out.println(i+1 + ") " + s);
        }
    }
}
