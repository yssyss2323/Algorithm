import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        Scanner input = new Scanner(System.in);

        int n = input.nextInt();
        input.nextLine();
        String states = input.nextLine();

        int[] arr = new int[n];
        int tot = 0;
        for (int i = 0; i < n; i++) {
            char tmp = states.charAt(i);
            if (tmp == 'R') {
                arr[i] = 0;
            } else if (tmp == 'G') {
                arr[i] = 1;
            } else {
                arr[i] = 2;
            }
            tot += arr[i];
        }

        int ans = 3 * n; // 그냥 적당히 큰 수
        for (int targetNum = 0; targetNum < 3; targetNum++) {

            if ((targetNum * n) % 3 == tot % 3) {
                int tmp = 0;
                int[] copy = arr.clone();
                for (int i = 0; i < n - 2; i++) {
                    while (copy[i] != targetNum) {
                        for (int j = i; j < i + 3; j++) {
                            copy[j] = (copy[j] + 1) % 3;
                        }
                        tmp++;
                    }
                }

                if (copy[n - 2] == targetNum && copy[n - 1] == targetNum) {
                    if (ans > tmp) ans = tmp;
                }
            }
        }
        if (ans == 3 * n) ans = -1;

        System.out.println(ans);
    }
}