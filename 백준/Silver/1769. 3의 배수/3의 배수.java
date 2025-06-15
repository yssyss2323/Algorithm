import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String largeNumber = scanner.nextLine();

        int cnt = 0;
        while (largeNumber.length() > 1) {
            int tot = 0;
            for (int i = 0; i < largeNumber.length(); i++) {
                int num = largeNumber.charAt(i) - '0';
                tot += num;
            }
            largeNumber = String.valueOf(tot);
            cnt++;
        }
        System.out.println(cnt);
        int num = largeNumber.charAt(0) - '0';
        if (num % 3 != 0) {
            System.out.println("NO");
        } else {
            System.out.println("YES");
        }
    }
}
