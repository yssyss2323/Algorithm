import java.util.Arrays;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        scanner.nextLine();

        int[] arr = new int[n];
        int ans = 0;
        for (int i = 0; i < n; i++) {
            int cnt = scanner.nextInt();
            int tmp = 0;
            for (int j = 0; j < cnt; j++) {
                tmp += scanner.nextInt();
            }
            arr[i] = tmp;
        }
        Arrays.sort(arr);
        int tmp = 0;
        for (int i = 0; i < n; i++) {
            tmp += arr[i];
            ans += tmp;
        }
        System.out.println(ans);
    }
}
