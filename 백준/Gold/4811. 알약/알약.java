import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        int MAX = 30;
        Scanner input = new Scanner(System.in);

        long[][] dp = new long[MAX + 1][MAX + 1];
        for (int w = 0; w < MAX + 1; w++) {
            dp[w][0] = 1;
        }
        for (int w = 1; w < MAX + 1; w++) {
            for (int h = 1; h < MAX + 1; h++) {
                if (w < h) continue;
                dp[w][h] = dp[w - 1][h] + dp[w][h - 1];
            }
        }

        while (true) {
            int n = input.nextInt();
            if (n == 0) break;

            System.out.println(dp[n][n]);
        }
    }
}
