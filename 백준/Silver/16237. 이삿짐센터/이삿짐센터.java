import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        Scanner input = new Scanner(System.in);

        int[] arr = new int[5];
        for (int i = 0; i < 5; i++) {
            arr[i] = input.nextInt();
        }

        int ans = arr[4];

        ans += arr[3];
        if (arr[0] >= arr[3]) {
            arr[0] -= arr[3];
        } else {
            arr[0] = 0;
        }

        ans += arr[2];
        if (arr[1] >= arr[2]) {
            arr[1] -= arr[2];
        } else {
            if (arr[0] >= (arr[2] - arr[1]) * 2) {
                arr[0] -= (arr[2] - arr[1]) * 2;
            } else {
                arr[0] = 0;
            }
            arr[1] = 0;
        }

        ans += arr[1] / 2;
        if (arr[0] >= arr[1] / 2) {
            arr[0] -= arr[1] / 2;
        } else {
            arr[0] = 0;
        }
        if (arr[1] % 2 == 1) {
            ans += 1;
            if (arr[0] >= 3) {
                arr[0] -= 3;
            } else {
                arr[0] = 0;
            }
        }

        ans += arr[0] / 5;
        if (arr[0] % 5 > 0) {
            ans += 1;
        }

        System.out.println(ans);
    }
}
