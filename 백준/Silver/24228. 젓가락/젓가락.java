import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        long n = input.nextLong();
        long r = input.nextLong();

        System.out.println(n + 2 * r - 1);
    }
}