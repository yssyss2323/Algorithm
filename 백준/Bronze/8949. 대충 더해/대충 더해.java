import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        Scanner input = new Scanner(System.in);
        int n = input.nextInt();
        int m = input.nextInt();

        long ans = 0;
        long ansCnt = 1;
        while (n > 0 | m > 0) {
            int nn = n % 10;
            n /= 10;
            int mm = m % 10;
            m /= 10;

            int tmp = nn + mm;
            int tmpCnt = nn + mm < 10 ? 10 : 100;

            ans += tmp * ansCnt;
            ansCnt *= tmpCnt;
        }
        System.out.println(ans);

    }
}
