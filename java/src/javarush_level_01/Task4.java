package javarush_level_01;

public class Task4 {
    public static void main(String[] args) {
//        String s; объявление новой переменной способной хранить строку
//        int i;    объявление новой переменной способной хранить целое число
        String s = "Elly";
        int i = 5;

        int a = 5; // в переменной а хранится значение 5
        int b = 6; // в переменной b хранится значение 6
        int c = a + b; // в переменной c хранится значение 11

        // при вычислении нового значение переменной может использоваться ее старое значение
        c = c + c; // 22

        // строки можно конкатинировать
        String s1 = "Мама ";
        String s2 = "Мыла ";
        String s3 = s1 + s2 + "Раму";
//        System.out.println(s3);

        // добавляение пробела в текст
        s1 = "Мой любимый фильм";
        s2 = "Дорога";
        int roadNumber = 66;
        String text = s1 + " " + s2 + " " + roadNumber;
//        System.out.println(text);

        String name1 = "Andrey";
        String name2 = "Nikita";
        String name3 = "Igor";

        for (i=0; i < 10; i++){
            System.out.println(i + 1 + ") Когда я вырасту, то хочу быть паровым экскаватором!");
        }


    }
}
