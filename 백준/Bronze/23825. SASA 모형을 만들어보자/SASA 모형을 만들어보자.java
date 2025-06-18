import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        int n = input.nextInt();
        int m = input.nextInt();

        int ans = n / 2;
        if (ans > m / 2) ans = m / 2;
        System.out.println(ans);
    }
}
