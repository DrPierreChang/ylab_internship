package javarush_level_01; // имя пакета - директории
import java.io.IOException;

/**
 * User: General
 * Date: 12/21/12
 * Time 11:59
 */
public class Task1 { // имя класса

    private static String TEXT = "Hello from JavaRush!"; // переменная класса

    public static void main(String[] args) throws IOException{ // метод main
        System.out.println("Some text"); // вывод строчки на экран

    /*
    Это многострочный комментарий
    Код ниже выведет на экран три одинаковые строчки
     */
        String s = "Ho-ho-ho!"; //объявление переменной
        printTextMoreTimes(s,3);// вызов метода

    }

    public static void printTextMoreTimes(String s, int count) // заголовок и аргументы метода
    {
        for (int i = 0;i<count;i++) { // цикл
            System.out.println(s);
        }
    }
}
