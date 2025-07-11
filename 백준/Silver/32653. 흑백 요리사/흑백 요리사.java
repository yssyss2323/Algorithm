import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        int n = input.nextInt();

        int[] arr = new int[n];
        long ans = 1;
        for (int i = 0; i < n; i++) {
            arr[i] = input.nextInt() * 2;
            ans = ans * arr[i] / gcd(ans, arr[i]);
        }

        System.out.println(ans);

    }

    public static long gcd(long a, long b) {
        if (b == 0) {
            return a;
        }
        return gcd(b, a % b);
    }
}