import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        long a = input.nextLong();
        long b = input.nextLong();
        if (b - a >= 2) {
            System.out.println(b - a - 1);
            for (long i = a + 1; i < b - 1; i++) {
                System.out.print(i + " ");
            }
            System.out.print(b - 1);
        } else if (a - b >= 2) {
            System.out.println(a - b - 1);
            for (long i = b + 1; i < a - 1; i++) {
                System.out.print(i + " ");
            }
            System.out.print(a - 1);
        } else {
            System.out.println(0);
        }
    }
}