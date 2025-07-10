import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        long r = input.nextLong();
        long c = input.nextLong();
        long n = input.nextLong();

        r = (r % n > 0) ? r / n + 1 : r / n;
        c = (c % n > 0) ? c / n + 1 : c / n;

        System.out.println(r * c);
    }
}