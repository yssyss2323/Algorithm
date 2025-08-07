import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner input = new  Scanner(System.in);
        int t =  input.nextInt();
        for (int i = 0; i < t; i++) {
            long ans = 0;
            int n = input.nextInt();
            int[] arr = new int[n];
            for (int j = 0; j < n; j++) {
                arr[j] = input.nextInt();
            }
            for (int j = 0; j < n - 1; j++) {
                for (int k = j + 1; k < n; k++) {
                    ans += gcd(arr[j], arr[k]);
                }
            }
            System.out.println(ans);
        }
    }
    public static int gcd(int a, int b) {
        return b == 0 ? a : gcd(b, a % b);
    }
}
